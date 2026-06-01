from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Influencer Analytics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

influencers = [
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
    data = influencers.copy()

    if search and search.lower() != "all":
        data = [
            item for item in data
            if search.lower() in item["name"].lower()
            or search.lower() in item["niche"].lower()
            or search.lower() in item["location"].lower()
        ]

    if platform != "All":
        data = [item for item in data if item["platform"] == platform]

    if niche != "All":
        data = [item for item in data if item["niche"] == niche]

    if sort_by in ["followers", "engagement_rate", "avg_views", "price", "score"]:
        data = sorted(data, key=lambda x: x[sort_by], reverse=True)

    return data

@app.get("/api/metrics")
def get_metrics():
    return {
        "total_influencers": len(influencers),
        "average_engagement": round(sum(i["engagement_rate"] for i in influencers) / len(influencers), 2),
        "top_platform": "TikTok",
        "top_niche": "Beauty",
    }