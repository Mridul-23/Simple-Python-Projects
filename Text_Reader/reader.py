# Importing various modules, classes and finction required for our function
import ttkbootstrap as tk
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText

# Making class which is inheriting Frame from
class TextReader(tk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=15)
        self.filename = tk.StringVar()
        self.pack(fill = BOTH, expand='yes')
        self.create_elements()

    # Here we will be creating elements 
    def create_elements(self):
        style = tk.Style()
        lbl = tk.Label(self, text="TEXT READER", font=('Open sans', 30, 'bold'), anchor='n')
        lbl.pack(side=TOP, expand=YES, pady=2)
        self.textbox = ScrolledText(
            master = self,
            highlightcolor = style.colors.primary,
            highlightbackground = style.colors.border,
            highlightthickness=1
        )
        self.textbox.pack(fill=BOTH)
        default_text = "Click the browse button to open new text file."
        self.textbox.insert(END, default_text)
        
        file_entry = tk.Entry(self, textvariable=self.filename)
        file_entry.pack(side=LEFT, fill=X, expand=YES, padx=(0, 5), pady=10)

        btn = tk.Button(self, text='QUIT', command=self.quit, bootstyle = (DANGER), cursor='pirate')
        btn.pack(side=RIGHT, fill=X, pady=10, padx = (5, 0))

        btn = tk.Button(self, text='Browse', command=self.open_file, bootstyle=(PRIMARY), cursor='spraycan')
        btn.pack(side=RIGHT, fill=X, pady=10, padx = (5, 0))

    # File opening command function
    def open_file(self):
        path = askopenfilename()
        if not path:
            return
        
        with open(path, encoding='utf-8') as f:
            self.textbox.delete('1.0', END)
            self.textbox.insert(END, f.read())
            self.filename.set(path)


if __name__ == "__main__":
    app = tk.Window("Text Reader", "superhero")
    TextReader(app)
    app.mainloop()