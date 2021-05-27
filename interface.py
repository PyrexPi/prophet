import tkinter as tk
from pathlib import Path
from resource_path import resource_path


def get_text(root, val, name):
    # try to open the file and set the value of val to its contents
    try:
        with open(name, "r") as f:
            val.set(f.read())
        root.lift()
    except IOError as e:
        print('No sequence.txt found')
    else:
        # schedule the function to be run again after 1000 milliseconds
        root.after(200, lambda: get_text(root, val, name))


if __name__ == '__main__':
    with open('sequence.txt', "w") as f:
        f.write('Start the encounter!')

    root = tk.Tk()
    root.wm_title('Prophet visual guide')
    var = tk.StringVar()
    var.set('Start the encounter!')
    root.attributes('-topmost', True)
    l = tk.Label(root, textvariable=var)
    l.config(font=("Courier", 30))
    l.pack()
    get_text(root, var, resource_path('sequence.txt'))
    root.mainloop()

