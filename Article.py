""" Article.py """
import file

class Article:
    FILE_NAME = 'data/articles.json'

    title: str
    content: str
    status: str
    image: str
    created_by: str

    def __init__(self, title: str, content: str, status: str, image:str, created_by: str):
        self.title = title
        self.content = content
        self.status = status
        self.image = image
        self.created_by = created_by
        
    def save(self):
        file.create_or_update(self.FILE_NAME, self.__dict__)

test = Article('Titulo', 'Contenido','Activo','img.png', 'Enrique Avalos')
test.save()