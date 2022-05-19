#include "henon_w1.h"
#include "henon_w2.h"
#include "henon_b2.h"
#include "sample.h"
#include "utils.h"
#include <math.h>

int main() {
	LED_Initialize();

	int arena[15] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

	int i;
	int j;
	for (i = 0; i < 5; i++) {
		for (j = 0; j < 784; j++) {
			arena[i] = arena[i] + sample[0][j] * henon_w1_npy[i][j];
		}
	}

	LEDRed_On();

	for (i = 0; i < 10; i++) {
		for (j = 0; j < 5; j++) {
			arena[i + 5] = arena[i + 5] + arena[j] * henon_w2_npy[i][j];
		}
	}

	for (i = 0; i < 10; i++) {
		arena[i + 5] = arena[i + 5] + henon_b2_npy[i];
	}

	LEDGreen_On();

	int largest_val = 0;
	int largest_ind = 0;
	for (i = 0; i < 10; i++) {
		if(arena[i + 5] > largest_val) {
			largest_val = arena[i + 5];
			largest_ind = i;
		}
	}

	delay();
	LED_Off();
	delay();
	for(i = 0; i < largest_ind; i++) {
		if (i % 2 == 0) {
			LEDGreen_On();
		} else {
			LEDRed_On();
		}
		delay();
		LED_Off();
		delay();
	}

	return 0;

}
