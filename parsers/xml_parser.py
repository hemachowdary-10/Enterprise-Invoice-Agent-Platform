import lxml.etree as ET

def parse_xml(path):

    tree = ET.parse(path)
    root = tree.getroot()

    invoice = {}

    invoice["invoice_number"] = root.findtext(".//InvoiceNumber")
    invoice["total"] = root.findtext(".//TotalAmount")

    return invoice