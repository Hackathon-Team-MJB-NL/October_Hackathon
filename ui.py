
import tkinter as tk

def UI():
    root = tk.Tk()
    root.title("Swim Predictor")
    root.geometry("300x350")

    # Store the submitted values here
    result = {}

    def submit():
        result["name1"] = entry1.get()
        result["SE1"] = entry2.get()
        result["name2"] = entry3.get()
        result["SE2"] = entry4.get()

        # Close the window after submission
        root.destroy()

    label1 = tk.Label(root, text="1st Name:")
    label1.pack(pady=(10, 0))

    entry1 = tk.Entry(root, width=30)
    entry1.pack(pady=5)

    label2 = tk.Label(root, text="1st SE Number:")
    label2.pack(pady=(10, 0))

    entry2 = tk.Entry(root, width=30)
    entry2.pack(pady=5)

    label3 = tk.Label(root, text="2nd Name:")
    label3.pack(pady=(10, 0))

    entry3 = tk.Entry(root, width=30)
    entry3.pack(pady=5)

    label4 = tk.Label(root, text="2nd SE Number:")
    label4.pack(pady=(10, 0))

    entry4 = tk.Entry(root, width=30)
    entry4.pack(pady=5)

    btn = tk.Button(root, text="Submit", command=submit)
    btn.pack(pady=10)

    root.mainloop()

    # Return the values after the window closes
    return (
        result.get("name1", ""),
        result.get("SE1", ""),
        result.get("name2", ""),
        result.get("SE2", "")
    )
