Title: pygame Tire Kicking
Date: 2009-07-15 22:57
Author: crossjam
Category: Uncategorized
Slug: pygame_tire_kicking
Status: published

[<img src="http://crossjam.net/mpr/media/pygame_logo_bot.png" alt="pygame_logo_bot.png" border="0" width="200" height="60" align="left" style="margin: 10px;" />][1] A while back, I used to dabble in music visualization. The kind of stuff you see in the iTunes or Winamp visualizers. At the time, I was working on Windows and really interested in writing the graphics code in Python. I actually got pretty far in putting Python inside a Winamp plug-in and using OpenGL for the graphics. Unfortunately, it wasn't really fast enough, and I had to drop the experiment as life intruded.

Since then I've been thinking about what the right combination of Python modules would be good for this sort of hacking. The key is to have good image processing facilities, fast bit blitting, and decent vector graphics support. A lot of interesting music vizzes that I've seen in the commercial music players rely on rapidly mogrifying bit images. Occasionally you want to draw some vector figures to initialize the mutating bit images. And of course it has to get to the frame buffer reasonably quickly to keep up a decent framerate.

Thinking about coming back to this arena, I wasn't aware that there were any good prepackaged solutions. Then I decided to take a look at [pygame][1]. Lo and behold pretty much everything I was looking for, including the ability to use Numpy to manipulate images as bitmap arrays and then easily blit the array to the screen.

Now that I think about it, starting with pygame you might be able to build up a more dynamically realtime [NodeBox][2] that could be competitive with [processing][3]. Sure you couldn't plop your sketches into an applet, but you'd be able to write them with Python.

[1]: http://www.pygame.org/

[2]: http://nodebox.net/code/index.php/Home

[3]: http://processing.org/

