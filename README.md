# SLAM_GMAPPING

SLAM(Simultaneous Localization and Mapping) is the computational problem of constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it.

This contains package ```openslam_gmapping``` and ```slam_gmapping``` which is a ROS2 wrapper for OpenSlam's Gmapping. Using slam_gmapping, you can create a 2-D occupancy grid map (like a building floorplan) from laser and pose data collected by a mobile robot.

## Launch:

```bash
ros2 launch slam_gmapping slam_gmapping.launch.py
```

The node slam_gmapping subscribes to sensor_msgs/LaserScan on ros2 topic ``scan``. It also expects appropriate TF to be available.

It publishes the nav_msgs/OccupancyGrid on ``map``. 

Map Meta Data and Entropy is published on ``map_metadata`` and ``entropy`` respectively.

# Added by forker 1 

Add transform nodes from odom to base_link `0 0 0 0 0 0` and from base_link to velodyne `0 0 0 0 0 0`. Run directly and get map.

Rviz2 add map and point_clouds and TF can show all we need.