# - import modules
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os


class IMG_Stegno:
    output_image_size = 0
    key = ""

    # main frame
    def main(self, root):
        root.title('Image Steganography by Group2')
        root.geometry('500x700')
        root.resizable(width=False, height=False)
        root.config(bg='#e3f4f1')
        frame = Frame(root)
        frame.grid()

        title = Label(frame, text='Image Steganography')
        title.config(font=('Segoe UI', 25, 'bold'))
        title.grid(pady=10)
        title.config(bg='#e3f4f1')
        title.grid(row=1, ipady=110)

        encode = Button(frame, text="Encode", command=lambda: self.encode_frame1(
            frame), padx=14, bg='#e3f4f1')
        encode.config(font=('Segoe UI', 14), bg='#e8c1c7', width=10)
        encode.grid(row=2)

        decode = Button(frame, text="Decode", command=lambda: self.decode_frame1(
            frame), padx=14, bg='#e3f4f1')
        decode.config(font=('Segoe UI', 14), bg='#e8c1c7', width=10)
        decode.grid(pady=12)
        decode.grid(row=3)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

    # back function to loop back to main frame
    def back(self, frame):
        frame.destroy()
        self.main(root)

    ###encode###
    # frame for encode page
    def encode_frame1(self, frame):
        frame.destroy()
        e_frame = Frame(root)
        label1 = Label(
            e_frame, text='Select the image in which \nyou want to hide text :')
        label1.config(font=('Segoe UI', 25, 'bold'), bg='#e3f4f1')
        label1.grid(ipady=110)

        button_bws = Button(e_frame, text='Select',
                            command=lambda: self.encode_frame2(e_frame))
        button_bws.config(font=('Segoe UI', 14), bg='#e8c1c7', width=10)
        button_bws.grid()

        button_back = Button(
            e_frame, text='Cancel', command=lambda: IMG_Stegno.back(self, e_frame))
        button_back.config(font=('Segoe UI', 14), bg='#e8c1c7', width=10)
        button_back.grid(pady=15)
        e_frame.grid()

    # function to encode image
    def encode_frame2(self, e_frame):
        e_pg = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(
            filetypes=([('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            my_img = Image.open(myfile)
            new_image = my_img.copy()
            new_image.thumbnail((200, 200))
            img = ImageTk.PhotoImage(new_image)
            label1 = Label(e_pg, text='Selected Image')
            label1.config(font=('Segoe UI', 14, 'bold'))
            label1.grid()

            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid()

            label2 = Label(e_pg, text='Enter the Hidden Key')
            label2.config(font=('Segoe UI', 14, 'bold'))
            label2.grid(pady=10)
            text_hidden_key = Text(e_pg, width=50, height=2)
            text_hidden_key.grid()

            label3 = Label(e_pg, text='Enter the Message')
            label3.config(font=('Segoe UI', 14, 'bold'))
            label3.grid(pady=10)
            text_data = Text(e_pg, width=50, height=10)
            text_data.grid()

            encode_button = Button(e_pg, text='Encode', command=lambda: [
                self.enc_fun(text_hidden_key, text_data, my_img), IMG_Stegno.back(self, e_pg)])
            encode_button.config(font=('Segoe UI', 14), bg='#e8c1c7', width=10)
            encode_button.grid(pady=10)

            back_button = Button(e_pg, text='Cancel',
                                 command=lambda: IMG_Stegno.back(self, e_pg))
            back_button.config(font=('Segoe UI', 14), bg='#e8c1c7', width=10)
            back_button.grid()

            e_pg.grid(row=1)
            e_frame.destroy()

    ###decode###
    # frame for decode page

    def decode_frame1(self, frame):
        frame.destroy()
        d_frame = Frame(root)

        label1 = Label(d_frame, text='Select image with hidden text:')
        label1.config(font=('Segoe UI', 25, 'bold'), bg='#e3f4f1')
        label1.grid(ipady=110)
        label1.config(bg='#e3f4f1')

        button_bws = Button(
            d_frame, text='Select', command=lambda: self.decode_frame2(d_frame))
        button_bws.config(font=('Segoe UI', 14), bg='#e8c1c7', width=10)
        button_bws.grid()

        button_back = Button(d_frame, text='Cancel',
                             command=lambda: IMG_Stegno.back(self, d_frame))
        button_back.config(font=('Segoe UI', 14), bg='#e8c1c7', width=10)
        button_back.grid(pady=15)
        button_back.grid()
        d_frame.grid()

    # function to decode image

    def decode_frame2(self, d_frame):
        d_pg1 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(
            filetypes=([('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.copy()
            my_image.thumbnail((200, 200))
            img = ImageTk.PhotoImage(my_image)

            label1 = Label(d_pg1, text="Selected Image")
            label1.config(font=('Segoe UI', 14, 'bold'))
            label1.grid()
            board = Label(d_pg1, image=img)
            board.image = img
            board.grid()

            label2 = Label(d_pg1, text='Enter the Hidden Key')
            label2.config(font=('Segoe UI', 14, 'bold'))
            label2.grid(pady=10)
            text_hidden_key = Text(d_pg1, width=50, height=2)
            text_hidden_key.grid()

            hidden_data = self.decode(my_img)

            decode_button = Button(d_pg1, text='Decode', command=lambda:
                                   self.check_hidden_key(d_pg1, hidden_data, text_hidden_key))
            decode_button.config(font=('Segoe UI', 14), bg='#e8c1c7', width=10)
            decode_button.grid(pady=10)

            back_button = Button(d_pg1, text='Cancel',
                                 command=lambda: IMG_Stegno.back(self, d_pg1))
            back_button.config(font=('Segoe UI', 14), bg='#e8c1c7', width=10)
            back_button.grid()

            d_pg1.grid(row=1)
            d_frame.destroy()

    def check_hidden_key(self, d_pg1, hidden_data, text_hidden_key):
        hidden_key = text_hidden_key.get("1.0", "end-1c")
        if (len(hidden_key) == 0):
            messagebox.showinfo("Alert", "Kindly enter text in textbox!")
        else:
            if ("#" in hidden_data) and ("!" in hidden_data):
                start = hidden_data.find("!")
                end = hidden_data.find("#")
                if(end > start and hidden_data[start+1:end] == hidden_key):
                    if hidden_data[end+1:] != "":
                        data = hidden_data[end+1:]
                        messagebox.showinfo(
                            "Result", "Decoding Successful\nHidden data: " + data)
                    else:
                        messagebox.showerror(
                            "Error", "No message from the selected image!")
                else:
                    messagebox.showerror("Error", "Hidden key is incorrect!")
            else:
                messagebox.showerror(
                    "Error", "No message from the selected image!")

    # function to decode data
    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''

        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'

            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data

    # function to generate data
    def generate_Data(self, data):
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data

    # function to modify the pixels of image
    def modify_Pix(self, pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            # Extracting 3 pixels at a time
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]

            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                    pix[j] -= 1

                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1

            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    # function to enter the data pixels in image
    def encode_enc(self, newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):

            # putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    # function to enter hidden text
    def enc_fun(self, text_hidden_key, text_data, myImg):
        data1 = text_hidden_key.get("1.0", "end-1c")
        data2 = text_data.get("1.0", "end-1c")
        data = "!" + data1 + "#" + data2
        if (len(data1) == 0 or len(data2) == 0):
            messagebox.showinfo("Alert", "Kindly enter text in textbox!")
        else:
            newImg = myImg.copy()
            self.encode_enc(newImg, data)
            my_file = BytesIO()
            temp = os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename(
                initialfile=temp, filetypes=([('png', '*.png')]), defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w, self.d_image_h = newImg.size
            messagebox.showinfo("Result", "Encoding Successful!")


# GUI loop
root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()
