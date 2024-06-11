import ttkbootstrap as tk
from tkinter import scrolledtext, filedialog, messagebox

class NotepadApp:
    def __init__(self, root):
        self.root = root

        self.fr = tk.Frame(root)
        self.fr.pack(side=tk.TOP, fill=tk.X)

        self.new_button = tk.Button(self.fr, text="New", command=self.new_file)
        self.new_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.open_button = tk.Button(self.fr, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(self.fr, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.quit_button = tk.Button(self.fr, text="Quit", command=self.destroy, bootstyle='danger')
        self.quit_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.root.title("Simple Notepad")
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')


    def new_file(self):
        self.text_area.delete(1.0, tk.END)
    
    def destroy(self):
        exit()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

if __name__ == "__main__":
    root = tk.Window("Notepad", "darkly")
    app = NotepadApp(root)
    root.mainloop()
