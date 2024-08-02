try:
    from . import BASE, SESSION, engine
except ImportError as e:
    raise Exception("Hello!") from e
from sqlalchemy import Column, String


class MustafaLink(BASE):
    __tablename__ = "Mustafa_links"
    key = Column(String(255), primary_key=True)
    url = Column(String(255))

    def __init__(self, key, url):
        self.key = str(key)
        self.url = str(url)


MustafaLink.__table__.create(bind=engine, checkfirst=True)


def get_link(key):
    link = SESSION.query(MustafaLink).get(str(key))
    return link.url if link else None


def add_link(key, url):
    link = MustafaLink(str(key), str(url))
    SESSION.add(link)
    SESSION.commit()
    
def delete_link(key):
    link = SESSION.query(MustafaLink).get(str(key))
    if link:
        SESSION.delete(link)
        SESSION.commit()