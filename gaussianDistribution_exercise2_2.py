from math import pi
import tensorflow as tf
mean = 0.0
sigma = 1.0
x = tf.constant([[1,2]])
go = tf.exp(tf.negative(tf.pow(x - mean, 2.0) /
       (2.0 * tf.pow(sigma, 2.0)))*
	   (1.0 /(sigma * tf.sqrt(2.0 * pi))))
print(go)