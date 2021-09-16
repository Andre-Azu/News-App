from . import db


class use(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

        
class News:
    '''
    class that genrates news object
    '''

    def __init__(self,source,author,url,article,description,image,time_published):
        self.source=source
        self.author=author
        self.url=url
        self.article=article
        self.description=description
        self.image=image
        self.time_published=time_published

