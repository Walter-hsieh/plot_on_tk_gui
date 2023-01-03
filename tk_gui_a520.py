import pandas as pd
import matplotlib.colors as mcolors

colors = mcolors.TABLEAU_COLORS
color_list = list(colors.values())


# Create dataframe in python
df = pd.read_excel("mof_granule_ads_80rh.xlsx")
colnames = df.columns
columns = len(df.columns)


# Create the GUI
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Add the charts on the GUI by using this generic template
root =tk.Tk()

figure = plt.Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(111)
for i in range(columns-1):
    label = ["extru_2mm", "mix-centri_2mm", "pan_2mm"]
    markers = ["o", "v", "s", "p", "x"]
    df_new = df[["time_min", label[i]]].dropna()
    ax.plot(df_new["time_min"], df_new[label[i]], label=label[i], color = color_list[i], marker=markers[i], linewidth=1)
    ax.set_xlabel("time_min")
    ax.set_ylabel("water uptake_wt.%")
    ax.legend(loc=7, fontsize=10)
    # ax.set_xlim([0, 120])
    ax.set_title("A520 granule produced by different methods")
    ax.text(30, 0, "measured at 80%RH/ 25°C")

scatter = FigureCanvasTkAgg(figure, root)
scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

# Create a button using destroy command to close a Tkinter window
quit_button = tk.Button(root, text='Quit', command=root.quit)
quit_button.pack()

# Create an Entry widget to accept user input
entry = tk.Entry(root)
entry.focus_set()
entry.pack()

# Create a save image function
def save_image():
    global entry
    string = entry.get()
    figure.savefig(string)

# Create a button to save the image
save_fig = tk.Button(root, text='save image', command=(lambda:save_image()))
save_fig.pack()

root.mainloop()

# Reference: How to place matplotlib charts on a Tkinter GUI
url = 'https://datatofish.com/matplotlib-charts-tkinter-gui/'