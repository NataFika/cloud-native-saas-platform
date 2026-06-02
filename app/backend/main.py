import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "influencers")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "ChangeMe12345!")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

app = FastAPI(title="Influencer Analytics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Influencer(Base):
    __tablename__ = "influencers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    platform = Column(String)
    niche = Column(String)
    followers = Column(Integer)
    engagement_rate = Column(Float)
    location = Column(String)
    avg_views = Column(Integer)
    price = Column(Integer)
    score = Column(Integer)


seed_data = [
    {"id": 1, "name": "Sophia Lee", "platform": "Instagram", "niche": "Beauty", "followers": 120000, "engagement_rate": 5.8, "location": "Los Angeles", "avg_views": 45000, "price": 1200, "score": 91},
    {"id": 2, "name": "Mia Carter", "platform": "TikTok", "niche": "Lifestyle", "followers": 450000, "engagement_rate": 7.2, "location": "New York", "avg_views": 180000, "price": 3500, "score": 94},
    {"id": 3, "name": "Emma Brooks", "platform": "YouTube", "niche": "Fitness", "followers": 89000, "engagement_rate": 4.1, "location": "Miami", "avg_views": 30000, "price": 900, "score": 78},
    {"id": 4, "name": "Ava Stone", "platform": "Instagram", "niche": "Fashion", "followers": 230000, "engagement_rate": 6.4, "location": "Los Angeles", "avg_views": 85000, "price": 2100, "score": 88},
    {"id": 5, "name": "Liam Hayes", "platform": "YouTube", "niche": "Tech", "followers": 610000, "engagement_rate": 3.9, "location": "San Francisco", "avg_views": 220000, "price": 5200, "score": 86},
    {"id": 6, "name": "Olivia Reed", "platform": "TikTok", "niche": "Beauty", "followers": 980000, "engagement_rate": 8.5, "location": "Chicago", "avg_views": 410000, "price": 7600, "score": 97},
    {"id": 7, "name": "Noah Kim", "platform": "Instagram", "niche": "Fitness", "followers": 175000, "engagement_rate": 5.1, "location": "Seattle", "avg_views": 62000, "price": 1500, "score": 82},
    {"id": 8, "name": "Isabella Cruz", "platform": "TikTok", "niche": "Travel", "followers": 320000, "engagement_rate": 6.9, "location": "Austin", "avg_views": 140000, "price": 2800, "score": 90},
    {"id": 9, "name": "Ethan Moore", "platform": "YouTube", "niche": "Finance", "followers": 740000, "engagement_rate": 4.7, "location": "Boston", "avg_views": 260000, "price": 6400, "score": 89},
    {"id": 10, "name": "Grace Miller", "platform": "Instagram", "niche": "Lifestyle", "followers": 54000, "engagement_rate": 9.1, "location": "Los Angeles", "avg_views": 25000, "price": 700, "score": 84},
]


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        existing_count = db.query(Influencer).count()

        if existing_count == 0:
            for item in seed_data:
                db.add(Influencer(**item))
            db.commit()
    finally:
        db.close()


def influencer_to_dict(item):
    return {
        "id": item.id,
        "name": item.name,
        "platform": item.platform,
        "niche": item.niche,
        "followers": item.followers,
        "engagement_rate": item.engagement_rate,
        "location": item.location,
        "avg_views": item.avg_views,
        "price": item.price,
        "score": item.score,
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/api/influencers")
def get_influencers(
    search: str = "",
    platform: str = "All",
    niche: str = "All",
    sort_by: str = "score",
):
    db = SessionLocal()
    try:
        query = db.query(Influencer)

        if search and search.lower() != "all":
            search_term = f"%{search}%"
            query = query.filter(
                Influencer.name.ilike(search_term)
                | Influencer.niche.ilike(search_term)
                | Influencer.location.ilike(search_term)
            )

        if platform != "All":
            query = query.filter(Influencer.platform == platform)

        if niche != "All":
            query = query.filter(Influencer.niche == niche)

        allowed_sort_fields = {
            "followers": Influencer.followers,
            "engagement_rate": Influencer.engagement_rate,
            "avg_views": Influencer.avg_views,
            "price": Influencer.price,
            "score": Influencer.score,
        }

        sort_column = allowed_sort_fields.get(sort_by, Influencer.score)
        query = query.order_by(sort_column.desc())

        return [influencer_to_dict(item) for item in query.all()]
    finally:
        db.close()


@app.get("/api/platforms")
def get_platforms():
    db = SessionLocal()
    try:
        platforms = db.query(Influencer.platform).distinct().all()
        return sorted([item[0] for item in platforms])
    finally:
        db.close()


@app.get("/api/niches")
def get_niches():
    db = SessionLocal()
    try:
        niches = db.query(Influencer.niche).distinct().all()
        return sorted([item[0] for item in niches])
    finally:
        db.close()


@app.get("/api/metrics")
def get_metrics():
    db = SessionLocal()
    try:
        data = db.query(Influencer).all()

        total_reach = sum(i.followers for i in data)
        average_engagement = round(
            sum(i.engagement_rate for i in data) / len(data), 2
        )
        average_price = round(sum(i.price for i in data) / len(data), 2)

        platforms = [i.platform for i in data]
        niches = [i.niche for i in data]

        top_platform = max(set(platforms), key=platforms.count)
        top_niche = max(set(niches), key=niches.count)

        return {
            "total_influencers": len(data),
            "total_reach": total_reach,
            "average_engagement": average_engagement,
            "average_price": average_price,
            "top_platform": top_platform,
            "top_niche": top_niche,
        }
    finally:
        db.close()