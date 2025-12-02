from sqlalchemy import create_engine #lay thu vien, ket noi den db
from sqlalchemy.orm import sessionmaker, declarative_base  #tao session de lam viec voi db, tao lop co so de dinh nghia mo hinh

DATABASE_URL = "postgresql://postgres:qxike1819@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL) #tao engine ket noi giua sqlalcemy va db
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False) #tao session de dam bao ket noi voi db

Base = declarative_base() #tao lop co so de dinh nghia mo hinh, cac lop mo hinh se ke thua lop nay

def get_db(): #tao 1 session db voi moi api request, dam bao an toan va tu dong dong ket noi
    db = SessionLocal()
    try:        
        yield db
    finally:
        db.close()
