from .lib_download import descargarPlaylistVideo
from sys import version

if version[0] == "3":
    from tkinter import Frame, Label, Entry, Button, messagebox
elif version[0] == "2":
    from Tkinter import (Frame, Label, PhotoImage, Button, Entry)
else:
    print("Wtf que porongas paso aqui?!")

from .load_config import calcular_file, load_file

class Frame2:
    
    def __init__(self,
                VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
                InstanciaPadre,
                # parametro por defecto para la clase:
                grosor_borde=1,                                     # Grosor para el Frame por defecto
                color_fondo="white",                                # color de fondo por defecto de la venta
                tamano_ventana=[400, 250],                          # tamaño de la ventana por defecto [x, y]
                tipo_cursor="tcross",                               # Cursor por defecto(cruz)
                tipo_borde="sunken",                                # tipo de borde por defecto
                load_json=True                                      # cargar la configuracion del .json
        ):
        
        if load_json:
            ruta = calcular_file(__file__, "config-GUI")
            print("[[ ",ruta)
            config_data = load_file(ruta)
            print(config_data)
            
            grosor_borde = config_data["grosor-borde"]
            color_fondo = config_data["color-background"]
            tamano_ventana = config_data["size"]
            tipo_cursor = config_data["tipo-cursor"]
            tipo_borde = config_data["tipo-borde"]
        
        self.VentanaPadre = VentanaPadre
        self.Frame = Frame(self.VentanaPadre)
        VentanaPadre.FrameActual = 2
        self.InstanciaPadre = InstanciaPadre
        
        self.Frame.config(
            width=tamano_ventana[0], 
            height=tamano_ventana[1], # Cambiar tamaño del Frame 
            bg=color_fondo,           # Cambiando color de fondo
            bd=grosor_borde,          # Cambiando grosor del borde
            relief=tipo_borde,        # Cambiar el tipo de borde
            cursor=tipo_cursor        # Cambiar el cursor
        )
        
        self.Frame.pack(
            fill="both", 
            anchor="center", # centramos el frame
            expand=1, # permitimos expandir el Frame
            side="top",
        )

        self.EqtiquetaInformacion1 = Label(self.Frame, text="Programa creado en Python para \ndescargar vídeos de Youtube\n")
        self.EqtiquetaInformacion1.grid(row=0, column=1)
        # texto1 = StringVar()
        # texto1.set("") 3 Nos permite cambiar el texto a lo largo de la ejecucion del programa
        self.EqtiquetaInformacion1.config(
                        bg="#aaaaaa",         # Color de fondo
                        fg="black",         # Color de letras
                        font=("Console", 10), # Tipo y tamaño de letra
                        padx=10, pady=10    # Margene
                        #textvariable=texto1 # texto variable
                    )  
        
        self.videos = Entry(self.Frame)
        self.videos.grid(row=1, column=1)

        self.boton = Button(self.Frame, text="Descargar :)", command=self.downloadPlayListVideo, relief="groove")
        self.boton.grid(row=2, column=1)        

    def downloadPlayListVideo(self):
        descargarPlaylistVideo(self.videos.get(), messagebox=messagebox, Frame=self.Frame)