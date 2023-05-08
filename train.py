import os
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Flatten, Dense, Dropout
from keras.models import Model
from keras.optimizers import Adam
from keras.applications import ResNet50


def train():
    # 设置训练集和测试集的图像尺寸
    img_width, img_height = 224, 224

    # 设置批次大小和训练迭代次数
    batch_size = 32
    epochs = 100

    # 设置训练集和验证集的路径
    file_dir = os.path.dirname(__file__)
    train_data_dir = os.path.join(file_dir, 'face_pictures/train_pictures/')
    val_data_dir = os.path.join(file_dir, 'face_pictures/val_pictures/')

    # 使用ResNet50模型，去掉最后一层，并添加一个全连接层，作为新的输出层
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))
    x = base_model.output
    x = Flatten()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions = Dense(1, activation='sigmoid')(x)
    model = Model(inputs=base_model.input, outputs=predictions)

    # 冻结ResNet50模型中的卷积层
    for layer in base_model.layers:
        layer.trainable = False

    # 编译模型
    model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

    # 数据增强器
    train_datagen = ImageDataGenerator(rescale=1. / 255,
                                       shear_range=0.2,
                                       zoom_range=0.2,
                                       horizontal_flip=True)

    # 加载训练集和验证集图像数据并进行数据增强
    train_generator = train_datagen.flow_from_directory(
        os.path.join(train_data_dir, 'Images'),
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='binary',
        color_mode='rgb')

    val_generator = train_datagen.flow_from_directory(
        val_data_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='binary',
        color_mode='rgb')

    # 训练模型
    model.fit(train_generator,
              steps_per_epoch=len(train_generator),
              epochs=epochs,
              validation_data=val_generator,
              validation_steps=len(val_generator))

    # 保存模型
    model.save(os.path.join(file_dir, 'trained_model/face_detection_model.h5'))
    print('[INFO] Model saved.')


if __name__ == "__main__":
    train()
