import pandas as pd
import matplotlib.colors as mcolors
import os

# Create the GUI
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root =tk.Tk()

colors = mcolors.TABLEAU_COLORS
color_list = list(colors.values())


# list the excel files on GUI
files = list(filter(lambda x: 'xlsx' in x, os.listdir()))
files_string = ', '.join(files)

files_label = tk.Label(root, text=files_string)
files_label.pack()

# create a entry to take the file name for plotting
chosen_file = tk.Entry(root)
chosen_file.pack()

# create a button to set chosen file name

open_file = tk.Button(root, text='open file', command=(lambda : on_submit()))
open_file.pack()


# Create an Entry widget to accept user input
img_name = tk.Entry(root)
img_name.focus_set()
img_name.pack()


def on_submit():
    filename = chosen_file.get()   

    # Create dataframe in python
    df = pd.read_excel(filename)
    colnames = df.columns
    columns = len(df.columns)


    # Add the charts on the GUI by using this generic template
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    ax = figure.add_subplot(111)
    for i in range(columns-1):
        label = colnames[1::]
        markers = ["o", "v", "s", "p", "x"]
        df_new = df[["time_min", label[i]]].dropna()
        ax.plot(df_new["time_min"], df_new[label[i]], label=label[i], color = color_list[i], marker=markers[i], linewidth=1)
        ax.set_xlabel("time_min")
        ax.set_ylabel("water uptake_wt.%")
        ax.legend(loc=7, fontsize=10)
        ax.set_title("A520 granule produced by different methods")
        ax.text(30, 0, "measured at 80%RH/ 25°C")

    scatter = FigureCanvasTkAgg(figure, root)
    scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    # Create a button using destroy command to close a Tkinter window
    quit_button = tk.Button(root, text='Quit', command=root.quit)
    quit_button.pack()

    # Create a save image function
    def save_image():
        global entry
        string = img_name.get()
        figure.savefig(string)

    # Create a button to save the image
    save_fig = tk.Button(root, text='save image', command=(lambda:save_image()))
    save_fig.pack()

root.mainloop()

# Reference: How to place matplotlib charts on a Tkinter GUI
url = 'https://datatofish.com/matplotlib-charts-tkinter-gui/'
