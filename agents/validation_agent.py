def validate(invoice):

    if float(invoice.get("total",0)) > 50000:
        return "manual_review"

    return "approved"