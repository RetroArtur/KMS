import sys
import os
import json
import requests
import time

def download_pdfs(json_path, download_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        print("Öffne Json")
        zotero_data = json.load(file)

    if not os.path.exists(download_path):
        print("Erstelle Ordner")
        os.makedirs(download_path)
        print("Pfad erstellt unter"+ download_path)

    for entry in zotero_data:
        if 'URL' in entry:
            pdf_url = entry['URL']
            pdf_title = entry.get('title', 'unknown')
            pdf_path = os.path.join(download_path, pdf_title)

            if os.path.exists(pdf_path):
                print(f"Datei bereits vorhanden, wird übersprungen: {pdf_path}")
                continue            
            print(f"Downloading: {pdf_url}")
            response = requests.get(pdf_url, stream=True)
            if response.status_code == 200:
                with open(pdf_path, 'wb') as pdf_file:
                    for chunk in response.iter_content(chunk_size=8192):
                        pdf_file.write(chunk)
                print(f"Saved: {pdf_path}")
            else:
                print(f"Failed to download {pdf_url}")
            time.sleep(60)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python download_zotero_pdfs.py <zotero_json_path> <download_directory>")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    download_dir = sys.argv[2]

    download_pdfs(json_file_path, download_dir)

 ## cmd == python3 pull_zotero.py KMS.json .