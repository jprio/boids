# boids
Simulating Bird Flock Behavior in Python Using Boids

Craig Reynolds, introduced a system known as “boids” that could simulate something similar to birds’ flocking behavior. His model of artificial life followed three simple rules:

separation: steer to avoid crowding local flockmates
alignment: steer towards the average heading of local flockmates
cohesion: steer to move towards the average position (center of mass) of local flockmates
With only the above rules you can see emergent complexity arise out of almost nothing.

Références Python :
* https://betterprogramming.pub/boids-simulating-birds-flock-behavior-in-python-9fff99375118
    sudo apt-get install libglfw3-dev libgles2-mesa-dev
    sudo apt install fontconfig
    
* https://medium.com/@sowmyab/implementing-boids-in-python-ede6e2ad652d


* X11 Forwarding
- côté codespace :
   9  sudo apt install lixrandr
   10  sudo apt install lixrandr2
   11  sudo apt install libxrandr2
   62  sudo apt install cmake
   64  sudo apt install fontconfig
   68  apt-get install libgl1-mesa-glx
   69  sudo apt-get install libgl1-mesa-glx
   73  sudo apt install libx11
   76  sudo apt install  libx11-6 -y
   77  sudo apt install libx11-dev
   
- côté windows : 
    - setx DISPLAY "127.0.0.1:10.0"
    - gh cs ssh -- -XYvvv
- références :
    - https://babyprogrammer.com/blog/running-gui-code-applications-in-github-codespaces-on-windows/
    - https://x410.dev/cookbook/enabling-ssh-x11-forwarding-in-visual-studio-code-for-remote-development/
    - https://x410.dev/cookbook/built-in-ssh-x11-forwarding-in-powershell-or-windows-command-prompt/
    - https://yunusmuhammad007.medium.com/jetson-nano-vs-code-x11-forwarding-over-ssh-d97fd2290973


