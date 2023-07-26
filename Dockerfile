ARG BASE_IMAGE=ros:noetic-robot-focal

FROM ${BASE_IMAGE}

ARG SOURCE_TARGET=/opt/ros/noetic/setup.bash

# RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list
# ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -q -qq && \
    apt install -q -qq -y  -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" keyboard-configuration && \
    apt install -q -qq -y \
        python3-catkin-tools \
        git \
        ros-noetic-gazebo-ros \
        ros-noetic-control-toolbox \
        ros-noetic-gazebo-ros-control \
        ros-noetic-moveit \
        ros-noetic-ros-control \
        ros-noetic-ros-controllers \
        ros-noetic-robot-state-publisher \
        ros-noetic-rqt* && \
    apt clean && \
    rm -rf /var/lib/apt/lists/
        
RUN cd / && mkdir -p /catkin_ws/src
RUN bash -c "source ${SOURCE_TARGET} && cd /catkin_ws && catkin init"
RUN cd /catkin_ws/src && git clone https://github.com/utecrobotics/ur5 && git clone https://github.com/filesmuggler/robotiq
RUN bash -c "source ${SOURCE_TARGET} && cd /catkin_ws && catkin build"

RUN sed -i.bk 's/PositionJointInterface/hardware_interface\/PositionJointInterface/g' /catkin_ws/src/ur5/ur5_description/urdf/ur.transmission.xacro \
 && sed -i.bk 's/PositionJointInterface/hardware_interface\/PositionJointInterface/g' /catkin_ws/src/robotiq/robotiq_description/urdf/robotiq_85_gripper.transmission.xacro
RUN sed -i.bk 's/type=\"state_publisher\"/type=\"robot_state_publisher\"/g' /catkin_ws/src/ur5/ur5_description/launch/display_with_gripper.launch && \
    sed -i.bk 's/type=\"state_publisher\"/type=\"robot_state_publisher\"/g' /catkin_ws/src/ur5/ur5_description/launch/display.launch && \
    sed -i.bk 's/type=\"state_publisher\"/type=\"robot_state_publisher\"/g' /catkin_ws/src/ur5/ur5_gazebo/launch/ur5_controllers.launch
