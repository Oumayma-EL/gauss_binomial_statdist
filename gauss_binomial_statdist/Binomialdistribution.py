import math

import matplotlib.pyplot as plt

from .Generaldistribution import Distribution


class Binomial(Distribution):
    def __init__(self, probability=1.0, size_population=100):
        """

        :param probability: is probability of success in a single trial
        :type probability: float
        :param size_population: is the number of trials (occurrences)
        :type size_population: int
        """
        super().__init__()
        self.p = probability
        self.n = size_population

    def calculate_mean(self):
        """

        :return: The mean of the binomial distribution which is np
        :rtype: float
        """
        self.mean = self.p * self.n
        return self.mean

    def calculate_standard_deviation(self):
        """

        :return: The mean of the binomial distribution which is sqrt(np(1-p))
        :rtype: float
        """
        self.standard_deviation = math.sqrt(self.n * self.p * (1 - self.p))
        return self.standard_deviation

    def replace_stats_with_data(self):

        """ Function to calculate p and n from the data set

                Args:
                    None

                Returns:
                    float: the p value
                    float: the n value

                """


        if len(self.data) != 0:
            count = {}
            for number in self.data:
                count[number] = count.get(number, 0) + 1
                # print(type(number))
            # print(count)
            # print(count.get(1))
            self.n = count.get(0) + count.get(1)
            self.p = int(count.get(1)) / self.n
            self.mean = self.calculate_mean()
            self.standard_deviation = self.calculate_standard_deviation()
        else:
            self.mean = self.calculate_mean()
            self.standard_deviation = self.calculate_standard_deviation()

        return self.p, self.n

    def plot_bar(self):
        """
        :return: The histogram plotted
        :rtype:None
        """
        plt.bar(x=['0', '1'], height=[(1 - self.p) * self.n, self.p * self.n])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')

    def pdf(self, k: int):
        """
        Probability density function calculator for the binomial distribution.


        :param k: point for calculating the probability density function
        :type k: int
        :return: probability density function output
        :rtype: float
        """
        return pow(self.p, k) * pow(1 - self.p, self.n - k) * (
                math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n - k)))

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the probability density function plot
            list: y values for the probability density function plot

        """
        x = []
        y = []

        # calculate the x values to visualize
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()

        return x, y

    def __add__(self, other):
        """

        :param other: Represents the second distribution to be added
        :type other: Binomial
        :return: The binomial distribution as a result of 2 binomial distributions
        :rtype:Binomial
        """

        try:
            assert self.p == other.p, 'p values are not equal'
            result = Binomial()
            result.p = other.p
            result.n = self.n + other.n
            result.mean = self.calculate_mean()
            result.standard_deviation = self.calculate_standard_deviation()

        except AssertionError as error:
            raise error
        return result

    def __repr__(self):
        """
        :return: The characteristics of the Binomial object
        :rtype: str
        """
        return f"mean {self.mean:.2f}, standard deviation {self.standard_deviation:.2f}, p {self.p:.2f}, n {self.n}"
