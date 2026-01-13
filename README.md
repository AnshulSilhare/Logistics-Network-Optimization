# 📦 Amazon Logistics Network Optimization

### 🚀 [View Live Interactive Map](https://AnshulSilhare.github.io/Logistics-Network-Optimization/map.html)
*Dynamic geospatial analysis of the 5-node hub-and-spoke network. (Generated via Python/Folium)*

![Network Flow Animation](network-flow.gif)

## 📝 Executive Summary
This project engineers a **Digital Twin** of a high-volume logistics network to solve the "Last Mile" efficiency problem. The goal: achieve **90% US population coverage** within a **48-hour transit window** while minimizing Capital Expenditure (CapEx).

Moving beyond static Excel modeling, I utilized **Python** to programmatically visualize supply chain flows, calculate geodesic distances, and stress-test a 5-node distribution strategy against real-world constraints.

## 📊 Key Performance Indicators (KPIs)
*Snapshot of the network performance upon final optimization:*

| Metric | Result | Strategic Impact |
| :--- | :--- | :--- |
| **Network Structure** | **Hub-and-Spoke** | Consolidated 15 demand nodes into 5 regional DCs. |
| **Active Hubs** | **5** | Redlands (CA), Robbinsville (NJ), Louisville (KY), Coppell (TX), Lakeland (FL). |
| **Avg Delivery Radius** | **249 km** | **18% reduction** in fuel consumption vs. legacy 3-node model. |
| **Service Level** | **94%** | Customers reached within <48hr transit window. |

## 🧠 Economic & Operational Logic
My analysis balanced Service Levels against Macroeconomic constraints:
* **CapEx Optimization:** With the current cost of capital, opening >5 warehouses yielded diminishing returns on ROI (Return on Investment).
* **Fuel Hedging:** By algorithmically minimizing the "Average Delivery Distance" to 249km, the network is insulated from global oil price volatility.
* **Risk Mitigation:** The "Midwest Flow" (Louisville Hub) acts as a redundancy node, capable of absorbing overflow from the East Coast during peak season.

## 💻 Technical Architecture
### Tech Stack
* **Python 3.10:** Core logic for distance calculation and node mapping.
* **Folium:** Geospatial visualization and AntPath animation.
* **Pandas:** Data handling for transit matrices.
* **Google Colab:** Cloud-based development environment.

### Code Snippet: Logic-Driven Visualization
The following snippet demonstrates how transit times dictate the visual "risk" indicators on the map:

```python
# LOGIC: Dynamic coloring based on transit efficiency
# If transit time > 2 days, the route is flagged Red (Risk)
# If transit time <= 2 days, the route is flagged Green (Optimized)

for cust in customers:
    line_color = "red" if cust['transit_days'] > 2 else "green"
    
    folium.PolyLine(
        locations=[warehouse_loc, customer_loc],
        color=line_color,
        weight=2.5,
        tooltip=f"Route Efficiency: {cust['efficiency_score']}"
    ).add_to(map_layer)
```

## ⚡ Development Workflow (AI-Augmented)
This project utilizes a modern, AI-augmented workflow to maximize development velocity.

* **Architecture & Strategy:** The network design, KPI selection, and economic constraints were defined by the author.
* **Code Acceleration:** Large Language Models (LLMs) were utilized to generate Folium syntax boilerplate and optimize the HTML injection for the dashboard HUD.
* **Validation:** All code logic was reviewed, tested, and validated against the source Excel datasets to ensure 100% accuracy.

## 📂 Project Structure
```bash
├── data
│   ├── Network_Model.xlsx       # Source data for transit times
│   └── coordinates.csv          # Geocoded city locations
├── src
│   ├── network_optimizer.py     # Main Python logic
│   └── map_generator.ipynb      # Jupyter Notebook for visualization
├── output
│   └── map.html # Interactive map (Result)
└── README.md
