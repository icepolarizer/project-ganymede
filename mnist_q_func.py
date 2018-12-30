import numpy as np

data_file = open("data/mnist_train.csv", "r")
training_data = data_file.readlines()
data_file.close()

test_data_file = open("data/mnist_test.csv", "r")
test_data = test_data_file.readlines()
test_data_file.close()

class DeepNeuralNetwork:
    def __init__(self, input_layers, hidden_layers, output_layers):
        self.inputs = input_layers
        self.hiddens = hidden_layers
        self.outputs = output_layers
        self.test_data = None

        self.w_ih = np.random.randn(inputs, hiddens) / np.sqrt(inputs/2)
        self.w_ho = np.random.randn(hiddens, outputs) / np.sqrt(hiddens/2)

    # feed-forward를 진행한다.
    def predict(self, x):
        # 문자열을 float array로 바꾸는 과정
        data = self.normalize(np.asfarray(x.split(',')))

        # 0번은 라벨이기 때문에 날렸다.
        data = data[1:]

        layer_1 = self.sigmoid(np.dot(data, self.wih))
        output = self.sigmoid(np.dot(sigmoid_h, self.who))
        return output

    # training_data로 학습을 진행한다.
    def train(self, training_data, lr=0.01, epoch=1):
        pass

    # 현재 신경망의 정확도를 출력한다.
    def print_accuracy(self):
        matched = 0

        for x in self.test_data:
            label = int(x[0])
            predicted = np.argmax(predict(x))
                if label == predicted :
                    matched = matched + 1
        print('현재 신경망의 정확도 : {0}%'.format(matched/count(self.test_data)))

    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-x))

    def normalize(self, x):
        return (x / 255.0) * 0.99 + 0.01

network = DeepNeuralNetwork(input_layers=784, hidden_layers=100, output_layers=10)
network.test_data = test_data
network.train(training_data, lr=0.01, epoch=1)