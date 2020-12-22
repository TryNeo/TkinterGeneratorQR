import tkinter as tk
from PIL import ImageTk
from tkinter import ttk, messagebox


class MainWindow:
    def __init__(self, root):
        root.title('Tkinter Books')
        root.geometry("900x500")
        root.resizable(0, 0)

        root.update_idletasks()
        width = root.winfo_width()
        frm_width = root.winfo_rootx() - root.winfo_x()
        win_width = width + 2 * frm_width
        height = root.winfo_height()
        titlebar_height = root.winfo_rooty() - root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = root.winfo_screenwidth() // 2 - win_width // 2
        y = root.winfo_screenheight() // 2 - win_height // 2
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        root.deiconify()
        
if __name__ == '__main__':
    main = tk.Tk()
    window = MainWindow(main)
    main.mainloop()