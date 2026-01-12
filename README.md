# 🚚 Logistics Network Design: 5-Node Optimization Model

## Executive Summary
This project analyzes the optimal distribution network for a retail client requiring **90% US coverage within 48 hours**. Using a Center of Gravity approach and transit time modeling, I compared a 3-Node legacy network against a proposed 5-Node strategic expansion.

## 📊 Key Results
| Metric | Legacy Network (3 Nodes) | Optimized Network (5 Nodes) |
| :--- | :--- | :--- |
| **2-Day Coverage** | 65% of US Population | **94% of US Population** |
| **Avg Transit Time** | 3.4 Days | **1.8 Days** |
| **transportation Spend** | High (Zone Skipping) | **Optimized (Local Delivery)** |

## 🗺️ Visual Analysis

### 1. Network Configuration (The "Lean 5-Node" Strategy)
*Visualizing the strategic placement of Redlands, Robbinsville, Louisville, Coppell, and Lakeland.*

![Network Map](YOUR_MAP_IMAGE_FILENAME_HERE.jpg)

### 2. Service Level Validation
*Breakdown of transit days from regional hubs to major metro areas.*

![Transit Table](YOUR_TABLE_IMAGE_FILENAME_HERE.jpg)

## 🛠️ Methodology & Tools
- **Hub Selection:** Utilized weighted scoring (Labor Cost, Fuel Rates, Proximity to Ports) to select the 5 nodes.
- **Tools:** Advanced Excel (Solver Add-in), Bing Maps API for distance logic.
- **Constraints:** Modeled under the constraint that no single facility exceeds 85% capacity during peak season.

## 📂 File Description
- `Network_Model_Sanitized.xlsx`: The source data containing the distance matrix and cost-to-serve calculations.
