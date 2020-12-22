import tkinter as tk
import qrcode 
from datetime import datetime
from PIL import ImageTk
from tkinter import ttk, messagebox

class MainWindow:
    def __init__(self, root):
        root.title('Tkinter | Generador QR')
        root.geometry("600x600")
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
        
        self.main(root)
        
    def main(self,root):
        self.input = tk.StringVar()
        self.format = tk.StringVar()
        self.format_data = ("jpg","png","svg")
        self.format_cb = ttk.Combobox(root, values=self.format_data,width=4,state="readonly")
        self.format_cb.place(x=330,y=80)
        
        label_tittle = tk.Label(root,text="Generador | QR",font=("Roboto", 15)).place(x=220,y=20)
        label_format_cb = tk.Label(root,text="Formato:",font=("Roboto", 12)).place(x=250,y=80)
        label_input = tk.Label(root, text="ingrese:", font=("Roboto", 12)).place(x=15, y=80)
        entry_input = tk.Entry(root, width=20, textvariable=self.input).place(x=80, y=80)
        button_generator = tk.Button(root, text="Generar", font=("Roboto", 12), command=lambda : self.generator_qr(root)).place(x=420, y=73)

        
    def generator_qr(self,root):
        
        input = self.input.get()
        format_cb = self.format_cb.get()

        if input == "" or format_cb == "":
            messagebox.showerror("Error", 'Ingrese valores o elija un formato')
        else:
            fecha = datetime.now().strftime('%d_%m_%Y_%H_%S')
            qr = qrcode.QRCode(
                version = 1,
                error_correction = qrcode.constants.ERROR_CORRECT_H,
                box_size = 10,
                border = 2
            )
            info_qr = input
            qr.add_data(info_qr)
            qr.make(fit=True)
            image_name_qr = 'image_qr/codigo_qr_'+fecha+"."+format_cb
            image_qr = qr.make_image()
            image_qr.save(image_name_qr)
            messagebox.showinfo(title="QR Generado", message='Generado exitosamente')
            self.open_image_qr(root,image_name_qr)
        
        
    def open_image_qr(self,root,path):
        img = ImageTk.PhotoImage(file=path)
        open_qr = tk.Label(root, image=img)
        open_qr.image = img
        open_qr.place(x=100,y=150)

if __name__ == '__main__':
    main = tk.Tk()
    window = MainWindow(main)
    main.mainloop()