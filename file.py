""" file.py """
def create_file(file_name: str, content: str = None):
    """ Crea archivos con o sin contenido """
    mode = "w" if content else "x"
    with open(file_name, mode) as file:
        if content:
            file.write(content)

def modify_file(file_name: str, content: str, overwrite: bool = False):
    """  Modifica archivos """
    mode = "w" if overwrite else "a"
    with open(file_name, mode) as file:
        file.write(content)

def read_file(file_mane: str) ->  str:
    """  Lectura de archivos """
    content = ""
    with open(file_mane, "r") as file:
        content += file.readline()
    return content