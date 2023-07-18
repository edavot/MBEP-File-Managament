""" Comments.py """
import file

class Comments:
    
    FILE_NAME = 'data/comments.json'

    content: str
    created_by: str
    article: str

    def __init__(self, content: str, created_by: str, article: str):
        self.content = content
        self.created_by = created_by
        self.article = article
        
    def save(self):
        file.create_or_update(self.FILE_NAME, self.__dict__)

test = Comments('Contenido', 'Enrique Avalos', 'Articulo')
test.save()