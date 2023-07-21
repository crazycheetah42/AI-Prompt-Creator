import bardapi
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.wm_title("AI Prompt Creator")
root.geometry("1024x768")

header = tk.Label(root, text="AI Prompt Creator", font=("Helvetica", 16))
header.pack()

hint_lbl = tk.Label(root, text="Generate prompts for:")
hint_lbl.pack()

var = tk.StringVar()
entry = ttk.Entry(root, textvariable=var)
entry.pack()

def generate_prompts():
    token = 'Ywjff326_jwbSvPXTXOAsE8ooJYZQ_8Uqr9drbKg8iL4FqoFYkXqa2HRMjxcoiI7zATdzg.'
    input_var = var.get()
    input_text = "Generate good AI prompts for the following: " + input_var

    response = bardapi.core.Bard(token).get_answer(input_text)
    response_text = response['content']
    response_widget.delete(1.0, tk.END)
    response_widget.insert(1.0, response_text)

submit_btn = tk.Button(root, text="Generate", command=generate_prompts)
submit_btn.pack()

response_widget = tk.Text(root)
response_widget.pack()

info_lbl = tk.Label(root, text="Note: This is not an AI tool. It simply generates prompts to be used with AI.")
info_lbl.pack(side="bottom")

root.mainloop()
