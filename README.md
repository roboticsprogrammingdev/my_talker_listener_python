# my_talker_listener_python
This is a ROS package to demonstrate the communication of two nodes by publishing and subscribing to a topic.

This package was tested on ROS Melodic and Ubuntu 18.04 LTS.

## Installation
1. Create a catkin workspace.
```bash
~$ mkdir -p catkin_ws/src
~$ cd catkin_ws/src
~/catkin_ws/src$ catkin_init_workspace
```

2. Clone the repository.
```bash
~/catkin_ws/src$ git clone https://github.com/roboticsprogrammingdev/my_talker_listener_python.git
~/catkin_ws/src$ cd ..
```

3. Build the source and install the executables.
```bash
~/catkin_ws$ catkin_make
~/catkin_ws$ catkin_make install
```

## Demonstration
Launch the `.launch` file.
```bash
~/catkin_ws$ roslaunch my_talker_listener_python talker_listener.launch
```
![](ros-demo-launch-talker-listener.gif)

## Blog post
Read [Creating a ROS publisher and subscriber (Python)](https://blog.roboticsprogramming.dev/2020/10/creating-ros-publisher-subscriber-python.html).
