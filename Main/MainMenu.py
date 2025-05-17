import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

class Master(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestor Financeiro - LFA")
        self.geometry("1100x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Registrar fonte Azonix
        azonix_path = r"C:\Users\lucas\Desktop\Projetos\Gestor-Financeiro\Font\Azonix.ttf"
        self.tk.call('font', 'create', 'Azonix', '-family', 'Azonix', '-size', 22, '-weight', 'bold')
        tkfont.Font(family="Azonix", size=22, weight="bold")  # Garante registro

        # Frame do topo
        self.top_frame = ctk.CTkFrame(self, fg_color="transparent", height=60)
        self.top_frame.pack(fill="x", side="top")

        # LFA à esquerda com Azonix
        self.lfa_label = ctk.CTkLabel(
            self.top_frame,
            text="LFA",
            font=("Azonix", 22, "bold")
        )
        self.lfa_label.place(relx=0.01, rely=0.5, anchor="w")

        # Título centralizado com Azonix
        self.title_label = ctk.CTkLabel(
            self.top_frame,
            text="Gestor Financeiro",
            font=("Azonix", 24, "bold")
        )
        self.title_label.place(relx=0.5, rely=0.5, anchor="center")

        # Logo à direita (aumentado)
        logo_path = r"C:\Users\lucas\Desktop\Projetos\Gestor-Financeiro\Images\Logo.png"
        logo_img = Image.open(logo_path)
        logo_ctk = ctk.CTkImage(light_image=logo_img, dark_image=logo_img, size=(80, 80))
        self.logo_label = ctk.CTkLabel(self.top_frame, text="", image=logo_ctk)
        self.logo_label.place(relx=0.98, rely=0.5, anchor="e")

        # Container principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=(10, 20))

        # Year Selector
        self.year_frame = ctk.CTkFrame(self.main_frame)
        self.year_frame.pack(fill="x", pady=10)
        self.year_label = ctk.CTkLabel(
            self.year_frame,
            text="Ano referência:",
            font=("SF Pro Display", 16)
        )
        self.year_label.pack(side="left", padx=(10, 5))
        self.year_var = tk.StringVar(value="2024")

        self.year_selector = ttk.Combobox(
            self.year_frame,
            textvariable=self.year_var,
            values=[str(y) for y in range(2020, 2031)],
            width=8
        )
        self.year_selector.pack(side="left")

        # Aplica fundo escuro ao Combobox e ao menu suspenso (pode não funcionar em todos OS)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TCombobox",
                        fieldbackground="#222831",
                        background="#222831",
                        foreground="white",
                        selectforeground="white",
                        selectbackground="#222831",
                        borderwidth=0)
        style.map("TCombobox",
                  fieldbackground=[('readonly', '#222831')],
                  background=[('readonly', '#222831')],
                  foreground=[('readonly', 'white')])

        # Resumo Mensal
        self.monthly_frame = ctk.CTkFrame(self.main_frame)
        self.monthly_frame.pack(fill="x", pady=10)
        self.monthly_label = ctk.CTkLabel(
            self.monthly_frame,
            text="Resumo Mensal",
            font=("SF Pro Display", 18, "bold")
        )
        self.monthly_label.pack(anchor="w", padx=10, pady=(0, 5))

        self.months_container = ctk.CTkFrame(self.monthly_frame)
        self.months_container.pack(fill="x", padx=10)

        months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                  "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

        self.categorias = []  # O usuário irá cadastrar
        self.dados_mensais = {mes: {} for mes in months}

        # Aplica fundo escuro à tabela e define a fonte igual à dos meses (apenas UMA vez)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#222831",
                        foreground="white",
                        fieldbackground="#222831",
                        rowheight=20,
                        font=("SF Pro Display", 14, "bold"))
        style.configure("Treeview.Heading",
                        background="#393E46",
                        foreground="white",
                        font=("SF Pro Display", 15, "bold"))

        # Primeira linha: Janeiro a Junho
        row1 = ctk.CTkFrame(self.months_container)
        row1.pack(fill="x", pady=0, expand=False)
        for i in range(6):
            col_frame = ctk.CTkFrame(row1)
            col_frame.pack(side="left", expand=True, fill="both", padx=2)

            mes = months[i]
            mes_label = ctk.CTkLabel(
                col_frame,
                text=mes,
                font=("SF Pro Display", 14, "bold")
            )
            mes_label.pack(pady=(2, 0))

            tree = ttk.Treeview(
                col_frame,
                columns=("Categoria", "Total"),
                show="headings",
                height=5  # Diminui a altura da tabela
            )
            tree.heading("Categoria", text="Categoria")
            tree.heading("Total", text="Total")
            tree.column("Categoria", width=90)
            tree.column("Total", width=70)
            tree.pack(pady=(0, 2), padx=2, fill="x")

            # Preenche a tabela com os dados do mês, se houver
            for cat in self.categorias:
                valor = self.dados_mensais[mes].get(cat, 0)
                tree.insert("", "end", values=(cat, f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")))

        # Segunda linha: Julho a Dezembro
        row2 = ctk.CTkFrame(self.months_container)
        row2.pack(fill="x", pady=0, expand=False)
        for i in range(6, 12):
            col_frame = ctk.CTkFrame(row2)
            col_frame.pack(side="left", expand=True, fill="both", padx=2)

            mes = months[i]
            mes_label = ctk.CTkLabel(
                col_frame,
                text=mes,
                font=("SF Pro Display", 14, "bold")
            )
            mes_label.pack(pady=(2, 0))

            tree = ttk.Treeview(
                col_frame,
                columns=("Categoria", "Total"),
                show="headings",
                height=5  # Diminui a altura da tabela
            )
            tree.heading("Categoria", text="Categoria")
            tree.heading("Total", text="Total")
            tree.column("Categoria", width=90)
            tree.column("Total", width=70)
            tree.pack(pady=(0, 2), padx=2, fill="x")

            # Preenche a tabela com os dados do mês, se houver
            for cat in self.categorias:
                valor = self.dados_mensais[mes].get(cat, 0)
                tree.insert("", "end", values=(cat, f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")))

        # Resumo Anual
        self.annual_frame = ctk.CTkFrame(self.main_frame)
        self.annual_frame.pack(fill="both", expand=True, pady=10)

        self.annual_label = ctk.CTkLabel(
            self.annual_frame,
            text="Resumo Anual",
            font=("SF Pro Display", 18, "bold")
        )
        self.annual_label.pack(anchor="center", padx=10, pady=(0, 5))  # Centralizado

        self.annual_content = ctk.CTkFrame(self.annual_frame)
        self.annual_content.pack(anchor="center", pady=10)  # Centraliza o conteúdo

        # Tabela de categorias (fundo escuro)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#222831",  # Fundo escuro
                        foreground="white",
                        fieldbackground="#222831",
                        rowheight=28,
                        font=("SF Pro Display", 12))
        style.configure("Treeview.Heading",
                        background="#393E46",
                        foreground="white",
                        font=("SF Pro Display", 13, "bold"))

        self.categories_table = ttk.Treeview(
            self.annual_content,
            columns=("Categoria", "Total"),
            show="headings",
            height=8,
            style="Treeview"
        )
        self.categories_table.heading("Categoria", text="Categoria")
        self.categories_table.heading("Total", text="Total")
        self.categories_table.column("Categoria", width=150)
        self.categories_table.column("Total", width=80)
        self.categories_table.pack(side="left", fill="y", padx=(0, 10), pady=10)
        # Não insere categorias fixas, o usuário irá criar as categorias

        # Gráfico pizza (mockup)
        self.pizza_canvas = tk.Canvas(self.annual_content, width=200, height=200, bg="#222831", highlightthickness=0)
        self.pizza_canvas.pack(side="left", padx=10, pady=10)
        self.pizza_canvas.create_oval(20, 20, 180, 180, fill="#444", outline="#888")
        self.pizza_canvas.create_text(100, 100, text="Gráfico Pizza", fill="white", font=("SF Pro Display", 12))

        # Frame externo para centralizar e travar os botões na tela
        self.buttons_outer_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.buttons_outer_frame.pack(fill="x", pady=10)

        # Frame interno centralizado
        self.buttons_frame = ctk.CTkFrame(self.buttons_outer_frame, fg_color="transparent")
        self.buttons_frame.pack(anchor="center")

        # Botão "Nova Categoria"
        self.add_category_btn = ctk.CTkButton(
            self.buttons_frame,
            text="Nova Categoria",
            width=150,
            font=("SF Pro Display", 14)
        )
        self.add_category_btn.pack(side="left", padx=10, pady=5)

        # Botão "Nova Despesa"
        self.add_expense_btn = ctk.CTkButton(
            self.buttons_frame,
            text="Nova Despesa",
            width=150,
            font=("SF Pro Display", 14)
        )
        self.add_expense_btn.pack(side="left", padx=10, pady=5)

        # Botão "Novo Provento"
        self.add_income_btn = ctk.CTkButton(
            self.buttons_frame,
            text="Novo Provento",
            width=150,
            font=("SF Pro Display", 14)
        )
        self.add_income_btn.pack(side="left", padx=10, pady=5)

        # Defina um tamanho mínimo para a janela
        self.minsize(700, 600)

    def open_month_details(self, month):
        tk.messagebox.showinfo("Detalhes do Mês", f"Detalhes de {month} (implemente MonthDetails aqui)")

if __name__ == "__main__":
    app = Master()
    app.mainloop()