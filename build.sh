#!/bin/bash

set -x
#docker build -t ros_ur5e .

docker build . -t repo.irsl.eiiris.tut.ac.jp/ros_ur5e:noetic \
       --build-arg BASE_IMAGE=repo.irsl.eiiris.tut.ac.jp/irsl_system:noetic \
       --build-arg SOURCE_TARGET=/choreonoid_ws/install/setup.bash
