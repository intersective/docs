import os
from PyPDF2 import PdfReader

PDF_PATH = os.path.join('faq', 'incident-report.pdf')
MD_PATH = os.path.join('faq', 'incident-report-internal.md')


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = []
    for page in reader.pages:
        text.append(page.extract_text() or "")
    return "\n".join(text)


def summarize_text(text, max_words=500):
    words = text.split()
    summary = " ".join(words[:max_words])
    if len(words) > max_words:
        summary += "..."
    return summary


def main():
    if not os.path.exists(PDF_PATH):
        print(f"PDF file not found: {PDF_PATH}")
        return
    text = extract_text_from_pdf(PDF_PATH)
    if not text.strip():
        print("No text extracted from PDF.")
        return
    summary = summarize_text(text)
    md_content = f"# Incident Report Summary\n\n{summary}\n"
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Summary written to {MD_PATH}")


if __name__ == "__main__":
    main() 