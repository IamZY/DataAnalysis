import numpy as np
from utils.features.prepare_for_training import prepare_for_training


class LinearRegression:

    def __init__(self, data, labels, polynomial_degree=0, sinusoid_degree=0, normalize_data=True):
        """
        对数据预处理
        先得到所有的特征个数
        初始化参数矩阵
        """
        (data_processed,  # 预处理后的数据
         features_mean,
         features_deviation) = prepare_for_training(data, polynomial_degree, sinusoid_degree, normalize_data = True)
        self.data = data_processed
        self.labels = labels
        self.data_processed = data_processed
        self.features_mean = features_mean
        self.features_deviation = features_deviation
        self.polynomial_degree = polynomial_degree
        self.sinusoid_degree = sinusoid_degree
        self.normalize_data = normalize_data

        num_features = self.data.shape[1]  # data的列数 就是代表特征个数
        self.theta = np.zeros((num_features, 1))

    def train(self, alpha, num_iterations=500):
        """
        训练模块 执行梯度下降
        :param alpha:
        :param num_iterations:
        :return:
        """
        cost_history = self.gradient_descent(alpha, num_iterations)
        return self.theta, cost_history

    def gradient_descent(self, alpha, num_iterations):
        """
        实际迭代模块
        :param alpha:
        :param num_iterations:
        :return:
        """
        cost_history = []
        for _ in range(num_iterations):
            self.gradient_step(alpha)
            cost_history.append(self.cost_function(self.data, self.labels))
        return cost_history

    def gradient_step(self, alpha):
        """
        梯度下降 参数更新计算方法 矩阵计算
        :param alpha:
        :return:
        """
        num_examples = self.data.shape[0]
        prediction = LinearRegression.hypothesis(self.data, self.theta)
        delta = prediction - self.labels
        theta = self.theta
        theta = theta - alpha * (1 / num_examples) * (np.dot(delta.T, self.data)).T
        self.theta = theta

    def cost_function(self, data, labels):
        num_examples = data.shape[0]
        delta = LinearRegression.hypothesis(self.data, self.theta) - labels
        cost = (1 / 2) * np.dot(delta.T, delta) / num_examples
        return cost[0][0]

    @staticmethod
    def hypothesis(data, theta):
        prediction = np.dot(data, theta)
        return prediction

    def get_cost(self, data, labels):
        """
        损失计算方法
        :param data:
        :param labels:
        :return:
        """
        data_processed = prepare_for_training(data,  # 预处理后的数据
                                              self.polynomial_degree,
                                              self.sinusoid_degree,
                                              self.normalize_data
                                              )[0]

        return self.cost_function(data_processed, self.labels)

    def predict(self, data):
        """
        用训练好的参数模型 得到回归预测结果
        :param data:
        :return:
        """
        data_processed = prepare_for_training(data,  # 预处理后的数据
                                              self.polynomial_degree,
                                              self.sinusoid_degree,
                                              self.normalize_data
                                              )[0]
        predictions = LinearRegression.hypothesis(data_processed, self.theta)

        return predictions
