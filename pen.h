#ifndef _PEN_H_
#define _PEN_H_

#include <stdint.h>

#define COUNT_PENS 10

#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

struct pen {
	unsigned int x;
	unsigned int y;
};

// Functions
void move_pen(struct pen* pen, int x, int y, unsigned int width, unsigned int height);

#endif
