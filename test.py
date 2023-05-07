import os
import cv2
import numpy as np
from keras.models import load_model


def test():
    # 加载人脸检测模型
    face_detection_model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 加载人脸识别模型
    face_recognition_model = load_model('model/face_detection_model.h5')

    # 获取test文件夹下所有文件的文件名列表
    img_paths = os.listdir('test_jpg')

    # 遍历每张图片
    for img_path in img_paths:
        # 加载图片
        img = cv2.imread(os.path.join('test_jpg', img_path))

        # 检测人脸
        faces = face_detection_model.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

        # 统计人脸数
        count = len(faces)

        # 在原图片左上角添加红色数字显示人脸数
        cv2.putText(img, f"{count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # 遍历每张人脸
        for (x, y, w, h) in faces:
            # 提取人脸部分图片
            face = img[y:y + h, x:x + w]

            # 预处理图片
            face = cv2.resize(face, (224, 224))
            face = face.astype('float32') / 255.0
            face = np.expand_dims(face, axis=0)

            # 使用模型预测人脸数量
            count = int(face_recognition_model.predict(face)[0][0])

            # 在人脸部分画框和添加数字
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 显示图片
        cv2.imshow('Image', img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    test()
