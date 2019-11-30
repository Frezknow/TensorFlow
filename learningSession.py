import tensorflow as tf
import numpy as np
tf.compat.v1.disable_eager_execution()
sess=tf.compat.v1.InteractiveSession()
x = tf.constant([[1.,2.]])
negMatrix = tf.negative(x)
#session = tf.compat.v1.Session()
result = negMatrix.eval()
print(result)
sess.close()

