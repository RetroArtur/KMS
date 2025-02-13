import os
import time
import sys
import subprocess

watch_directory = "/data/shared/Exports"
processed_files = set()

def process_file(file_path):
    if file_path.endswith(('.pdf', '.md', '.txt')):
        print(f"Processing file: {file_path}")
        
        subprocess.run(["python3", "/data/shared/Exports/pdf_to_text.py", file_path], check=True)

while True:
    for file_name in os.listdir(watch_directory):
        file_path = os.path.join(watch_directory, file_name)
        if file_name not in processed_files and os.path.isfile(file_path):
            process_file(file_path)
            processed_files.add(file_name)
    time.sleep(10)  # Prüfe alle 10 Sekunden auf neue Dateien
