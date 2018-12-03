# -*- coding: utf-8 -*-
import tensorflow as tf
import scipy.misc
import os
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x=tf.placeholder(tf.float32,[None,784])
W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
Y=tf.nn.softmax(tf.matmul(x,W)+b)
Y_=tf.placeholder(tf.float32,[None,10])
cross_entropy= \
    tf.reduce_mean(-tf.reduce_sum(Y_ * tf.log(Y)))

train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

sess=tf.InteractiveSession()
tf.global_variables_initializer().run()

for _ in range(1000):
    batch_xs,batch_ys=mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={x:batch_xs,Y_:batch_ys})

correct_prediction=tf.equal(tf.argmax(Y,1),tf.argmax(Y_,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print(sess.run(accuracy,feed_dict={x:mnist.test.images,Y_:mnist.test.labels}))





