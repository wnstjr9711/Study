#필요한 패키지 로드
from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

#배치사이즈, 클래스개수, 에폭 설정
batch_size = 256 #학습할 때 사용되는 데이터 수
num_classes = 10 #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
epochs = 12 #입력 데이터 학습 횟수

#이미지 크기 설정(28x28)
img_rows, img_cols = 28, 28

#train set, test set을 가져온다.
(x_train, y_train), (x_test, y_test) = mnist.load_data()


if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')
#60000개의 훈련셋과 10000개의 검증셋으로 나눈다.

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

#CNN모델 정의
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), #Conv2D(filters, kernel_size, activation, input_shape)
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2))) #MaxPooling2D(pool_size, strides)
model.add(Dropout(0.25)) #Dropout(rate)
model.add(Flatten()) #1차원으로 변환
model.add(Dense(128, activation='relu')) # Dense(unit, activation)
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy, #compile(loss, optimizer, metrics)
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

#모델 학습
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

model.save('abc.h5')
