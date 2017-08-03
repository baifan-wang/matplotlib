# matplotlib_toturials
tutorials and some of my scripts for plotting, mainly used in computational chemistry filed.

## [tutorials](https://github.com/baifan-wang/matplotlib/tree/master/tutorials): introductory tutorials for matplotlib (in Chinese)

## [plot.py](https://github.com/baifan-wang/matplotlib/blob/master/plot.py): a general plot function based on matplotlib.
Usage:
```python
python plot.py -i input_data_file 
python plot.py -i input_data_file -bar               #plot bar chart
python plot.py -i input_data_file -scattor          #plot scattor
python plot.py -i input_data_file -bar  -save test.png  #save the figure to disk
```
Assuming the first row of data file contains the label for the data.    
The first column of the data file is used as x value, other columns are used y values.    
If multiple y values are present, subplots will be created.    
