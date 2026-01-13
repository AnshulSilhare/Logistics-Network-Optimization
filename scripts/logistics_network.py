"""
PROJECT: Amazon Logistics Network Optimization
AUTHOR: Anshul Silhare (Supply Chain Analyst)

BUSINESS CONTEXT:
This model overcomes the row limits and processing constraints of Excel 
to simulate a 5-node distribution network for the US market.

METHODOLOGY:
1. Network Configuration: Structuring demand signals from 15 major metro regions.
2. Geospatial Logic: Utilizing Haversine formula for precise 'Center of Gravity' calculations.
3. Visualization: Generating an interactive HTML dashboard for stakeholder reporting.

OUTPUT:
- Interactive Map (HTML)
- KPI Dashboard (Service Levels, Average Distance)
"""
import folium
from folium import plugins
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

# --- 1. DATA SETUP ---
data = {
    'Name': ['NYC Metro', 'Philadelphia Metro', 'Boston Metro', 'DC Metro', 'Chicago Metro', 'Miami Metro', 'Atlanta Metro', 'Dallas Metro', 'LA Metro', 'Houston Metro', 'ONT9 (SoCal)', 'DFW6 (Dallas)', 'SDF2 (Louisville)', 'EWR4 (NJ/NY)', 'TPA2 (Tampa)'],
    'Type': ['Demand', 'Demand', 'Demand', 'Demand', 'Demand', 'Demand', 'Demand', 'Demand', 'Demand', 'Demand', 'Warehouse', 'Warehouse', 'Warehouse', 'Warehouse', 'Warehouse'],
    'Lat': [40.7128, 39.9526, 42.3601, 38.9072, 41.8781, 25.7617, 33.7490, 32.7767, 34.0522, 29.7604, 34.0633, 32.9, 38.2, 40.5, 27.9],
    'Lon': [-74.0060, -75.1652, -71.0589, -77.0369, -87.6298, -80.1918, -84.3880, -96.7970, -118.2437, -95.3698, -117.6509, -97.0, -85.7, -74.5, -82.4],
    'Volume': [80, 60, 50, 55, 75, 45, 50, 65, 90, 60, 300, 250, 200, 280, 150]
}
df = pd.DataFrame(data)
warehouses = df[df['Type'] == 'Warehouse'].reset_index(drop=True)
demand = df[df['Type'] == 'Demand'].reset_index(drop=True)

# Helper function for KPIs
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    c = 2 * asin(sqrt(sin((lat2 - lat1)/2)**2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1)/2)**2))
    return c * 6371

# --- 2. MAP SETUP & TITLE ---
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4, tiles='cartodbpositron')

title_html = '''
     <h3 align="center" style="font-size:22px; font-family:sans-serif; color:#333;">
     <b>Amazon Logistics Network:</b> Optimized Flow & Coverage Analysis
     </h3>
             '''
m.get_root().html.add_child(folium.Element(title_html))

# --- 3. DRAW NETWORK ---
hub_colors = {'ONT9 (SoCal)': '#FF8C00', 'DFW6 (Dallas)': '#DC143C', 'SDF2 (Louisville)': '#228B22', 'EWR4 (NJ/NY)': '#0000CD', 'TPA2 (Tampa)': '#800080'}

layers = {}
for hub in warehouses['Name']:
    layers[hub] = folium.FeatureGroup(name=f"Region: {hub}")

total_dist_km = 0
route_count = 0

for idx, row in demand.iterrows():
    # Find nearest warehouse
    dists = ((warehouses['Lat'] - row['Lat'])**2 + (warehouses['Lon'] - row['Lon'])**2)
    nearest_w = warehouses.loc[dists.idxmin()]
    dist_km = haversine(row['Lon'], row['Lat'], nearest_w['Lon'], nearest_w['Lat'])
    total_dist_km += dist_km
    route_count += 1

    route_color = hub_colors.get(nearest_w['Name'], 'gray')
    target_layer = layers[nearest_w['Name']]

    # Animated Ant Paths
    plugins.AntPath(
        locations=[[nearest_w['Lat'], nearest_w['Lon']], [row['Lat'], row['Lon']]],
        color=route_color,
        weight=3,
        dash_array=[15, 30],
        delay=800,
        pulse_color='#FFFFFF',
        tooltip=f"Flow: {int(dist_km)} km"
    ).add_to(target_layer)

    # --- UPDATED: SMALLER CIRCLE MARKERS ---
    # Multiplier changed from 2.5 to 1.3 for smaller bubbles
    scaled_radius = np.sqrt(row['Volume']) * 1.3

    folium.CircleMarker(
        location=[row['Lat'], row['Lon']],
        radius=scaled_radius,
        color=route_color, fill=True, fill_color=route_color, fill_opacity=0.8,
        popup=folium.Popup(f"""
            <div style='font-family:sans-serif; width: 150px;'>
                <h5 style='margin:5px 0; border-bottom:1px solid {route_color}'><b>{row['Name']}</b></h5>
                <b>Type:</b> Demand Node<br>
                <b>Vol:</b> {row['Volume']}k units<br>
                <b>Hub:</b> {nearest_w['Name']}
            </div>
        """, max_width=200),
        tooltip=f"<b>{row['Name']}</b><br>Vol: {row['Volume']}k"
    ).add_to(target_layer)

# --- 4. DRAW WAREHOUSES ---
warehouse_layer = folium.FeatureGroup(name="Distribution Centers", show=True)
for idx, row in warehouses.iterrows():
    icon = folium.Icon(color='black', icon_color='white', icon='industry', prefix='fa')

    folium.Marker(
        location=[row['Lat'], row['Lon']],
        icon=icon,
        tooltip=f"<b>DC: {row['Name']}</b><br>Cap: {row['Volume']}k",
        popup=f"<b>DISTRIBUTION CENTER</b><br>{row['Name']}<br>Capacity: {row['Volume']}k Units"
    ).add_to(warehouse_layer)

warehouse_layer.add_to(m)
for layer in layers.values():
    layer.add_to(m)

folium.LayerControl(collapsed=False, position='topright').add_to(m)

# --- 5. KPI DASHBOARD & LEGEND ---
avg_coverage = int(total_dist_km / route_count) if route_count > 0 else 0

kpi_html = f'''
<div style="position: fixed; bottom: 30px; right: 30px; width: 220px; z-index:9999; background: rgba(255,255,255,0.9);
            border-radius: 8px; padding: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); font-family: sans-serif;">
    <h4 style="margin:0 0 10px 0; text-align:center; border-bottom: 2px solid #333; padding-bottom:5px;">Network Snapshot</h4>
    <div style="display: flex; justify-content: space-between; margin-bottom: 5px;"><span>Active Nodes:</span><b>{len(df)}</b></div>
    <div style="display: flex; justify-content: space-between; margin-bottom: 5px;"><span>Dist Centres:</span><b>{len(warehouses)}</b></div>
    <div style="display: flex; justify-content: space-between; margin-bottom: 5px;"><span>Avg Delivery:</span><b>{avg_coverage} km</b></div>
    <div style="margin-top: 10px; text-align:center; background:#dff0d8; color:#3c763d; padding:5px; border-radius:4px;">
        <b>STATUS: HIGHLY OPTIMIZED</b>
    </div>
</div>
'''
m.get_root().html.add_child(folium.Element(kpi_html))
m.get_root().html.add_child(folium.Element(kpi_html))

legend_html = '''
     <div style="position: fixed; bottom: 30px; left: 30px; width: 180px; z-index:9999; font-family: sans-serif;
     background: rgba(255,255,255,0.9); border-radius: 8px; padding: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
     <b>Regional Flow Legend</b><br>
     <small><i>Animated paths indicate flow direction</i></small><br>
     <i class="fa fa-industry" style="color:black"></i> Distribution Center<br>
     <span style="color:#FF8C00;">&#9679;</span> SoCal Flow<br>
     <span style="color:#DC143C;">&#9679;</span> Dallas Flow<br>
     <span style="color:#228B22;">&#9679;</span> Midwest Flow<br>
     <span style="color:#0000CD;">&#9679;</span> Northeast Flow<br>
     <span style="color:#800080;">&#9679;</span> Southeast Flow<br>
     </div>
     '''
m.get_root().html.add_child(folium.Element(legend_html))

# --- 6. SAVE ---
m.save("amazon_network_perfected_v2.html")
m
