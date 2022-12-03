import math

import matplotlib.pyplot as plt

from .Generaldistribution import Distribution


class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and
    visualizing a Gaussian distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        standard_deviation (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file

    """

    def __init__(self, mu=0, sigma=1):

        super().__init__(mu, sigma)

    def calculate_mean(self):

        """Function to calculate the mean of the data set.

        Args:
            None

        Returns:
            float: mean of the data set

        """
        somme = 0
        for element in self.data:
            somme += float(element)
        self.mean = somme / len(self.data)
        return self.mean

    def calculate_standard_deviation(self, sample=True):

        """Function to calculate the standard deviation of the data set.

        Args:
            sample (bool): whether the data represents a sample or population

        Returns:
            float: standard deviation of the data set

        """

        somme = 0
        for element in self.data:
            somme += pow(element - self.calculate_mean(), 2)

        if sample:
            self.standard_deviation = math.sqrt(somme / (len(self.data) - 1))
        else:
            self.standard_deviation = math.sqrt(somme / len(self.data))
        return self.standard_deviation

    def plot_histogram(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')

    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.

        Args:
            x (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        return (1.0 / (self.standard_deviation * math.sqrt(2 * math.pi))) *\
               math.exp(-0.5 * ((x - self.mean) / self.standard_deviation) ** 2)

    def plot_histogram_pdf(self, n_spaces=50):

        """Function to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            n_spaces (int): number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):

        """Function to add together two Gaussian distributions

        Args:
            other (Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian distribution

        """

        result = Gaussian()
        result.mean = self.mean + other.mean
        result.standard_deviation = math.sqrt(self.standard_deviation ** 2 +
                                              other.standard_deviation ** 2)

        return result

    def __repr__(self):

        """Function to output the characteristics of the Gaussian instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian Object

        """

        return f"mean {self.mean:.2f}, standard deviation {self.standard_deviation:.2f}"
