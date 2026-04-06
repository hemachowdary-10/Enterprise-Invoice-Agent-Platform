# Enterprise Agentic Invoice Platform

Supports PDF, images, XML and CSV invoices using multiple AI agents.

## Run Instructions

1. Install prerequisites
- Docker
- Python 3.10+

2. Start infrastructure

docker compose up -d

3. Install python dependencies

pip install -r requirements.txt

4. Run pipeline

python services/workflow_service.py

5. Place invoices inside:

sample_invoices/

Example XML invoice already included.