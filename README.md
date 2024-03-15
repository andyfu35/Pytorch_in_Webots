# About
I'm making a project about how to use Ros2 in Webots with python. I want to record it because of my poor memory.


# Getting started
    
## 1.Build a Ros2 workspace & package
```
mkdir /ros2_ws/src
cd /ros2_ws        
source /opt/ros/foxy/setup.bash        
colcon build  
```
Create Ros2 package. `my_package` & `my_robot_driver` can change current name
```
source install/setup.bash
cd /src
ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name my_robot_driver my_package --dependencies rclpy geometry_msgs webots_ros2_driver
```
Let's add a `launch` & a `worlds` folder
```
cd my_package
mkdir launch
mkdir worlds
```
## 2.Setup the simulation world        
Download this file [world](https://docs.ros.org/en/foxy/_downloads/5ad123fc6a8f1ea79553d5039728084a/my_world.wbt), then put it inside `worlds` folder

