#include "3140_concur.h"
#include <stdlib.h>
#include <MKL46Z4.h>
#include "shared_structs.h"

process_t * current_process = NULL;
process_t * queue_start = NULL;

struct process_state * pop_from_start_of_linked_list() {
/*
* Returns the first item in the process queue.
* There are two possibilities: if the list is not empty move the second item in the queue to the first place
* and return the first.
* Otherwise return NULL.
*/
	if (queue_start != NULL) {

	/*
	* Create a temporary pointer variable to store the value queue_start points to while being able to make queue_start
	* point to something else (the next process in the queue)
	*/

		process_t * top_node = queue_start;

		queue_start = queue_start->next;
		top_node->next = NULL;
		return top_node;

	} else {
		return NULL;
	}
}

void add_process_to_queue(process_t * new_pointer) {
/*
* This function adds an element to the process of our process queue, which is implemented as a linked list.
* There are two possibilities: is the list empty? If so simply set queue_start to be the new_pointer (the function's argument)
* Otherwise find the last node and make its ->next be the new_pointer. Set new_pointer's next to NULL.
*/
	process_t *tmp;
	if (queue_start == NULL) {
		queue_start = new_pointer;
		queue_start->next = NULL;
	}
	else{
		tmp = queue_start;
		while (tmp->next != NULL) {
			/*  if there are more elements in the list
			tmp will have a process_t element stored in .next.
			While the process queue is not empty replace
			the pointer with its next value
			*/
			tmp = tmp->next;
		}
		// now tmp is the last element in the list
		tmp->next = new_pointer;
		new_pointer->next = NULL;
	}
}


int process_create (void (*f)(void), int a) {
/*
* Creates a process, checks that there is enough memory to do so and initializes the necessary fields
* (stack base, pointer and size) if creating the process is possible. Add the new process to the end of the
* process queue.
*/
	unsigned int *init_proc; //pointer to an unsigned
	process_t *new_pointer; //pointer to the process structure
	init_proc = process_stack_init (f, a);
	new_pointer = malloc(sizeof(process_t));

	//check that there is enough memory to create this process
	if (init_proc == NULL || new_pointer == NULL) {
		return -1;
	} else {
		new_pointer->sp = init_proc;
		new_pointer->stack_base = init_proc; //at the beginning they're the same
		new_pointer->n = a;
		new_pointer->is_blocked = false;

		add_process_to_queue(new_pointer); //tell my partner what i'm doing and why i'm deleting new_process
		return 0;
	}

}

void process_start (void) {
/*
* Initializes the hardware needed to begin concurrent processes by enabling the PIT IRQ, the PIT, loading a value to the PIT
* and starting it. Calls process_begin() at the end.
*/
	// enable the PIT IRQ
	NVIC_EnableIRQ(PIT_IRQn);
	//enable PIT
	SIM->SCGC6 = SIM_SCGC6_PIT_MASK;
	//turn PIT on
	PIT->MCR &= ~PIT_MCR_MDIS_MASK;

	PIT->CHANNEL[1].LDVAL = 0xffffffff;

	PIT->CHANNEL[1].TCTRL = 7;
	//load a few miliseconds to the PIT timer
	PIT->CHANNEL[0].LDVAL = 0xffffffff;
	//enable interrupts
	PIT->CHANNEL[0].TCTRL = 1;

	//set the current process to the first process in the queue
	process_begin();
}


unsigned int * process_select(unsigned int * cursp) {
	/*
	* If there is a process to run, this function returns where to run it (the relevant stack pointer), since
	* part of context switch is understanding where to run from.
	*
	* Otherwise returns NULL.
	* This function can be thought of as a scheduler, where the interrupt handler was implemented for us.
	*
	* This is not a real time scheduler, however because the processes are predefined,
	* we'll never create a new one while running another one.
	*
	* UPDATE: check if current
	*/

	PIT->CHANNEL[0].TCTRL = 1;
	if (current_process == NULL) {
		/*If current_process is NULL it's the first time we're calling process_select*/
		if (queue_start == NULL) {
		/* The process queue is empty if the queue_start is null. */
			PIT->CHANNEL[0].TCTRL = 3;
			return NULL;
		} else {
			/*There are processes to run in the queue*/
			current_process = pop_from_start_of_linked_list();
			PIT->CHANNEL[0].TCTRL = 3;
			return current_process->sp;
		}
		//when a process tries to grab the lock but fails, its blocked variable is set to true
	} else {
	//cursp is the stack pointer of the interrupted pointer
		//if cursp is NULL: the process is finished
		if (cursp == NULL) {
		//we don't need to check if the process is blocked
			if (queue_start == NULL) {
			/* There is no other process in the queue*/
				process_stack_free((current_process)->stack_base, (current_process)->n);
				free(current_process);
				PIT->CHANNEL[0].TCTRL = 3;
				return NULL;
			} else {
			/*There are still other processes in the queue*/
				process_t * end_process = current_process; //now both variables point to the same memory address
				current_process = pop_from_start_of_linked_list(); //assign the first value in the queue to the current_process

				/* Get rid of finished process*/
				process_stack_free((end_process)->stack_base, (end_process)->n);
				free(end_process);

				PIT->CHANNEL[0].TCTRL = 3;
				return current_process->sp;
			}
			//you should only run something if queue_start->blocked =0

		} else {
		//here we check if the current process is blocked, and if it is we skip over it
		//This is not the first time you call process select and no process is done, so perform a context switch.
		process_t * running_process = current_process;

			// Don't add the process to the process queue if it is currently blocked
			if (!current_process->is_blocked){
				add_process_to_queue(running_process);
			}

			current_process = pop_from_start_of_linked_list();
			running_process->sp = cursp; // updating the stack pointer of the process to where it stopped (bc that's the value of cursp, which is set @backend)
			PIT->CHANNEL[0].TCTRL = 3;
			return current_process->sp;
		}

	}


}
