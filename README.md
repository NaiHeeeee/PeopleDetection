# 图像处理：人数检测

## 一·项目主要文件介绍

<img src="https://gitee.com/naihe6/people-detection/raw/master/Imags/1.png" alt="项目文件" style="zoom: 50%;" />

### 1· 文件夹Images

用于存放README图片



### 2· 文件夹detected_pictures

用于存放需要进行人数检测的图片



### 3· 文件夹facedata

用于存放训练人脸识别模型的图片数据

​	/train储存训练图片，/val储存验证图片，/test储存测试图片



​	数据集：中国科学院自动化研究所（CASIA）*[CAS-PEAL-R1 Face Database](http://www.jdl.link/peal/)*

<img src="https://gitee.com/naihe6/people-detection/raw/master/Imags/2.png" style="zoom: 67%;" />

​		*[CAS-PEAL-R1下载链接](https://pan.baidu.com/s/1trlF2Fk6-qaZLdQn1mw4Jw?pwd=969c)*



​	facedata为用于本项目中修改后的部分CAS-PEAL-R1数据集：

​		*[facedata下载链接](https://pan.baidu.com/s/1JP3Jn3HAjjjvz0X_rePLdQ?pwd=is3n)*



### 4· 文件夹trained_model

用于存放训练完成的人脸识别模型

​	*注：由于模型文件太大，故放在网盘中*

​		*[人脸识别模型](https://pan.baidu.com/s/1_bSI5qoxfSUXSnpozUnOvQ?pwd=yh8h)*



### 5· test.py

用于生成训练模型的代码

​	使用ResNet50模型进行训练



### 6· 人数检测.py

用于人数检测的主程序代码

​	识别前效果：

<img src="https://gitee.com/naihe6/people-detection/raw/master/Imags/3.png" alt="识别前" style="zoom:67%;" />

​	识别后效果：

<img src="https://gitee.com/naihe6/people-detection/raw/master/Imags/4.png" alt="识别前" style="zoom:67%;" />



