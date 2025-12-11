# Simple library for making plots tidy

## Example usage

```
from tidyplot.plotting import load_default_params, format_plot
x = [1, 2, 3]
y = [2, 3 4]
fig, ax = plt.subplots()

ax.plot(x, y)
ax = format_plot(ax, 'x', 'y')
```

If you want to change defaults, you can either load them using `load_default_params` and access them

```
kwargs = load_default_params('x', 'y')
print(kwargs.keys())
ax = format_plot(ax, **kwargs)
```

Or pass them directly to `format_plot`

```
ax = format_plot(ax, 'x', 'y', want_grid=1)
```
