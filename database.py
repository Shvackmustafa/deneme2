from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
db = Database(DATABASE_URL)
