#  Text Summarization NLP Project 

This project follows a modular and scalable **Machine Learning Pipeline Architecture**, widely used in production-level AI systems.

---

##  Project Workflow

The pipeline is designed in multiple stages:

```
config → entity → components → pipeline → main.py
```

---

## 📂 Pipeline Structure

### 1️⃣ Configuration (`config/`)

* Stores all project configurations
* Includes:

  * `config.yaml` → paths and directories
  * `params.yaml` → model parameters

---

### 2️⃣ Constants (`constants/`)

* Defines global file paths
* Example:

  * CONFIG_FILE_PATH
  * PARAMS_FILE_PATH

---

### 3️⃣ Entity (`entity/`)

* Contains dataclasses
* Defines structure of configuration objects

---

### 4️⃣ Components (`components/`)

* Core logic of each pipeline stage
* Example modules:

  * Data Ingestion
  * Data Validation
  * Data Transformation
  * Model Trainer

---

### 5️⃣ Pipeline (`pipeline/`)

* Controls execution of each stage
* Each stage is implemented separately:

  * stage_01_data_ingestion.py
  * stage_02_data_validation.py
  * etc.

---

### 6️⃣ Utils (`utils/`)

* Common reusable functions
* Example:

  * read_yaml()
  * create_directories()
  * save_json()

---

### 7️⃣ Logging (`logging/`)

* Handles logging across the project
* Tracks pipeline execution

---

### 8️⃣ Main Entry Point (`main.py`)

* Runs the complete pipeline
* Controls execution order

---

## 🔄 Pipeline Flow

1. Read configuration from YAML files
2. Create required directories
3. Perform data ingestion
4. Validate and transform data
5. Train model using HuggingFace Transformers
6. Evaluate model performance
7. Save outputs and logs

---

## 📦 Artifacts Generated

* Data files
* Trained model
* Logs
* Evaluation metrics

All outputs are stored in the `artifacts/` directory.

---

## 🛠️ Tech Stack

* Python
* NLP (HuggingFace Transformers)
* YAML Configuration
* Modular ML Pipeline Design

---

## 💡 Key Highlights

* Scalable architecture
* Industry-standard pipeline
* Easy to extend and maintain
* Suitable for MLOps deployment

---

## 🚀 How to Run

```bash
python main.py
```

---

## 📌 Future Enhancements

* Model deployment using Flask / FastAPI
* CI/CD integration
* Docker containerization
* Cloud deployment (AWS/GCP)
