# UR5 for choreonoid
## ディレクトリの中身について
- ReadMe.md : このファイル
- run_ur5_robot.launch : ros_launch用
- ur5_robot_ri_sample.py : RobotInterfaceを使う場合のサンプル
- ur5_robot_robotinterface.yaml : RobotInterface用設定ファイル
- ur5_robot.body : [ur5_robot.urdf.xacro](https://github.com/utecrobotics/ur5/blob/master/ur5_description/urdf/ur5_robot.urdf.xacro)を変換したもの
- ur5_robot.cnoid : choreonoid用設定ファイル

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
        cd ur5_robot_sample
        roslaunch run_ur5_robot.launch
        ```
    1. Run simulation (click the triangle on choreonoid window)
2. execute RI sample
    on Terminal B
    1. exec docker image
        ```
        bash exec.sh
        ```
    1. inside docker
        ```
        source /catkin_ws/devel/setup.bash
        cd ur5_robot_sample
        python3 ur5_robot_ri_sample.py
        ```
## 参考：UR5のインポート方法

1. choreonoidでxacroファイルを読み込んでBodyファイルへ変換する．
    1. ```roslaunch choreonoid_ros choreonoid.launch```としてchoreonoid_rosを起動する．
    1. Itemsで'World'を選択した状態で，File -> Load -> Bodyと選択し，ファイル種類でURDFを選択し，変換したいURDFをロードする．
    1. Itemsでロボットファイルを選択した状態で，File -> Save Selected Items asを選択し，Bodyファイルとして保存する．
    1. 起動したターミナルをCtrl+cで終了する．
1. choreonoid_rosを起動して環境を作る．
    1. ```roslaunch choreonoid_ros choreonoid.launch```としてchoreonoid_rosを起動する．
    1. File -> New -> Worldと選択し Worldを作成する．
    1. Itemsで'World'を選択した状態で，File -> Load -> Bodyと選択し，作成したBodyをロードする
    1. Itemsで'World'を選択した状態で，File -> Load -> Bodyと選択し，'/choreonoid_ws/src/choreonoid/share/model/misc'にあるfloor.bodyをロードする．
    1. Itemsで'World'を選択した状態で，File -> New -> WorldROSを選択する．
    1. Itemsで'World'を選択した状態で，File -> New -> AISTSimulatorを選択する．
    1. Itemsで'AssembleRobot'(ロードしたロボット)を選択した状態で，File -> New -> BodyROSを選択する．
    1. Itemsで'AssembleRobot'(ロードしたロボット)を選択した状態で，File -> New -> ROSControlを選択する．
    1. ROSControlを選択，Propertyをクリックし，Name spaceにロボット名("ur5")を入れる．
    1. GUI左上のフロッピーディスクアイコンを押して，プロジェクトを保存する．
1. RobotInterfaceの設定ファイルを作成する．
    1. サンプルを参考に作成する．
1. launchファイルを作成する．
    1. サンプルを参考に作成する．