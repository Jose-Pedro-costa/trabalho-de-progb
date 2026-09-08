from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import User, Track, Favorite, SearchHistory, DownloadHistory
from app.models.base import Base
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def seed_database():
    
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    try:
       
        if not db.query(User).first():
            users = [
                User(
                    name="Ana Silva",
                    email="ana@email.com",
                    hashed_password=get_password_hash("123456"),
                    created_at=datetime.utcnow()
                ),
                User(
                    name="João Santos",
                    email="joao@email.com",
                    hashed_password=get_password_hash("123456"),
                    created_at=datetime.utcnow()
                ),
            ]
            db.add_all(users)
            db.commit()
            print(" Usuários criados")

        
        if not db.query(Track).first():
            tracks = [
                Track(
                    title="Sunrise Melody",
                    artist="Free Sounds Collective",
                    album="Morning Vibes",
                    genre="Ambient",
                    duration=210,  # em segundos
                    cover_url="https://picsum.photos/seed/sunrise/300/300",
                    audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
                    created_at=datetime.utcnow()
                ),
                Track(
                    title="Ocean Waves",
                    artist="Nature Beats",
                    album="Relaxation",
                    genre="Ambient",
                    duration=185,
                    cover_url="https://picsum.photos/seed/ocean/300/300",
                    audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                    created_at=datetime.utcnow()
                ),
                Track(
                    title="City Lights",
                    artist="Urban Free",
                    album="Night Drive",
                    genre="Electronic",
                    duration=240,
                    cover_url="https://picsum.photos/seed/city/300/300",
                    audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                    created_at=datetime.utcnow()
                ),
                Track(
                    title="Acoustic Dream",
                    artist="Indie Open",
                    album="Simple Strings",
                    genre="Acoustic",
                    duration=195,
                    cover_url="https://picsum.photos/seed/acoustic/300/300",
                    audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
                    created_at=datetime.utcnow()
                ),
                Track(
                    title="Jazz Night",
                    artist="Open Jazz Band",
                    album="Late Hours",
                    genre="Jazz",
                    duration=265,
                    cover_url="https://picsum.photos/seed/jazz/300/300",
                    audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
                    created_at=datetime.utcnow()
                ),
            ]
            db.add_all(tracks)
            db.commit()
            print("✅ Músicas criadas")

        
        user1 = db.query(User).filter(User.email == "ana@email.com").first()
        track1 = db.query(Track).filter(Track.title == "Sunrise Melody").first()
        track2 = db.query(Track).filter(Track.title == "Ocean Waves").first()

        if user1 and track1 and not db.query(Favorite).first():
            favorites = [
                Favorite(user_id=user1.id, track_id=track1.id),
                Favorite(user_id=user1.id, track_id=track2.id),
            ]
            db.add_all(favorites)
            db.commit()
            print(" Favoritos criados")

        
        if not db.query(SearchHistory).first():
            searches = [
                SearchHistory(user_id=user1.id, query="ambient", created_at=datetime.utcnow()),
                SearchHistory(user_id=user1.id, query="jazz", created_at=datetime.utcnow()),
            ]
            db.add_all(searches)
            db.commit()
            print(" Histórico de buscas criado")

       
        if not db.query(DownloadHistory).first():
            downloads = [
                DownloadHistory(user_id=user1.id, track_id=track1.id, created_at=datetime.utcnow()),
            ]
            db.add_all(downloads)
            db.commit()
            print(" Histórico de downloads criado")

        print("\n Seed finalizada com sucesso!")

    except Exception as e:
        print(f"Erro ao executar a seed: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
