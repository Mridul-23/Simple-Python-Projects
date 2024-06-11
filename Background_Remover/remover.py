from tkinter import *
from rembg import remove
from PIL import Image, ImageTk
from tkinter import filedialog
from ttkbootstrap import Style

root = Tk()
root.title("Image Background Remover")
root.geometry('720x720')
root.resizable(FALSE, FALSE)

ic = PhotoImage(file='robot.png')
root.iconphoto(False, ic)

style = Style(theme='darkly')
# Functions
def open_image():
    global input_path, my_img
    input_path = filedialog.askopenfilename(title="Open Image", filetype=(("PNG Files", ".png"), ("All Files", "*.*")))
    if input_path:
        # Remove the existing image label
        pic_label.pack_forget()

        # Load and display the new image
        my_img = ImageTk.PhotoImage(Image.open(input_path))
        pic_label.config(image=my_img, bg="black")
        pic_label.pack(pady=20)

def remove_thing():
	# get file path to save file
	output_path = filedialog.asksaveasfilename(title="Save As",
		filetype=(("PNG Files", '.png'), ("All Files", "*.*")))

	# get file name
	input = Image.open(input_path)
	# remove bg
	output = remove(input)
	# Save the file
	output.save(output_path, 'png')

	# Put new image on the screen
	global my_img
	my_img = ImageTk.PhotoImage(Image.open(output_path))

	# Update label
	pic_label.config(image=my_img)

def destroy():
     exit()

ff= ("Arial Black", 27)
# Gui
pic_label = Label(root, text='BACKGROUND REMOVER', font=ff)
pic_label.pack(anchor='n', fill=X, pady=20)

fr = Frame(root)
fr.pack(side=TOP, fill=X)

btnf = ("Segoe UI", 15)

open_button = Button(fr, text="Open Image",font=btnf, command=open_image)
open_button.pack(side=LEFT, padx=85, pady=10)

remove_button = Button(fr, text="Remove Background",font=btnf, command=remove_thing)
remove_button.pack(side=LEFT, padx=0, pady=10)

quit_button = Button(fr, text="QUIT",font=btnf, command=destroy)
quit_button.pack(side=LEFT, padx=85, pady=10)

root.mainloop()