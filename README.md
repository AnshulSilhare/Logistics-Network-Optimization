# 📦 Amazon Logistics Digital Twin: Network Optimization

### 🚀 [View Live Interactive Map](YOUR_HTMLPREVIEW_LINK_HERE)
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
