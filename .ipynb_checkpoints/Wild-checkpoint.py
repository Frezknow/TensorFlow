{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " Import tensorflow and start an interactive session"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "tf.compat.v1.disable_eager_execution()\n",
    "sess=tf.compat.v1.InteractiveSession()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Build a computation graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "matrix = tf.constant([[1.,2.]])\n",
    "negMatrix = tf.negative(matrix)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Evaluate the graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-1. -2.]]\n"
     ]
    }
   ],
   "source": [
    "result = negMatrix.eval()\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
