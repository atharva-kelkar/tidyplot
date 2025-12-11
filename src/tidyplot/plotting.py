import matplotlib.pyplot as plt

def format_plot(
        ax: plt.axes,
        x_label: str,
        y_label: str,
        label_fontsize: int = 16,
        want_legend: int = -1,
        legend_fontsize: int = 14,
        tick_fontsize: int = 16,
        want_grid: int = -1,
        edge_linewidth: int = 2
) -> plt.axes:
    """
    Function to format plot given **kwargs
        Inputs:
            - ax: ax from "fig, ax = plt.subplots()"
            - x_label, y_label: X and Y axis labels respectively
            - label_fontsize: font size for X and Y axis labels
            - tick_fontsize: font size for ticks
            - want_legend: flag to indicate whether legend is wanted
            - legend_fontsize: font size for legend
            - want_grid: flag to indicate whether grid is wanted
            - edge_linewidth: linewidth for plot edges (also legend box edges)
    """

    ax.set_xlabel( x_label , fontsize=label_fontsize )
    ax.set_ylabel( y_label , fontsize=label_fontsize )
    ax.tick_params(axis='both', which='major', labelsize=tick_fontsize, width=edge_linewidth)
    if want_legend != -1:
        leg = ax.legend(fontsize = legend_fontsize)
        leg.get_frame().set_edgecolor('k')
        leg.get_frame().set_linewidth(edge_linewidth)
    for axis in ['top','bottom','left','right']:
      ax.spines[axis].set_linewidth(edge_linewidth)
    if want_grid != -1:
        ax.grid( linestyle = "--" )
    return ax

def load_default_params( x_label, y_label ) -> dict:
    """
    Function to load default input parameters
        Inputs:
            - x_label, y_label: X and Y axis labels respectively
    """
    kwargs = {'x_label': x_label,
              'y_label': y_label,
              'label_fontsize': 16,
              'want_legend': -1,
              'legend_fontsize': 14,
              'tick_fontsize': 16,
              'want_grid': -1
            }
    
    return kwargs
