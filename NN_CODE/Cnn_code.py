import tensorflow as tf

print("Tensorflow version:",tf.__version__)
## 텐서플로우 라이브러리 import 후 버전확인
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test,y_test) = mnist.load_data()

x_train, x_test = x_train/ 255.0, x_test/255.0

model =  tf.keras.models.Sequential([    
])