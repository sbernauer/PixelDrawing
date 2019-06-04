#include <math.h>

#include "pen.h"

// Doesnt check, that -1 <= x <= 1, nether for y. This is skipped for better performance.
// It is already done by net_str_to_uint32_16 in network.c.
void move_pen(struct pen* pen, int x, int y, unsigned int width, unsigned int height) {
	pen->x = MAX(MIN(pen->x + x, width - 1), 0);
	pen->y = MAX(MIN(pen->y + y, height - 1), 0);
}
