# code from sample code

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE = '/home/saltguy/Desktop/CS490/data/USA_Housing.xls'

# Step 1: read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows - 1)])
# Remove unneeded columns
data = np.delete(data,[0,3,4,6], axis=1)
#convert all data type to a float
data = data.astype(np.float64)



n_samples = sheet.nrows - 1

# # Step 2: create placeholders for X1 (house age), X2(number of rooms) and the Y(price)
X1 = tf.placeholder(tf.float32, name='X1')
X2 = tf.placeholder(tf.float32, name='X2')
Y1 = tf.placeholder(tf.float32, name='Y1')
Y2 = tf.placeholder(tf.float32, name='Y2')

# # Step 3: create weight and bias, initialized to 0
w1 = tf.Variable(0.0, name='weight1')
w2 = tf.Variable(0.0, name='weight2')

b1 = tf.Variable(0.0, name='bias1')
b2 = tf.Variable(0.0, name='bias2')

# # Step 4: build model to predict Y
Y_predicted1 = X1 * w1 + b1
Y_predicted2 = X2 * w2 + b2

# # Step 5: use the square error as the loss function
loss1 = tf.square(Y1 - Y_predicted1, name='loss')
loss2 = tf.square(Y2 - Y_predicted2, name='loss')

# # Step 6: using gradient descent with learning rate of 0.01 to minimize loss
optimizer1 = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss1)
optimizer2 = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss2)

with tf.Session() as sess:
    # Step 7: initialize the necessary variables, in this case, w and b
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)

    # Step 8: train the model
    for i in range(1):  # train the model 50 epochs
        total_loss1 = 0
        total_loss2 = 0
        for x1, x2, y in data:
            # Session runs train_op and fetch values of loss
            _, l1 = sess.run([optimizer1, loss1], feed_dict={X1: x1, Y1: y})
            _, l2 = sess.run([optimizer2, loss2], feed_dict={X2: x2, Y2: y})
            total_loss1 += l1
            total_loss2 += l2
        print('Epoch {0}: {1}'.format(i, total_loss1 / n_samples))
        print('Epoch {0}: {1}'.format(i, total_loss2 / n_samples))
    # close the writer when you're done using it
    writer.close()

    # Step 9: output the values of w and b
    w1, w2, b1, b2 = sess.run([w1, w2, b1, b2])

# plot the results
X1, X2, Y = data.T[0], data.T[1], data.T[2]

plt.figure()
plt.plot(X1, Y, 'bo', label='Real data')
plt.plot(X1, X1 * w1 + b1, 'r', label='Predicted data')
plt.legend()

plt.figure()
plt.plot(X2, Y, 'bo', label='Real data')
plt.plot(X2, X2 * w2 + b2, 'r', label='Predicted data')
plt.legend()
plt.show()