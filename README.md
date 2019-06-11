pixeldraw
=========
A multiplayer programming game similar to pixelflut. If you don't know pixelflut, have a look here: https://cccgoe.de/wiki/Pixelflut.
**This code was mostly written by TobleMiner and was copied and adapted** from https://github.com/TobleMiner/shoreline. A huge shout-out to him to make this possible! Check him out :)

His shoreline-server is a fast server for the pixelflut game and capable up to 40Gb/s with a beefy server. He also wrote a pixelflut-client (sturmflut) that is capable of 80Gb/s. And here lies the problem: You can easily reach the limits of the server, so not the client with the best strategy, rather the client with the beefiest hardware wins. This is initially no problem, but it raises the entry-level and costs for all players. Also it isn't so easy to find hardware that is capable of running the server at this speeds.

To address this problem i came to the conclusion: At pixelflut you only "shoot" you're predefined packets (PX x y rrggbb) against the server and hope that you draw the most pixels in a certain area (at least many published clients work this way). So if we add the need to react to other players on the server you can't pre-compute your packets and blindly shoot them against the server. Also you can cooperate or fight against other players in a direct way. Let me introduce you to pixeldraw:

There are a variable number of pens on the screen, for example 5. Each has an id going from 0 to `<numer of pens - 1>` and is located at a x and y position on the screen. You can move a pen by 1 pixel and define the color of the resulting line. With this technique it is possible to draw an complete image. But if 2 ore more people are using the same pen it gets complicated... It's up to you to develop some ideas how to try to solve this problem (and maybe troll other users ;P )
If a pen reaches the end of the screen it won't get any further.

# API
All numbers are integers, no floating points.

Request                                  | Respone                        | Desciption
---------------------------------------- | ------------------------------ | -----------------------------------------------------------------------------------------
`SIZE`                                   | `<width>x<height>`             | Returns the size of the screen
`PENS`                                   | `<number of pens>`             | Returns the numbers of pens on the screen, in this example 5
`PEN <id>`                               | `<x> <y>`                      | Returns the coordinates of the regested pen.
`MOVE <id> <x> <y> <color> <feedback>`   | `[PEN <id> <x> <y>]`           | Moves the specified pen. If the flag `feedback` is set to 1, the resposnse will be the new coordinates of the pen. If the flag is 0, there will be no response.


The MOVE command: Accepts the id of the pen and the amount of pixels to move the pen in x and y-achsis. `-1 <= x <= 1 and -1 <= y <= 1` to prevent to fast movements. The color must be given in hexadecimal `rrggbb`. It returns the id and the new position of the pen. This prevents an subsequent call, because it isn't clear if the pen was moved in an other direction at the same time. Also the id is given for the case that you do movements of different pens simultaniously. Example: `MOVE 0 1 0 ff0000` to move the first pen one pixel to the right and paints a red line.

# Sample client
A basic client written in python is located under `sampleClient/drawImage.py`. Use it as following: `python3 sampleClient/drawImage.py ./Downloads/myImage.png | nc 127.0.0.1 1234`. If you want to speed up the drawing process cache the commands in a file:
- `pip3 install -r sampleClient/requirements.txt`
- `python3 sampleClient/drawImage.py ./Downloads/myImage.png > commands.txt`
- `cat commands.txt | nc 127.0.0.1`
- Perhaps store the file in a ramdisk if your working on slow HDDs.

And you're ready to go and see your - surely beautiful - image on the screen. But remember: This script doesn't use feedback provided from the server and if you share the pen with an other client it won't work very well.
So, use it just as an starting point and write in your favorite language a program that uses the feedback of the server.

**Have fun and be creative!**

# Compiling

## Dependencies

* SDL2
* libpthread
* libvncserver
* libnuma (numactl)

On \*buntu/Debian distros use `sudo apt install git build-essential libsdl2-dev libpthread-stubs0-dev libvncserver-dev libnuma-dev` to install the dependencies.

Use ```make``` to build pixeldraw


# Usage

By default pixeldraw runs in headless mode. In headless mode all user frontends are disabled. Use ```pixeldraw -f sdl``` to get a sdl window for drawing

There are a few more commandline switches:

```
-p <port>				Port to listen on (default 1234)
-b <address>				Address to listen on (default ::)
-w <width>				Width of drawing surface (default 1024)
-h <height>				Height of drawing surface (default 768)
-r <update rate>			Screen update rate in HZ (default 60)
-s <ring size>				Size of network ring buffer in bytes (default 65536)
-l <listen threads>			Number of threads used to listen for incoming connections (default 10)
-f <frontend,[option=value,...]>	Frontend to use as a display. May be specified multiple times. Use -f ? to list available frontends and options
```

## Frontend options

When specifying a frontend frontend-specific options may be passed to the frontend. For example the VNC frontend can be configured
to use a nonstandard port:

`pixeldraw -f vnc,port=2342`

All available frontends and their options can be listed using `pixeldraw -f ?`.
