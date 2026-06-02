import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [influencers, setInfluencers] = useState([]);
  const [metrics, setMetrics] = useState(null);
  const [searchInput, setSearchInput] = useState("");

  const [filters, setFilters] = useState({
    search: "",
    platform: "All",
    niche: "All",
    sortBy: "score",
  });

 const fetchInfluencers = () => {
  const params = new URLSearchParams({
    search: filters.search,
    platform: filters.platform,
    niche: filters.niche,
    sort_by: filters.sortBy,
  });

  fetch(`http://a0858ec5e2142481788fbf97d57b4f8e-217161621.us-east-1.elb.amazonaws.com/api/influencers?${params}`)
    .then((res) => res.json())
    .then((data) => setInfluencers(data))
    .catch((err) => console.error("API error:", err));
};

const fetchMetrics = () => {
  fetch("http://a0858ec5e2142481788fbf97d57b4f8e-217161621.us-east-1.elb.amazonaws.com/api/metrics")
    .then((res) => res.json())
    .then((data) => setMetrics(data))
    .catch((err) => console.error("Metrics API error:", err));
};

  useEffect(() => {
    fetchInfluencers();
    fetchMetrics();
  }, [filters]);

  const handleSearch = () => {
    setFilters((prev) => ({
      ...prev,
      search: searchInput,
    }));
  };

  const handleReset = () => {
    setSearchInput("");
    setFilters({
      search: "",
      platform: "All",
      niche: "All",
      sortBy: "score",
    });
  };

  return (
    <main className="dashboard">
      <section className="hero">
        <p className="eyebrow">Cloud-Native SaaS Demo</p>
        <h1>Influencer Analytics Dashboard</h1>
        <p>
          Search, filter, and rank influencer profiles using a React frontend
          connected to a FastAPI backend running on AWS EKS.
        </p>
      </section>

      <section className="stats">
        <div>
          <span>Total Influencers</span>
          <strong>{metrics?.total_influencers || 0}</strong>
        </div>
        <div>
          <span>Total Reach</span>
          <strong>{metrics?.total_reach?.toLocaleString() || 0}</strong>
        </div>
        <div>
          <span>Avg Engagement</span>
          <strong>{metrics?.average_engagement || 0}%</strong>
        </div>
        <div>
          <span>Avg Price</span>
          <strong>${metrics?.average_price?.toLocaleString() || 0}</strong>
        </div>
        <div>
          <span>Top Platform</span>
          <strong>{metrics?.top_platform || "-"}</strong>
        </div>
        <div>
          <span>Top Niche</span>
          <strong>{metrics?.top_niche || "-"}</strong>
        </div>
      </section>

      <section className="controls">
        <label>
          Search
          <input
            value={searchInput}
            onChange={(e) => setSearchInput(e.target.value)}
            placeholder="Name, niche, location, or all"
          />
        </label>

        <label>
          Platform
          <select
            value={filters.platform}
            onChange={(e) =>
              setFilters((prev) => ({ ...prev, platform: e.target.value }))
            }
          >
            <option>All</option>
            <option>Instagram</option>
            <option>TikTok</option>
            <option>YouTube</option>
          </select>
        </label>

        <label>
          Niche
          <select
            value={filters.niche}
            onChange={(e) =>
              setFilters((prev) => ({ ...prev, niche: e.target.value }))
            }
          >
            <option>All</option>
            <option>Beauty</option>
            <option>Lifestyle</option>
            <option>Fitness</option>
            <option>Fashion</option>
            <option>Tech</option>
            <option>Travel</option>
            <option>Finance</option>
          </select>
        </label>

        <label>
          Sort by
          <select
            value={filters.sortBy}
            onChange={(e) =>
              setFilters((prev) => ({ ...prev, sortBy: e.target.value }))
            }
          >
            <option value="score">Best Match Score</option>
            <option value="followers">Followers</option>
            <option value="engagement_rate">Engagement Rate</option>
            <option value="avg_views">Average Views</option>
            <option value="price">Campaign Price</option>
          </select>
        </label>

        <button onClick={handleSearch}>Search</button>
        <button onClick={handleReset}>Reset</button>
      </section>

      <section className="results-header">
        <h2>Influencer Results</h2>
        <p>{influencers.length} profiles found</p>
      </section>

      <section className="cards">
        {influencers.map((creator) => (
          <article className="card" key={creator.id}>
            <div className="score">{creator.score}</div>
            <h2>{creator.name}</h2>
            <p>
              {creator.niche} · {creator.platform}
            </p>
            <strong>{creator.followers.toLocaleString()} followers</strong>
            <span>{creator.engagement_rate}% engagement</span>
            <span>{creator.avg_views.toLocaleString()} avg views</span>
            <span>${creator.price.toLocaleString()} campaign price</span>
            <small>{creator.location}</small>
          </article>
        ))}
      </section>
    </main>
  );
}

export default App;