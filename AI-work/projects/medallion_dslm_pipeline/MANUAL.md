# **Technical Manual: Medallion DSLM Generation Pipeline**
**Creator / Programmer:** David Akpoviroro Oke (MrIridescent - The Creative Renaissance Man)

---

## **1. Introduction**
The **Medallion DSLM Generation Pipeline** is an automated framework for transforming raw data into specialized Domain-Specific Language Models (DSLMs). This manual provides a simplified guide for developers to initialize and operate the pipeline.

---

## **2. Installation & Prerequisites**

### **System Requirements**
- **Python 3.10+**
- **Operating System:** Linux, macOS, or Windows 11.
- **Hardware:** 8GB RAM minimum; 32GB+ for large-scale Bronze-to-Gold refinement.

### **Setup Instructions**
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/MrIridescent/Future-Proofing.git
    cd Future-Proofing/projects/medallion_dslm_pipeline
    ```
2.  **Run the Setup Script:**
    ```bash
    bash setup.sh
    ```
3.  **Execute the Test Run:**
    ```bash
    python3 medallion_pipeline.py
    ```

---

## **3. Step-by-Step Operation Guide**

### **Step 1: Initialize the Pipeline**
Create an instance of the `MedallionDSLMPipeline` with the name of your target model (e.g., "Fin-Compliance-7B").
```python
pipeline = MedallionDSLMPipeline("Model-Name")
```

### **Step 2: Bronze Ingestion (Raw Data)**
Pass your raw data list (text, JSON, or SQL logs) into the `ingest_bronze` method. This layer saves the data in its original form for auditability.
```python
bronze_file = pipeline.ingest_bronze(raw_reports)
```

### **Step 3: Silver Refinement (Cleaning & Validation)**
Invoke the `refine_silver` method to clean, normalize, and validate the data. This step handles null values and noise filtering.
```python
silver_file = pipeline.refine_silver(bronze_file)
```

### **Step 4: Gold Specialization (DSLM-Ready Data)**
Transform the cleaned data into specialized intelligence by adding reasoning paths (CoT) and expert logic.
```python
gold_file = pipeline.specialize_gold(silver_file)
```

### **Step 5: Training & Deployment**
Use the resulting Gold dataset to fine-tune your DSLM using techniques like LoRA or QLoRA via frameworks like Ray or PEFT.

---

## **4. Troubleshooting & Best Practices**
- **Data Lineage:** Always retain the Bronze layer files to comply with AI audit regulations.
- **Schema Validation:** Customize the `refine_silver` method to enforce your specific domain's data schema.
- **Scale:** For datasets exceeding 100GB, integrate with **Ray Federated** for distributed processing.

---
**Authored by:** David Akpoviroro Oke (MrIridescent)
