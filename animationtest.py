import numpy as np

#%matplotlib inline
#import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
#matplotlib.rc('animation', html='html5')

import ipywidgets
from ipywidgets import interact, interactive, widgets
from IPython.display import display

#for setting the figure size
fsx, fsy = (4,3)

AnimationFigure, AnimationAxes = plt.subplots()
AnimationAxes.set_xlim(( 0, 2))
AnimationAxes.set_ylim((-2, 2))
line, = AnimationAxes.plot([], [], lw=2)
line.set_data([0,1,2,3,4],[0,2,4,6,8])
line.set_data([0,1,2,3,4],[0,-2,-4,-6,-8])

ipywidgets.HBox()

