#%%
import tensorflow as tf 



matrixA = tf.constant([[1,1],[1,1]])
matrixB = tf.constant([[1,1],[1,1]])
matrixC = tf.constant([[1,1],[1,1]])

#starts the enviroment
with tf.Session() as sess:
    #the problem is A^(2+B) * C
    
    # A^2
    step1  = tf.pow(matrixA, 2)
    #A + B
    step2 = tf.add(step1, matrixB)
    #step2 * C
    step3 = tf.matmul(step2, matrixC)
    
    #Session run is basically the same as eval execpt that run can be used 
    #on multiple tensors and eval can only be used on one tensor
   
    print("Step 1 " + str(step1.eval()))
    print("Step 2 " + str(step2.eval()))
    print("Step 3 " + str(step3.eval()))
    print(sess.run([step1,step2,step3]))
