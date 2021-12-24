# robosys_ROS
2020 robot system homework 1

---
このリポジトリは2021年度ロボットシステム学課題2で作成したROSのパッケージです。

---
## 動作環境

### OS : ubuntu 20.04.3 LTS
### ROS

---
## 環境構築

1 ROSのインストール

```sh
$ git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu18.04_desktop.git
$ cd ros_setup_scripts_Ubuntu18.04_desktop/
$ sudo apt update
$ sudo apt upgrade
$ ./locale.ja.bash
$ ./step0.bash
$ ./step1.bash
```

2 動作確認

```sh
$ cd     
$ source ~/.bashrc
$ roscore
```
Ctrl+Cでプログラムの終了

3 ワークスペースを作成し、~/.bashrcを編集

```sh
$ cd
$ mkdir -p catkin_ws/src
$ cd ~/catkin_ws/src/
$ catkin_init_workspace
$ cd ..
$ catkin_make
$ vi ~/.bashrc
source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash       #この行を追加
export ROS_MASTER_URI=http://localhost:11311
$ source ~/.bashrc
$ cd ~/catkin_ws/
$ catkin_make
```

4 本パッケージのインストール

```sh
$ cd ~/catkin_ws/src  
$ git clone  https://github.com/TonoLeo/robosys_ROS.git
$ cd ~/catkin_ws
$ catkin_make
``` 
