#!/bin/bash

xhost +
docker run --rm -it \
       --env="DISPLAY" \
       --env="QT_X11_NO_MITSHM=1" \
       --env="PYTHONPATH=/choreonoid_ws/install/lib/choreonoid-1.8/python" \
       --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
       --name docker_ros_ur5e repo.irsl.eiiris.tut.ac.jp/ros_ur5e:noetic \
       -- bash
