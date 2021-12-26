# robosys_ROS
2020 robot system homework 1

---
このリポジトリは2021年度ロボットシステム学課題2で作成したROSのパッケージです。
<br>
本パッケージは講義で作成したcount.pyとtwice.pyを参考に丁半賭博ができるパッケージです。

---
## 動作環境

### OS : ubuntu 20.04.3 LTS
### ROS

---
## 環境構築

### 本パッケージのインストール

```sh
$ cd ~/catkin_ws/src  
$ git clone  https://github.com/TonoLeo/robosys_ROS.git
$ cd ~/catkin_ws
$ catkin_make
``` 

---
## 実行方法

1 roscoreを起動する。
```sh
$ roscore &
```
（本パッケージはroscoreを起動したまま以下のプログラムを実行する。）

2 [scripts](https://github.com/TonoLeo/robosys_ROS/tree/main/scripts)にあるdealer.pyとplayer.pyを順に起動する。
```sh
$ rosrun robosys_ROS player.py
$ rosrun robosys_ROS dealer.py
```
---
## 実行結果

![image](https://user-images.githubusercontent.com/91268353/147406420-a6e333fb-2ae2-4c18-95ad-dc0e695631cd.png)

## ライセンス
[BSD 3-Clause "New" or "Revised" License](https://github.com/TonoLeo/robosys_ROS/blob/main/LICENSE)
