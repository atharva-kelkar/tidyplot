import unittest
import matplotlib
import matplotlib.pyplot as plt
from tidyplot.plotting import load_default_params, format_plot


class TestPlotting(unittest.TestCase):
    def test_format_plot_returns_ax(self):
        x = [1, 2, 3]
        y = [2, 3, 4]
        fig, ax = plt.subplots()
        ax.plot(x, y)
        kwargs = load_default_params('x_label', 'y_label')
        ax = format_plot(ax, **kwargs)
        self.assertTrue(isinstance(ax, matplotlib.axes._axes.Axes))
