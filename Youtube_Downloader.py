from ast import literal_eval

# Cargamos los modulos donde se han configurado cada Frame:
from frames.root import root, ruta
from frames.load_config import load_file, calcular_file
from frames.idiomas import Idiomas

from get_hash import get_directory, get_hash, write_dict_hash_dir, cheack_updates

information = literal_eval(open("information.json", "r").read())

__version__ = information["version"]
__doc__ = information["doc"]
__autor__ =  information["autor"]
__contribuidores__ = information["contribuidores"]


# Codigo principal a ejecutar:
if __name__ == "__main__":
    
    print("Comprobando actualizaciones....")
    tree_dir = get_directory(debug=False)
    #print_tree(tree_dir)
    
    dict_hash_dir = get_hash(tree_dir)
    #print_dict_hash_dir(dict_hash_dir)
    write_dict_hash_dir(dict_hash_dir)
    
    if cheack_updates():
        print("Hay una nueva version de este software!!!")
    
    print("\n"+"="*30)
    print ("version del software -> {}".format(__version__))
    print("="*30)
    print ("doc -> {}".format(__doc__))
    
    print("="*30)
    print ("contribuidores: ")
    for i in __contribuidores__:
        print ("Usuario -> {}".format(i["usuario"]))
        print ("Github -> {}".format(i["github"]))
        print("-"*30)
        
    print ("Autor -> {}".format(__autor__["usuario"]))
    print ("Github -> {}".format(__autor__["github"]))
    print("="*30+"\n")

    try:
        
        ruta = calcular_file(ruta, "config-GUI")
        print("[[ ",ruta)
        config_data = load_file(ruta)
        print(config_data)
        
        root = root(
            idioma=Idiomas(config_data["lenguaje"]),
            tamano_ventana=config_data["size"],
            color_fondo=config_data["color-background"]
        ) # instancia a la clase root
        
        root.root.mainloop()
    except KeyboardInterrupt:
        print("Saliendo")
        exit(0)
