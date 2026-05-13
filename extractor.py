import os
import requests
from bs4 import BeautifulSoup

# Data extraction from .txt file 
def from_txt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# From PDF
def from_pdf(file_path: str) -> str:
    import PyPDF2
    text = ''
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

# From Word DOCX file
def from_docx(file_path: str) -> str:
    import docx
    doc = docx.Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

# From Website
def from_website(url: str) -> str:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html_parser')
    for tag in soup(['nav', 'footer', 'script', 'style']):
        tag.decompose()
    text = soup.get_text(separator='\n')
    text = 'n'.join(line.strip() for line in splitlines() if line.strip())
    return text[:3000]


def load_all(knowledge_folder: str = 'knowledge', website_url: str = None) -> str:
    """
    Reads everything from knowledege folder automatically.
    Supports .txt, .pdf, .docx files.
    Optionally scrapes a website too.
    All text is combined into one string.
    """
    all_text = ""

    # Read all files in knowledge folder
    if os.path.exists(knowledge_folder):
        for filename in os.listdir(knowledge_folder):
            filepath = os.path.join(knowledge_folder, filename)
            print(f"Loading: {filename}")

            if filename.endswith('.txt'):
                all_text += from_txt(filepath) + '\n'
            elif filename.endswith('.pdf'):
                all_text += from_pdf(filepath) + '\n'
            elif filename.endswith('.docx'):
                all_text += from_docx(filepath) + '\n'
            else:
                print(f"Skipping unsupported file: {filename}")

    # Optionally add website content
    if website_url:
        print(f"Loading website: {website_url}")
        all_text += from_website(website_url) + '\n'

    print(f"✅ Total knowledge loaded: {len(all_text)} characters")
    return all_text


