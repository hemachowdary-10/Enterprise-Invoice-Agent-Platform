import requests

def extract(text):

    prompt = f'''
Extract invoice fields:
vendor
invoice_number
total
invoice_date
Return JSON
'''

    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"llama3",
            "prompt":prompt + text
        }
    )

    return r.json()