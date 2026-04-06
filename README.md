# 🧠 Enterprise Agentic Invoice Platform

An AI-powered, multi-agent system that processes invoices from **PDF, images, XML, and CSV formats**, extracts structured data, and integrates seamlessly into a modern data platform for logistics and financial analytics.

---

## 📌 Overview

This project implements an **Agentic AI workflow** that:

* Ingests invoices in multiple formats
* Uses intelligent agents to extract structured information
* Outputs normalized JSON data
* Integrates with downstream data pipelines (Snowflake, dbt, BI tools)

This system is designed to be a **plug-and-play financial ingestion layer** within a larger **real-time logistics analytics platform**.

---

## 🧠 Key Capabilities

* 📄 Multi-format invoice support:

  * PDF
  * Images (OCR-based)
  * XML
  * CSV
* 🤖 Multi-agent processing pipeline:

  * Parsing agent
  * Extraction agent
  * Validation agent
* 🔄 Automated workflow execution
* 📦 Structured JSON output for downstream systems
* 🐳 Fully containerized with Docker

---

## 🏗️ Architecture (Invoice Processing Layer)

```id="f5zj7y"
Input Invoices (PDF / Image / XML / CSV)
        |
        |  Agentic Workflow Engine
        v
Multi-Agent Processing
        |
        |  Structured Extraction
        v
JSON Output
        |
        v
Downstream Data Platform (Snowflake / dbt / BI)
```

---

## 🔗 Role in End-to-End Data Platform

This repository represents the **AI ingestion layer** in a larger system:

```id="f91nq1"
Real-Time Logistics Data (Streaming)
        |
        v
Snowflake (Operational Data)

+
        |
        v
Agentic Invoice Platform (THIS REPO)
        |
        v
Structured Financial Data

→ Combined in Analytics Layer → BI Dashboards
```

---

## 📂 Project Structure

```id="w3zx0c"
.
├── services/
│   └── workflow_service.py   # Main orchestration entry point
├── sample_invoices/          # Sample input files
├── docker-compose.yml        # Infrastructure setup
├── requirements.txt          # Python dependencies
└── README.md
```

---

## ▶️ Getting Started

### 1. Clone Repository

```bash id="bcmc0f"
git clone https://github.com/hemachowdary-10/Enterprise-Invoice-Agent-Platform.git
cd Enterprise-Invoice-Agent-Platform
```

---

### 2. Start Infrastructure

```bash id="0h9xbm"
docker compose up -d
```

---

### 3. Install Python Dependencies

```bash id="u2bq1d"
pip install -r requirements.txt
```

---

### 4. Add Sample Invoices

Place your files inside:

```id="l3pq2g"
sample_invoices/
```

Supported formats:

* `.pdf`
* `.png`, `.jpg`
* `.xml`
* `.csv`

---

### 5. Run the Pipeline

```bash id="l1q4kc"
python services/workflow_service.py
```

---

## 📤 Output

The system processes invoices and produces:

* Structured JSON output
* Extracted fields such as:

  * invoice_id
  * vendor
  * amount
  * currency
  * invoice_date
  * line items (if available)

This output can be:

* Stored locally
* Sent to cloud storage (GCS)
* Loaded into Snowflake for analytics

---

## 🔄 Integration with Data Platform (Recommended)

To integrate this system into a modern data stack:

1. Save JSON outputs to:

```id="b6q2sq"
data/invoices/
```

2. Load into Snowflake:

```id="u33vlw"
RAW.INVOICES
```

3. Transform using dbt:

* Clean fields
* Join with shipment data
* Build cost analytics models

---

## 📊 Example Use Cases

* 💰 Invoice cost analysis
* 🚚 Shipment vs cost correlation
* ⚠️ High-cost shipment detection
* 📉 Carrier performance benchmarking
* 🧾 Automated financial ingestion

---

## 🚀 Future Enhancements

* LLM-based anomaly detection
* Fraud detection for invoices
* Confidence scoring for extracted fields
* Integration with real-time pipelines (Pub/Sub, IICS)
* Automated reconciliation with logistics data

---

## 🤝 Contributing

Contributions are welcome. Please open an issue to discuss proposed changes.

---

