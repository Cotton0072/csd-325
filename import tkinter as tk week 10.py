import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.tasks = []

        self.title("Cotton-ToDo")  # Title updated
        self.geometry("320x420")

        # Instruction label
        instruction = tk.Label(self, text="Right-click a task to delete it",
                               font=("Segoe UI", 10, "italic"), fg="darkred")
        instruction.pack(pady=(6, 4))

        # Canvas and scrollbar
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        # Text input
        self.text_frame = tk.Frame(self)
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Menu bar with complementary colors
        menubar = tk.Menu(self, bg="navy", fg="white")
        filemenu = tk.Menu(menubar, tearoff=0, bg="navy", fg="white")
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

        # Color schemes
        self.colour_schemes = [{"bg": "lightblue", "fg": "black"}, {"bg": "lightyellow", "fg": "black"}]

        # Bindings
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # Add default tasks
        self.add_task_text("Grade 325 Discussion Board")
        self.add_task_text("Grade 325 Tkinter program")

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()
        if task_text:
            self.add_task_text(task_text)
        self.task_create.delete(1.0, tk.END)

    def add_task_text(self, text):
        new_task = tk.Label(self.tasks_frame, text=text, pady=10)
        self.set_task_colour(len(self.tasks), new_task)
        new_task.bind("<Button-3>", self.remove_task)  # Right-click to delete
        new_task.pack(side=tk.TOP, fill=tk.X)
        self.tasks.append(new_task)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", f"Delete '{task.cget('text')}'?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, style = divmod(position, 2)
        scheme = self.colour_schemes[style]
        task.configure(bg=scheme["bg"], fg=scheme["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(-1 * (event.delta // 120), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
