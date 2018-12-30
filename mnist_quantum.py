import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
from momment import xavier


class NN:
    def __init__(self):
        self.W1 = np.random.uniform(low=-0.01, high=0.01, size=(784, 100))
        self.W2 = np.random.uniform(low=-0.01, high=0.01, size=(100, 10))
        self.learningRate = 0.001

    def sigmoid(self, x):
        # return 1.0 / (1.0 + np.exp(-x))
        return xavier(x)

    def dsigmoid(self, x):
        return x * (1. - x)


    def softmax(self, x):
        if x.ndim == 1:
            x = x.reshape([1, x.size])
        modifiedX = x - np.max(x, 1).reshape([x.shape[0], 1]);
        sigmoid = np.exp(modifiedX)
        return sigmoid / np.sum(sigmoid, axis=1).reshape([sigmoid.shape[0], 1]);

    def getCrossEntropy(self, predictY, labelY):
        return np.mean(-np.sum(labelY * np.log(self.softmax(predictY)), axis=1))

    def feedForward(self, x):
        y1 = np.dot(x, self.W1)
        sigmoidY1 = self.sigmoid(y1)

        y2 = np.dot(sigmoidY1, self.W2)
        softmaxY2 = self.softmax(y2)

        return sigmoidY1, softmaxY2

    def backpropagation(self, x, labelY, predictY1, predictY2):
        error = predictY2 - labelY

        dY2 = np.matmul(error, self.W2.T)
        dY1 = self.dsigmoid(predictY1)

        dW1 = x.T.dot(dY2 * dY1)

        dW2 = predictY1.T.dot(error)

        return dW1, dW2

    def update(self, dW1, dW2):
        self.W1 -= self.learningRate * dW1
        self.W2 -= self.learningRate * dW2


if __name__ == '__main__':

    mnist = input_data.read_data_sets('/tmp/tensorflow/mnist/input_data', one_hot=True)

    np.random.seed(777)

    NN = NN()

    for _ in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        y1, y2 = NN.feedForward(batch_xs)
        dW1, dW2 = NN.backpropagation(batch_xs, batch_ys, y1, y2)
        NN.update(dW1, dW2)

    y1, y2 = NN.feedForward(mnist.test.images)
    correct_prediction = np.equal(np.argmax(y2, 1), np.argmax(mnist.test.labels, 1))
    accuracy = np.mean(correct_prediction)
    print(accuracy)


