#include <math.h>

#include "pen.h"

void movePen(struct pen* pen, int x, int y, unsigned int width, unsigned int height) {
	if (x < -1 || x > 1 || y < -1 || y > 1) {
		return;
	}
	pen->x = MAX(width - 1, MIN(0, pen->x + x));
	pen->y = MAX(height - 1, MIN(0, pen->y + y));
}
