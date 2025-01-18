from database import engine, metadata
from models import *

def create_tables():
    metadata.drop_all(engine, checkfirst=True)
    metadata.create_all(engine)
    print("Tüm veritabanı tabloları başarıyla oluşturuldu!")

if __name__ == "__main__":
    create_tables()
