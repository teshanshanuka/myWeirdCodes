# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""A very simple MNIST classifier.

See extensive documentation at
https://www.tensorflow.org/get_started/mnist/beginners
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

FLAGS = None


def main(_):
  # Import data
  mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

  # Create the model
  # x = tf.placeholder(tf.float32, [None, 784])
  # W = tf.Variable(tf.zeros([784, 10]))
  # b = tf.Variable(tf.zeros([10]))
  # y = tf.matmul(x, W) + b

  # Create the model TSJ
  ############################################
  n_nodes_hl1 = 500
  n_nodes_hl2 = 500
  n_nodes_hl3 = 500

  n_classes = 10
  x = tf.placeholder(tf.float32, [None, 784])

  hidden_l1 = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])),
              'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))}

  hidden_l2 = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
              'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))}

  hidden_l3 = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
              'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))}

  output_l = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
              'biases': tf.Variable(tf.random_normal([n_classes]))}

  #input data * weights + biases
  l1 = tf.matmul(x, hidden_l1['weights']) + hidden_l1['biases']
  l1 = tf.nn.relu(l1)
  # l1 = tf.nn.sigmoid(l1)

  l2 = tf.matmul(l1, hidden_l2['weights']) + hidden_l2['biases']
  l2 = tf.nn.relu(l2)
  # l2 = tf.nn.sigmoid(l2)

  l3 = tf.matmul(l2, hidden_l3['weights']) + hidden_l3['biases']
  l3 = tf.nn.relu(l3)
  # l3 = tf.nn.sigmoid(l3)

  y = tf.matmul(l3, output_l['weights']) + output_l['biases']
  ############################################

  # Define loss and optimizer
  y_ = tf.placeholder(tf.float32, [None, 10])

  # The raw formulation of cross-entropy,
  #
  #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
  #                                 reduction_indices=[1]))
  #
  # can be numerically unstable.
  #
  # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
  # outputs of 'y', and then average across the batch.
  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  # train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
  train_step = tf.train.AdamOptimizer().minimize(cross_entropy)

  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

  # Test trained mode
  sess = tf.InteractiveSession()
  tf.global_variables_initializer().run()
  # Train
  # for _ in range(1000):
  #   batch_xs, batch_ys = mnist.train.next_batch(100)
  #   sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

  #################################################
  epochs_no = 10
  batch_size = 100
  lalog = []
  for epoch in range(epochs_no):
      for _ in range(int(mnist.train.num_examples/batch_size)):
          batch_xs, batch_ys = mnist.train.next_batch(batch_size)
          l, _, a = sess.run([cross_entropy, train_step, accuracy], feed_dict={x: batch_xs, y_: batch_ys})
          lalog.append([l,a])
          # code that optimizes the weights & biases
      print('Epoch', epoch, 'of', epochs_no)
  #################################################

  print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels}))

  with open('lalog.csv','w') as f:
      for l,a in lalog:
          f.write(str(l)+','+str(a)+'\n')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
