import tkinter as tk
from tkinter import messagebox

class ListaCumparaturiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de cumpărături")
        self.root.geometry("1000x500")

        # Liste de cumparaturi
        self.lista_food = []
        self.lista_non_food = []
        self.cost_total_food = 0
        self.cost_total_non_food = 0

        # Culori
        self.culoare_background = "#E0E0E0"
        self.culoare_text = "#000000"
        self.culoare_button = "#FF69B4"
        self.culoare_button_text = "#ffffff"
        self.culoare_contur = "#000000"

        # Fonturi
        self.font_fancy = ("Segoe Print", 8)
        self.font_bold = ("Segoe Print", 11, "bold")

        # Frame pentru introducerea produselor
        self.frame_produse = tk.Frame(root, bg=self.culoare_background, bd=5)
        self.frame_produse.place(relx=0, rely=0, relwidth=0.4, relheight=1, anchor='nw')

        # Input pentru numele produsului
        self.label_produs = tk.Label(self.frame_produse, text="Produs:", bg=self.culoare_background, fg=self.culoare_text, font=self.font_fancy)
        self.label_produs.grid(row=0, column=0, pady=10)
        self.entry_produs = tk.Entry(self.frame_produse, font=self.font_bold)
        self.entry_produs.grid(row=0, column=1, padx=10)

        # Input pentru cantitatea produsului
        self.label_cantitate = tk.Label(self.frame_produse, text="Cantitate:", bg=self.culoare_background, fg=self.culoare_text, font=self.font_fancy)
        self.label_cantitate.grid(row=1, column=0, pady=10)
        self.entry_cantitate = tk.Entry(self.frame_produse, font=self.font_bold)
        self.entry_cantitate.grid(row=1, column=1, padx=10)

        # Input pentru prețul produsului
        self.label_pret = tk.Label(self.frame_produse, text="Preț:", bg=self.culoare_background, fg=self.culoare_text, font=self.font_fancy)
        self.label_pret.grid(row=2, column=0, pady=10)
        self.entry_pret = tk.Entry(self.frame_produse, font=self.font_bold)
        self.entry_pret.grid(row=2, column=1, padx=10)

        # Categoria produsului
        self.label_categorie = tk.Label(self.frame_produse, text="Categorie:", bg=self.culoare_background, fg=self.culoare_text, font=self.font_fancy)
        self.label_categorie.grid(row=5, column=0, pady=10)
        self.var_categorie = tk.StringVar()
        self.var_categorie.set("Food")
        self.dropdown_categorie = tk.OptionMenu(self.frame_produse, self.var_categorie, "Food", "Non-food")
        self.dropdown_categorie.config(bg=self.culoare_button, fg=self.culoare_button_text, font=self.font_bold)
        self.dropdown_categorie.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        # Buton pentru adaugarea produsului în lista
        self.buton_adauga = tk.Button(self.frame_produse, text="Adaugă", command=self.adauga_produs, bg=self.culoare_button, fg=self.culoare_button_text, relief="raised", bd=3, font=self.font_bold, padx=10, pady=5, borderwidth=1, highlightthickness=0, activebackground="#5cb85c", activeforeground="#ffffff", highlightbackground=self.culoare_contur)
        self.buton_adauga.grid(row=6, columnspan=2, pady=10)

        # Frame pentru afisarea listei de cumparaturi food
        self.frame_lista_food = tk.Frame(root, bg=self.culoare_background, bd=2)
        self.frame_lista_food.place(relx=0.4, rely=0, relwidth=0.3, relheight=0.8, anchor='nw')

        # Lista de cumparaturi food
        self.lista_box_food = tk.Listbox(self.frame_lista_food, bg=self.culoare_background, fg=self.culoare_text, font=self.font_bold)
        self.lista_box_food.pack(side="left", fill="both", expand=True)

        # Scrollbar
        self.scrollbar_food = tk.Scrollbar(self.frame_lista_food, orient="vertical", command=self.lista_box_food.yview)
        self.scrollbar_food.pack(side="right", fill="y")

        self.lista_box_food.config(yscrollcommand=self.scrollbar_food.set)

        # Frame pentru afișarea listei de cumparaturi non-food
        self.frame_lista_non_food = tk.Frame(root, bg=self.culoare_background, bd=2)
        self.frame_lista_non_food.place(relx=0.7, rely=0, relwidth=0.3, relheight=0.8, anchor='nw', )

        # Lista de cumparaturi non-food
        self.lista_box_non_food = tk.Listbox(self.frame_lista_non_food, bg=self.culoare_background, fg=self.culoare_text, font=self.font_bold, )
        self.lista_box_non_food.pack(side="left", fill="both", expand=True)

        # Scrollbar
        self.scrollbar_non_food = tk.Scrollbar(self.frame_lista_non_food, orient="vertical", command=self.lista_box_non_food.yview)
        self.scrollbar_non_food.pack(side="right", fill="y")

        self.lista_box_non_food.config(yscrollcommand=self.scrollbar_non_food.set)

        # Buton pentru stergerea produsului selectat din lista de cumparaturi food
        self.buton_sterge_food = tk.Button(root, text="Șterge Food", command=self.sterge_produs_food, bg=self.culoare_button, fg=self.culoare_button_text, relief="raised", bd=3, font=self.font_bold, padx=5, pady=2, borderwidth=1, highlightthickness=0, activebackground="#d9534f", activeforeground="#ffffff", highlightbackground=self.culoare_contur)
        self.buton_sterge_food.place(relx=0.4, rely=0.9, relwidth=0.30, relheight=0.05, anchor='nw')

        # Buton pentru stergerea produsului selectat din lista de cumparaturi non-food
        self.buton_sterge_non_food = tk.Button(root, text="Șterge Non-food", command=self.sterge_produs_non_food, bg=self.culoare_button, fg=self.culoare_button_text, relief="raised", bd=3, font=self.font_bold, padx=5, pady=2, borderwidth=1, highlightthickness=0, activebackground="#d9534f", activeforeground="#ffffff", highlightbackground=self.culoare_contur)
        self.buton_sterge_non_food.place(relx=0.7, rely=0.9, relwidth=0.30, relheight=0.05, anchor='nw')

        # Buton pentru produsul cumparat food
        self.buton_cumparat_food = tk.Button(root, text="Cumpărat Food", command=self.marcaza_cumparat_food, bg=self.culoare_button, fg=self.culoare_button_text, relief="raised", bd=3, font=self.font_bold, padx=5, pady=2, borderwidth=1, highlightthickness=0, activebackground="#5bc0de", activeforeground="#ffffff", highlightbackground=self.culoare_contur)
        self.buton_cumparat_food.place(relx=0.4, rely=0.85, relwidth=0.30, relheight=0.05, anchor='nw')

        # Buton pentru produsul cumparat non-food
        self.buton_cumparat_non_food = tk.Button(root, text="Cumpărat Non-food", command=self.marcaza_cumparat_non_food, bg=self.culoare_button, fg=self.culoare_button_text, relief="raised", bd=3, font=self.font_bold, padx=5, pady=2, borderwidth=1, highlightthickness=0, activebackground="#5bc0de", activeforeground="#ffffff", highlightbackground=self.culoare_contur)
        self.buton_cumparat_non_food.place(relx=0.7, rely=0.85, relwidth=0.30, relheight=0.05, anchor='nw')

        # Buton pentru total food
        self.buton_calculeaza_food = tk.Button(root, text="Total Food", command=self.calculeaza_cost_total_food, bg=self.culoare_button, fg=self.culoare_button_text, relief="raised", bd=3, font=self.font_bold, padx=5, pady=2, borderwidth=1, highlightthickness=0, activebackground="#f0ad4e", activeforeground="#ffffff", highlightbackground=self.culoare_contur)
        self.buton_calculeaza_food.place(relx=0.4, rely=0.95, relwidth=0.30, relheight=0.05, anchor='nw')

        # Buton pentru total non-food
        self.buton_calculeaza_non_food = tk.Button(root, text="Total Non-food", command=self.calculeaza_cost_total_non_food, bg=self.culoare_button, fg=self.culoare_button_text, relief="raised", bd=3, font=self.font_bold, padx=5, pady=2, borderwidth=1, highlightthickness=0, activebackground="#f0ad4e", activeforeground="#ffffff", highlightbackground=self.culoare_contur)
        self.buton_calculeaza_non_food.place(relx=0.7, rely=0.95, relwidth=0.30, relheight=0.05, anchor='nw')

    def adauga_produs(self):
        produs = self.entry_produs.get()
        cantitate = self.entry_cantitate.get()
        pret = self.entry_pret.get()
        categorie = self.var_categorie.get()

        if not produs or not cantitate or not pret:
            messagebox.showerror("Error", "Te rog completează toate câmpurile.")
            return

        # Adaugarea produsului în lista de cumparaturi corespunzatoare
        if categorie == "Food":
            self.lista_food.append((produs, cantitate, pret))
            self.lista_box_food.insert(tk.END, f"{produs} - Cantitate: {cantitate} - Preț: {pret}")
            self.cost_total_food += float(pret)
        else:
            self.lista_non_food.append((produs, cantitate, pret))
            self.lista_box_non_food.insert(tk.END, f"{produs} - Cantitate: {cantitate} - Preț: {pret}")
            self.cost_total_non_food += float(pret)

        # Stergerea input-urilor
        self.entry_produs.delete(0, tk.END)
        self.entry_cantitate.delete(0, tk.END)
        self.entry_pret.delete(0, tk.END)

    def sterge_produs_food(self):
        # Stergerea produsului selectat din lista de cumparaturi food și din afisare
        index = self.lista_box_food.curselection()[0]
        produs_selectat = self.lista_food[index]
        self.lista_box_food.delete(index)
        del self.lista_food[index]

        # Scaderea pretului produsului sters din costul total food
        self.cost_total_food -= float(produs_selectat[2])

    def sterge_produs_non_food(self):
        # stergerea produsului selectat din lista de cumparaturi non-food si din afisare
        index = self.lista_box_non_food.curselection()[0]
        produs_selectat = self.lista_non_food[index]
        self.lista_box_non_food.delete(index)
        del self.lista_non_food[index]

        # Scaderea pretului produsului sters din costul total non-food
        self.cost_total_non_food -= float(produs_selectat[2])

    def marcaza_cumparat_food(self):
        index = self.lista_box_food.curselection()[0]
        produs_selectat = self.lista_food[index]
        produs_selectat = list(produs_selectat)
        produs_selectat.append("(Cumpărat)")
        self.lista_food[index] = tuple(produs_selectat)
        self.lista_box_food.delete(index)
        self.lista_box_food.insert(index, f"{produs_selectat[0]} - Cantitate: {produs_selectat[1]} - Preț: {produs_selectat[2]} - {produs_selectat[3]}")

    def marcaza_cumparat_non_food(self):
        index = self.lista_box_non_food.curselection()[0]
        produs_selectat = self.lista_non_food[index]
        produs_selectat = list(produs_selectat)
        produs_selectat.append("(Cumpărat)")
        self.lista_non_food[index] = tuple(produs_selectat)
        self.lista_box_non_food.delete(index)
        self.lista_box_non_food.insert(index, f"{produs_selectat[0]} - Cantitate: {produs_selectat[1]} - Preț: {produs_selectat[2]} - {produs_selectat[3]}")

    def calculeaza_cost_total_food(self):
        messagebox.showinfo("Cost Total Food", f"Costul total al cumpărăturilor food este: {self.cost_total_food}")

    def calculeaza_cost_total_non_food(self):
        messagebox.showinfo("Cost Total Non-food", f"Costul total al cumpărăturilor non-food este: {self.cost_total_non_food}")


root = tk.Tk()
app = ListaCumparaturiApp(root)
root.mainloop()

