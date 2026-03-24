# **Technical Manual: Smart Agriculture - Battery-Free TinyML Platform**
**Creator / Programmer:** David Akpoviroro Oke (MrIridescent - The Creative Renaissance Man)

---

## **1. Introduction**
The **Smart Agriculture - Battery-Free TinyML Platform** is a specialized framework for performing soil moisture and nutrient analysis using harvested environmental energy. This manual provides a simplified, step-by-step guide for setting up and operating the battery-free sensor node.

---

## **2. Installation & Prerequisites**

### **System Requirements**
- **Python 3.10+** (for simulation and setup).
- **Embedded Platform:** ARM Cortex-M Series or RISC-V SoC with solar/thermal harvesting modules.
- **Hardware:** 1MB RAM minimum; 4MB+ recommended for complex TinyML models.

### **Setup Instructions**
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/MrIridescent/Future-Proofing.git
    cd Future-Proofing/projects/smart_agri_battery_free
    ```
2.  **Run the Setup Script:**
    ```bash
    bash setup.sh
    ```
3.  **Verify the Sensor Logic:**
    ```bash
    python3 battery_free_agri.py
    ```

---

## **3. Step-by-Step Operation Guide**

### **Step 1: Initialize the Sensor Node**
Create an instance of the `BatteryFreeAgriSensor` with a unique ID for your agricultural node.
```python
sensor = BatteryFreeAgriSensor("AG-NODE-01")
```

### **Step 2: Harvest Energy**
During daylight hours or when thermal/RF sources are available, invoke the `harvest_energy` method to store power.
```python
sensor.harvest_energy(light_intensity=100, duration_sec=3600)
```

### **Step 3: Trigger TinyML Soil Analysis**
Once sufficient energy is stored, perform the `perform_inference` method to analyze soil moisture and nutrient levels.
```python
result = sensor.perform_inference(soil_moisture=0.25, nutrient_levels=0.4)
print(result)
```

### **Step 4: Manage Power Consumption**
Use the `sleep_cycle` method to simulate aggressive power gating during periods of inactivity (e.g., nighttime).
```python
sensor.sleep_cycle(duration_sec=12*3600)
```

### **Step 5: Automated Action**
Based on the `Recommendation` field in the result, automate your irrigation or fertilization systems.
```python
if "Irrigation Required" in result["Recommendation"]:
    # Trigger low-power LoRa signal to irrigation pump
    pass
```

---

## **4. Troubleshooting & Best Practices**
- **Energy Budgeting:** Monitor the `Energy Remaining` to ensure the sensor does not brown out during inference.
- **Harvesting Efficiency:** Ensure solar panels are clean and oriented toward the sun for maximum daytime harvesting.
- **Sleep Optimization:** Use longer sleep cycles during periods of high moisture (e.g., after rain) to conserve stored energy.

---
**Authored by:** David Akpoviroro Oke (MrIridescent)
