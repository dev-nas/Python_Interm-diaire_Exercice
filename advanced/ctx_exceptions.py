class Ctx:
    
    def __enter__(self):
        pass

    # x_type : Classe de l'exception levée dans le bloc
    # x_value : message ou objet de l'exception
    # x_trace : la stack trace de l'erreur
    def __exit__(self, x_type, x_value, x_trace):
        if x_type:
            print(x_type, x_value, x_trace.tb_frame.f_code)
        # retourner qqch semblable à True ne relève pas l'exception
        return True

if __name__ == "__main__":
    
    # le contexte récupère les exceptions du bloc dans le __exit__
    with Ctx():
        3/0