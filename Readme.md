# ros_ur5e

## How to use
1. docker build
    ```
    bash build.sh
    ```
1. execute gazebo
    on Terminal A
    1. run docker image
        ```
        bash run.sh
        ```
    1. inside docker
        ```
        source /catkin_ws/devel/setup.bash
        roslaunch ur5_gazebo ur5_cubes.launch
        ```
    1. Run simulation (click the triangle on gazebo window)
2. execute rqt
    on Terminal B
    1. exec docker image
        ```
        bash exec.sh
        ```
    1. inside docker
        ```
        source /catkin_ws/devel/setup.bash
        rqt
        ```
    1. Select `Plugins->Robot tools->joint trajectory controller`.
    1. Set `controller manager ns` and `controller`.
    1. Click power bottom.
    1. Slide bars bottom the GUI.

## Reference
- https://demura.net/robot/athome/14710.html
- https://github.com/utecrobotics/robotiq/issues/1