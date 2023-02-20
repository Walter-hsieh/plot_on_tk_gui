import pandas as pd
import matplotlib.colors as mcolors
import os
import random

# Create the GUI
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

root =ttkb.Window(themename="cosmo")

colors = mcolors.TABLEAU_COLORS
color_list = list(colors.values())


# list the excel files on GUI
files = list(filter(lambda x: 'xlsx' in x, os.listdir()))
files_string = ', '.join(files)


# Create a entry and button to change the title for the plot
plot_title_label = ttkb.Label(root, text='Enter the title for this plot')
plot_title_label.pack(pady=5)

plot_title_inp = ttkb.Entry(root, bootstyle="primary")
plot_title_inp.pack(pady=5)

set_plot_title = ttkb.Button(root, text='Set plot title', command=(lambda: set_plot_title()), bootstyle=SUCCESS)
set_plot_title.pack(pady=5)


# create a entry to take the file name for plotting
file_inp = ttkb.Label(root, text='Choose a file to open')
file_inp.pack(pady=5)

cb = ttkb.Combobox(root, values=files)
cb.pack(pady=5)

# create a button to set chosen file name
open_file = ttkb.Button(root, text='Open file', command=(lambda : on_submit()), bootstyle=SUCCESS)
open_file.pack(pady=5)


# Create an Entry widget to accept user input
img_name_label = ttkb.Label(root, text='Enter name for saved image')
img_name_label.pack(pady=5)

img_name = ttkb.Entry(root, bootstyle="primary")
img_name.focus_set()
img_name.pack(pady=5)


# Create a button to save the image
save_fig = ttkb.Button(root, text='save image', command=(lambda:save_image()), bootstyle=SUCCESS)
save_fig.pack(pady=5)


# Create a button using destroy command to close a Tkinter window
quit_button = ttkb.Button(root, text='Close window', command=root.quit, bootstyle=SUCCESS)
quit_button.pack(pady=5)


# set action box
action_label = ttkb.Label(root, text='You will see action statement showing here when you click any button')
action_label.pack(pady=5)


# set plot title function
plot_title_default = 'This is your plot title'
def set_plot_title():
    plot_title = plot_title_inp.get()
    ax.set_title(plot_title)
    action_label.configure(text='plot title is set')

# Create a save image function
def save_image():
    global entry
    string = img_name.get()
    figure.savefig(string, dpi=1000)
    action_label.configure(text='image is saved')



# Add the charts on the GUI by using this generic template
figure = plt.Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(111)
ax.set_title(plot_title_default)
ax.set_xlabel("time_min")
ax.set_ylabel("water uptake_wt.%")
# ax.text(30, 0, "measured at 25°C")




def on_submit():

    filename = cb.get()

    # Create dataframe in python
    df = pd.read_excel(filename)
    colnames = df.columns
    columns = len(df.columns)

    for i in range(columns-1):

        label = colnames[1::]
        markers = ["o", "v", "s", "p", "x"]
        df_new = df[[colnames[0], label[i]]].dropna()
        ax.plot(df_new[df.columns[0]], df_new[label[i]], label=label[i], color = color_list[i], marker=markers[i], linewidth=1)
        ax.legend(loc=7, fontsize=10)



    scatter = FigureCanvasTkAgg(figure, root)
    scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)



root.mainloop()

# Reference: How to place matplotlib charts on a Tkinter GUI
url = 'https://datatofish.com/matplotlib-charts-tkinter-gui/'
