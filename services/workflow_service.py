import os

from agents.classifier_agent import classify
from agents.extraction_agent import extract
from agents.validation_agent import validate
from agents.fraud_agent import detect
from agents.erp_agent import post_to_erp

from parsers.pdf_parser import parse_pdf
from parsers.image_parser import parse_image
from parsers.xml_parser import parse_xml
from parsers.csv_parser import parse_csv


def process_invoice(file_path):

    file_type = classify(file_path)

    print("Detected:",file_type)

    if file_type == "pdf":
        text = parse_pdf(file_path)

    elif file_type == "image":
        text = parse_image(file_path)

    elif file_type == "xml":
        invoice = parse_xml(file_path)
        text = str(invoice)

    elif file_type == "csv":
        invoice = parse_csv(file_path)
        text = str(invoice)

    else:
        print("Unsupported format")
        return

    invoice = {"total":1000}  # simplified placeholder

    status = validate(invoice)
    fraud = detect(invoice)

    print("Validation:",status)
    print("Fraud:",fraud)

    if status == "approved" and fraud == "clear":
        post_to_erp(invoice)


def run_pipeline():

    folder="sample_invoices"

    for file in os.listdir(folder):

        path=os.path.join(folder,file)

        process_invoice(path)


if __name__ == "__main__":

    run_pipeline()