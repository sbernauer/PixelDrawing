CC ?= gcc
RM = rm -f

CCFLAGS = -Wall -D_GNU_SOURCE
ifeq ($(DEBUG),1)
	CCFLAGS += -O1 -ggdb
else
	CCFLAGS += -Ofast -march=native
endif

DEPS = sdl2 libvncserver
DEPFLAGS_CC = `pkg-config --cflags $(DEPS)`
DEPFLAGS_LD = `pkg-config --libs $(DEPS)` -lpthread -lnuma
OBJS = ring.o llist.o framebuffer.o sdl.o vnc.o network.o main.o workqueue.o frontend.o pen.o

all: pixeldrawing

%.o : %.c
	$(CC) -c $(CCFLAGS) $(DEPFLAGS_CC) $< -o $@

pixeldrawing: $(OBJS)
	$(CC) $(CCFLAGS) $^ $(DEPFLAGS_LD) -o pixeldrawing

clean:
	$(RM) $(OBJS)
	$(RM) pixeldrawing

.PHONY: all clean