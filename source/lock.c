#include "3140_concur.h"
#include "lock.h"
#include "shared_structs.h"

/* Retrieves the next node in a process_t linkedlist. Helper Function. */
process_t * get_next_node (process_t * process) {
	return process->next;
}

/* Adds a new process to the lock's queue. Copied from process.c. */
void add_process_to_lock_queue(lock_t* l, process_t * new_pointer) {
	if (l->queue == NULL) {
		l->queue = new_pointer;
	} else {
		process_t * tmp;
		tmp = l->queue;
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

/* Retrieves the first item from the queue of processes waiting for this lock. */
process_t * pop_process_from_lock_queue(lock_t* l) {
	if (l->queue == NULL) {
		return NULL; // can't pop something from nothing
	} else { // there's at least one process waiting in line

		process_t * next_process = l->queue;
		l->queue = get_next_node(l->queue);
		/* Retrieve the head of the list and move the queue forward. */

		next_process->next = NULL;
		return next_process;
		/* Return the head of the queue. */
	}
}

/* Initializes lock object as free with no processes in line to use it. */
void l_init(lock_t* l) {
	l->locked = false;
	l->queue = NULL;
	/* Initialize queue to be empty and leave lock open */
}

/* If the lock is in use, queues the process up to use the lock when it is free.
 * Otherwise, closes the lock while the current process is executing. */
void l_lock(lock_t* l) {
	PIT->CHANNEL[0].TCTRL = 1;
	if (l->locked) { // if lock is occuptied
		current_process->is_blocked = true;
		/* mark current process as blocked */

		add_process_to_lock_queue(l, current_process);
		/* add process to lock queue */

		process_blocked();
	} else { // lock is not occupied
		l->locked = true;
		/* lock is now occupied */
	}
	PIT->CHANNEL[0].TCTRL = 3;
}

/* Opens the lock for use by anyone who may need it. */
void l_unlock(lock_t * l) {
	PIT->CHANNEL[0].TCTRL = 1;
	l->locked = false;
	/* lock is not occupied */
	if (l->queue != NULL) { // if there is someone in line to use the lock

		process_t * next_process = l->queue;
		/* retrieve the next person in line to use lock */

		l->queue = next_process->next;
		/* remove head from lock queue */

		next_process->is_blocked = false;
		next_process->next = queue_start;
		queue_start = next_process;
		/* fast track this process to the front of the process queue */
	}
	PIT->CHANNEL[0].TCTRL = 3;
}
