#ifndef __SHARED_STRUCTS_H__
#define __SHARED_STRUCTS_H__
#include <stdbool.h>

/** Implement your structs here */

/**
 * This structure holds the process structure information
 */
typedef struct process_state {
	/* Built as a LinkedList */


	unsigned int * sp;
	/* the stack pointer for the process */

	unsigned int * stack_base; //stack base: to deallocate memory they gave us the process_stack free function, takes the initial size of the process and the size of the stack.
	/* the base of the process stack */

	int n;
	/* stack size passed into stack init */
	
	bool is_blocked;
	/* lock needed, if any */

	process_t *next;
	/*next process state */
} process_t;

/**
 * This defines the lock structure
 */
typedef struct lock_state {

	process_t * queue; // linked list of processes waiting for this lock

	bool locked; // the status of the lock (can it be accessed or not)

} lock_t;

/**
 * This defines the conditional variable structure
 */
typedef struct cond_var {

} cond_t;

// Declare these two variables here as global variables. We would like to access them in both
// process.c and lock.c.
extern process_t * current_process;
extern process_t * queue_start;

#endif
