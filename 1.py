import tensorflow as tf
import os
x=tf.random.normal((1,3))
x=x.numpy()
print(x)
x=tf.convert_to_tensor(x)
print(type(x))
x=tf.Variable([1,2,3])
print(x)
