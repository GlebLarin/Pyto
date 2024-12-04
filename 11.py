import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
def create_calculator_tab(notebook):
    calc_frame = ttk.Frame(notebook)
    notebook.add(calc_frame, text="Калькулятор")
    num1_label = ttk.Label(calc_frame, text="Число 1:")
    num1_entry = ttk.Entry(calc_frame)
    num2_label = ttk.Label(calc_frame, text="Число 2:")
    num2_entry = ttk.Entry(calc_frame)\
    operation_label = ttk.Label(calc_frame, text="Операция:")
    operation_var = tk.StringVar(calc_frame)
    operation_var.set("+")  
    operation_menu = ttk.OptionMenu(calc_frame, operation_var, "+", "+", "-", "*", "/")
    result_label = ttk.Label(calc_frame, text="Результат:")
    result_entry = ttk.Entry(calc_frame, state="readonly")
    def calculate():
        try:
            num1 = float(num1_entry.get())
            num2 = float(num2_entry.get())
            op = operation_var.get()
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    result = "Деление на ноль!"
                else:
                    result = num1 / num2
            else:
                result = "Ошибка операции!"
            result_entry.config(state="normal")
            result_entry.delete(0, tk.END)
            result_entry.insert(0, str(result))
            result_entry.config(state="readonly")
        except ValueError:
            result_entry.config(state="normal")
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Ошибка ввода!")
            result_entry.config(state="readonly")
    calculate_button = ttk.Button(calc_frame, text="Вычислить", command=calculate)
    num1_label.grid(row=0, column=0, sticky=tk.W)
    num1_entry.grid(row=0, column=1, sticky=tk.E+tk.W)
    num2_label.grid(row=1, column=0, sticky=tk.W)
    num2_entry.grid(row=1, column=1, sticky=tk.E+tk.W)
    operation_label.grid(row=2, column=0, sticky=tk.W)
    operation_menu.grid(row=2, column=1, sticky=tk.E+tk.W)
    result_label.grid(row=3, column=0, sticky=tk.W)
    result_entry.grid(row=3, column=1, sticky=tk.E+tk.W)
    calculate_button.grid(row=4, column=1, sticky=tk.E)
def create_checkbox_tab(notebook):
    checkbox_frame = ttk.Frame(notebook)notebook.add(checkbox_frame, text="Чекбоксы")
    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()
    check1 = ttk.Checkbutton(checkbox_frame, text="Первый", variable=var1)
    check2 = ttk.Checkbutton(checkbox_frame, text="Второй", variable=var2)
    check3 = ttk.Checkbutton(checkbox_frame, text="Третий", variable=var3)
    def show_message():
        message = ""
        if var1.get():
            message = "Вы выбрали первый вариант"
        elif var2.get():
            message = "Вы выбрали второй вариант"
        elif var3.get():
            message = "Вы выбрали третий вариант"
        else:
            message = "Вы ничего не выбрали"
        messagebox.showinfo("Выбор", message)
    button = ttk.Button(checkbox_frame, text="Показать выбор", command=show_message)
    check1.pack(pady=5)
    check2.pack(pady=5)
    check3.pack(pady=5)
    button.pack(pady=10)
def create_text_tab(notebook):
    text_frame = ttk.Frame(notebook)
    notebook.add(text_frame, text="Текст")
    text_area = tk.Text(text_frame, wrap=tk.WORD)
    text_area.pack(fill=tk.BOTH, expand=True)
    def load_text():
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    text_area.delete("1.0", tk.END)
                    text_area.insert(tk.END, file.read())
            except Exception as e:
                messagebox.showerror("Error", f"Could not load file: {e}")
    menubar = tk.Menu(text_frame)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Загрузить", command=load_text)
    menubar.add_cascade(label="Файл", menu=filemenu)
    text_frame.master.config(menu=menubar)
root = tk.Tk()
root.title("Ларин Глеб")
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)
create_calculator_tab(notebook)
create_checkbox_tab(notebook)
create_text_tab(notebook)
root.mainloop()