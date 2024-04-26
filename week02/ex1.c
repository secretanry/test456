#include <stdio.h>
#include <limits.h>
#include <float.h>

int main(){
	int a1;
	unsigned short int a2;
	signed long int a3;
	float a4;
	double a5;

	a1 = INT_MAX;
	a2 = USHRT_MAX;
	a3 = LONG_MAX;
	a4 = FLT_MAX;
	a5 = DBL_MAX;

	printf("Size of integer: %lu\n", sizeof(a1));
        printf("Size of unsignedShort: %lu\n", sizeof(a2));
        printf("Size of long: %lu\n", sizeof(a3));
        printf("Size of float: %lu\n", sizeof(a4));
        printf("Size of double: %lu\n", sizeof(a5));

        printf("Value of integer: %d\n", a1);
        printf("Value of unsignedShort: %hu\n", a2);
        printf("Value of long: %ld\n", a3);
        printf("Value of float: %f\n", a4);
        printf("Value of double: %lf\n", a5);

        return 0;	
}
