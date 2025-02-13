import PyPDF2
import markdown
import re
import sys
import os

def pdf_to_text_clean(input_pdf, output_txt):
    with open(input_pdf, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        extracting = False

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                # Dynamische Erkennung von Kopf- und Fußzeilen durch Mustererkennung
                page_text = re.sub(r'(?i)(.*standard.*|.*seite.*|.*page.*|.*\d+.*)$', '', page_text)

                # Inhaltsverzeichnis anhand typischer Strukturen erkennen
                if re.search(r'(?i)inhalt|contents', page_text) and not extracting:
                    continue
                if re.search(r'\d+\.\d+\s+[A-Za-z]', page_text):
                    extracting = True  # Start extracting content after TOC

                if extracting:
                    text += page_text + "\n"

    with open(output_txt, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)
    print(f"Extracted text saved to {output_txt}")

def md_to_text(input_md, output_txt):
    with open(input_md, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()
        text = markdown.markdown(md_content)
        # Entferne HTML-Tags und Markdown-Formatierungen
        clean_text = re.sub(r'<[^>]*>', '', text)
        clean_text = re.sub(r'\n+', '\n', clean_text)  # Mehrfache Zeilenumbrüche reduzieren

    with open(output_txt, "w", encoding="utf-8") as txt_file:
        txt_file.write(clean_text)
    print(f"Markdown converted to text and saved to {output_txt}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input file>")
        sys.exit(1)

    input_file = sys.argv[1]
    file_extension = os.path.splitext(input_file)[1].lower()

    if file_extension == ".pdf":
        output_txt = input_file.replace(".pdf", ".txt")
        pdf_to_text_clean(input_file, output_txt)
    elif file_extension == ".md":
        output_txt = input_file.replace(".md", ".txt")
        md_to_text(input_file, output_txt)
    elif file_extension == ".txt":
        print("Text file provided, no processing needed.")
    else:
        print(f"Unsupported file format: {file_extension}. Skipping.")
