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

# Create a entry and button to change the title for the plot
plot_title_label = tk.Label(root, text='Enter the title for this plot')
plot_title_label.pack()

plot_title_inp = tk.Entry(root)
plot_title_inp.pack()

set_plot_title = tk.Button(root, text='Set plot title', command=(lambda: set_plot_title()))
set_plot_title.pack()


# create a entry to take the file name for plotting
file_inp = tk.Label(root, text='Choose a file to open')
file_inp.pack()
chosen_file = tk.Entry(root)
chosen_file.pack()

# create a button to set chosen file name
open_file = tk.Button(root, text='Open file', command=(lambda : on_submit()))
open_file.pack()


# Create an Entry widget to accept user input
img_name_label = tk.Label(root, text='Enter name for saved image')
img_name_label.pack()

img_name = tk.Entry(root)
img_name.focus_set()
img_name.pack()


# Create a button to save the image
save_fig = tk.Button(root, text='save image', command=(lambda:save_image()))
save_fig.pack()

# create a clear the graph button
clear_button = tk.Button(root, text='Clear graph', command=(lambda:clear_graph()))
clear_button.pack()

# Create a button using destroy command to close a Tkinter window
quit_button = tk.Button(root, text='Close window', command=root.quit)
quit_button.pack()


# set action box
action_label = tk.Label(root, text='You will see action statement showing here when you click any button ')
action_label.pack()


# set plot title function
plot_title_default = 'This is your plot title'
def set_plot_title():
    plot_title = plot_title_inp.get()
    ax.set_title(plot_title)

# Create a save image function
def save_image():
    global entry
    string = img_name.get()
    figure.savefig(string)

def clear_graph():
    ax.cla()
    action_label.configure(text='graph is cleared')


# Add the charts on the GUI by using this generic template
figure = plt.Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(111)
ax.set_title(plot_title_default)
ax.set_xlabel("time_min")
ax.set_ylabel("water uptake_wt.%")
ax.text(30, 0, "measured at 80%RH/ 25°C")



def on_submit():

    filename = chosen_file.get()

    # Create dataframe in python
    df = pd.read_excel(filename)
    colnames = df.columns
    columns = len(df.columns)

    for i in range(columns-1):
        label = colnames[1::]
        markers = ["o", "v", "s", "p", "x"]
        df_new = df[["time_min", label[i]]].dropna()
        ax.plot(df_new["time_min"], df_new[label[i]], label=label[i], color = color_list[i], marker=markers[i], linewidth=1)
        ax.legend(loc=7, fontsize=10)


    scatter = FigureCanvasTkAgg(figure, root)
    scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)



root.mainloop()

# Reference: How to place matplotlib charts on a Tkinter GUI
url = 'https://datatofish.com/matplotlib-charts-tkinter-gui/'
