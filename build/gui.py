from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from btmain import Btmain as bt
from pytmain import Pytmain as pyt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)


def plot_btmain():
    """
    Embeds the Backtrader plot from btmain into the tKinter window. Master canvas
    is btmain_canvas. Size and dpi are specific for formatting.  
    
    """
    fig = b.get_plot()
    fig.set_size_inches(13, 5)
    fig.set_dpi(74.5)
    graph = FigureCanvasTkAgg(fig, master = btmain_canvas) 
    graph.draw()
    graph.get_tk_widget().pack()


def plot_pytrends():
    """
    Embeds the pytrends plot from pyt into the tKinter window. Master canvas
    is pytrends_canvas. Size and dpi are specific for formatting. 

    """

    p = pyt()
    
    data = p.get_data("bitcoin")
    
    y = data["bitcoin"].values
    
    # TODO: add actual dates instead of 0-whatever
    x = data.index
        
    fig = Figure()
    fig.set_size_inches(13, 2)
    fig.set_dpi(74.6)
    fig.add_subplot(111, title=f"Bitcoin: Interest Over Time").plot(x, y)
        
    canvas = FigureCanvasTkAgg(fig, master=pytrends_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack()

#window is initialized
window = Tk()
window.geometry("1000x700")
window.configure(bg = "#373737")


# btmain is initialized
b = bt()

#root canvas for the gui
main_canvas = Canvas(
    window,
    bg = "#e6e6e6",
    height = 700,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
main_canvas.place(x = 0, y = 0)

# bitmain layout marker
main_canvas.create_rectangle(
    15.0,
    13.0,
    985.0,
    412.0,
    fill="#FFFFFF",
    outline="")
# bitmain canvas
btmain_canvas = Canvas(
    main_canvas,
    bg = "#FFFFFF",
    height = 480,
    width = 970,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
btmain_canvas.place(x=15, y=13)


# pytrends layout marker
main_canvas.create_rectangle(
    15.0,
    504.0,
    985.0,
    604.0,
    fill="#FFFFFF",
    outline="")
# pytrends canvas
pytrends_canvas = Canvas(
    main_canvas,
    bg = "#FFFFFF",
    height = 150,
    width = 970,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
pytrends_canvas.place(x=15, y=430)

# Bottom text banner
main_canvas.create_rectangle(
    15.0,
    611.0,
    986.0,
    689.0,
    fill="#abc8e0",
    outline="")

#Starting portfolio value label
main_canvas.create_text(
    22.0,
    611.0,
    anchor="nw",
    text="Starting portfolio value:",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

#Ending portfolio value label
main_canvas.create_text(
    22.0,
    651.0,
    anchor="nw",
    text="Ending portfolio value:",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

#Starting portfolio value, called after btmain is initialized but before cerebro is run
main_canvas.create_text(
    292.0,
    611.0,
    anchor="nw",
    text=b.get_starting_value(),
    fill="#000000",
    font=("Roboto", 24 * -1)
)


# Calls the graphing functions
# Pytrends has to be called first otherwise it doesn't plot for some reason
plot_pytrends()
plot_btmain()

# Ending portfolio value, called after cerebro is run else returns starting value
main_canvas.create_text(
    292.0,
    651.0,
    anchor="nw",
    text=b.get_ending_value(),
    fill="#000000",
    font=("Roboto", 24 * -1)
)

# run gui after everything is finished
window.resizable(False, False)
window.mainloop()
