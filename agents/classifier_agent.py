import mimetypes

def classify(file_path):
    mime,_ = mimetypes.guess_type(file_path)

    if mime == "application/pdf":
        return "pdf"
    if mime in ["image/png","image/jpeg"]:
        return "image"
    if mime == "text/xml":
        return "xml"
    if mime == "text/csv":
        return "csv"

    return "unknown"