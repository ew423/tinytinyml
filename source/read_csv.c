#include <stdio.h>
#include <errno.h>
#include <string.h>

int main() {

	char line[100];
	FILE* in_file;
	in_file = fopen("test.txt", "w");

	if (in_file == NULL) {
		fprintf(stderr, "Value of errno: %d\n", errno);
		perror("Error printed by perror");
		fprintf(stderr, "Error opening file: %s\n", strerror( errno ));
	} else {
		fprintf(in_file, "%s", "This is tutorialspoint.com");
	}

//	while ( fgets(in_file, 100, & line ) == 1 )
//	{
//	   printf("We just read %s\n", line);
//	}
	fclose(in_file);
	return 0;
}
