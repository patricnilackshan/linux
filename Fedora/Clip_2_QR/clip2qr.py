#!/home/patricnilackshan/miniconda3/bin/python
import qrcode
import tkinter as tk
import pyperclip as pc

def main():
    info = pc.paste()
    window = tk.Tk()

    qr_code_filename = "clip2qr.png"
    qr_code = qrcode.make(info)
    qr_code.save(qr_code_filename)
    window.title("Clip2QR")
    image = tk.PhotoImage(file=qr_code_filename)
    image_label = tk.Label(window, image=image)
    image_label.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
