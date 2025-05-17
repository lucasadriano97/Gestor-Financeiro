import customtkinter as ctk
from PIL import Image
from MainMenu import Master

class StartMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Lucky Financial Assistant - LFA")
        self.geometry("900x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Carregar imagem de fundo
        bg_image_path = r"C:\Users\lucas\Desktop\Projetos\Gestor-Financeiro\Images\Fundo.png"
        bg_image = Image.open(bg_image_path)
        self.bg_photo = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(900, 600))

        self.bg_label = ctk.CTkLabel(self, text="", image=self.bg_photo)
        self.bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Atualizar imagem ao redimensionar
        self.bind("<Configure>", self._resize_bg)

        # Botão "Iniciar" um pouco acima do rodapé
        self.start_button = ctk.CTkButton(
            self,
            text="Iniciar",
            corner_radius=20,
            width=200,
            height=40,
            font=("SF Pro Display", 18, "bold"),
            command=self.open_main_menu
        )
        self.start_button.place(relx=0.5, rely=0.82, anchor="center")

    def _resize_bg(self, event):
        new_width = event.width
        new_height = event.height
        self.bg_photo.configure(size=(new_width, new_height))
        self.bg_label.configure(image=self.bg_photo)

    def open_main_menu(self):
        from MainMenu import Master
        self.withdraw()
        main_menu = Master()
        main_menu.grab_set()

if __name__ == "__main__":
    app = StartMenu()
    app.mainloop()