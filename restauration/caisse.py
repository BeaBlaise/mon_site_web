import tkinter as tk
from tkinter import messagebox

class CaisseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Logiciel de caisse simple")

        self.label = tk.Label(root, text="Montant:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Ajouter au total", command=self.ajouter)
        self.button.pack()

        self.total = 0
        self.total_label = tk.Label(root, text=f"Total: {self.total} €")
        self.total_label.pack()

    def ajouter(self):
        try:
            montant = float(self.entry.get())
            self.total += montant
            self.total_label.config(text=f"Total: {self.total} €")
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaisseApp(root)
    root.mainloop()
