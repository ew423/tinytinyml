#include "3140_concur.h"
#include "utils.h"
#include "lock.h"


lock_t l;

// This is the 'big' function that calls the 'small' function. It calls the 'small' function (p6) three times,
// then toggles the green light on and off.
void p5(void){
	l_lock(&l);
	LEDGreen_Toggle();
	delay();
	LEDGreen_Toggle();
	delay();
	l_unlock(&l);
}

void p6(void){
	LED_Off();
}
// This is the 'small' function called by the 'big' function. It toggles the red light on and off.

// We expect the red light to turn on and off three times, then for the green light to turn on and off
// once.
int main(void){
	LED_Initialize();           /* Initialize the LEDs           */

	l_init (&l);

	if (process_create (p6,20) < 0) {
	 	return -1;
	}

	if (process_create (p6,20) < 0) {
		return -1;
	}

	if (process_create (p6,20) < 0) {
		return -1;
	}

	if (process_create (p5,20) < 0) {
		return -1;
	}

	process_start();
	LEDGreen_On();

	while(1);
	return 0;
}
