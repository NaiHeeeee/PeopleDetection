# 图像处理：人数检测

## 一.项目结构

``````
Image-processing_people-detection
│
├── README.md                           # 项目说明文件
├── .gitignore                          # Git忽略文件列表
├── LICENSE                             # 许可证文件
├── train.py                            # 模型训练程序
├── 人数检测.py                          # 主程序
├── 需求分析文档.md                       # 需求分析文档
├── 软件设计文档.md                       # 软件设计文档
│
├── detected_pictures                   # 存放测试图片
│   ├── test1.jpg                       # 测试图片1
│   └── test2.jpg                       # 测试图片2
│
├── facedata                            # 存放训练数据集
│   ├── train                           # 训练集
│   ├── val                             # 验证集
│   └── test                            # 测试集
│
├── trained_model                       # 存放训练好的模型
│   └── face_detection_model.h5         # 人脸识别模型
``````

## 二·项目主要文件介绍

### 1· 文件夹detected_pictures

用于存放需要进行人数检测的图片



### 2· 文件夹facedata

用于存放训练人脸识别模型的图片数据

​	/train储存训练图片，/val储存验证图片，/test储存测试图片



​	数据集：中国科学院自动化研究所（CASIA）*[CAS-PEAL-R1 Face Database](http://www.jdl.link/peal/)*

<img src="https://raw.githubusercontent.com/NaiHeeeee/TyporaImg/main/Img/202306051133581.png" alt="2" style="zoom: 67%;" />

​		*[CAS-PEAL-R1下载链接](https://pan.baidu.com/s/1trlF2Fk6-qaZLdQn1mw4Jw?pwd=969c)*

​	facedata为用于本项目中修改后的CAS-PEAL-R1数据集：

​		*[facedata下载链接](https://pan.baidu.com/s/1JP3Jn3HAjjjvz0X_rePLdQ?pwd=is3n)*



### 3· 文件夹trained_model

用于存放训练完成的人脸识别模型

​	*注：由于模型文件太大，故放在网盘中*

​		*[人脸识别模型](https://pan.baidu.com/s/1_bSI5qoxfSUXSnpozUnOvQ?pwd=yh8h)*



### 4· train.py

用于生成训练模型的代码

​	使用ResNet50模型进行训练



### 5· 人数检测.py

用于人数检测的主程序代码

​	识别前效果：

<img src="https://raw.githubusercontent.com/NaiHeeeee/TyporaImg/main/Img/202306051133893.png" alt="3" style="zoom: 33%;" />

​	识别后效果：

<img src="https://raw.githubusercontent.com/NaiHeeeee/TyporaImg/main/Img/202306051133227.png" alt="4" style="zoom: 33%;" />







*注:本项目 README.md，软件设计文档.md，需求分析文档.md 文档中的所有图片使用Github图床链接，部分网络可能加载不出或加载较慢*
