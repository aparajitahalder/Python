import tensorflow as tf
t1=tf.constant(3.0)
t2=tf.constant(3.0)
sess=tf.Session()
print(sess.run([t1,t2]))
