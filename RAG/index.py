
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

# Get the path to nodejs.pdf
pdf_path = Path(__file__).parent / "nodejs.pdf"

# Check whether the PDF exists
if not pdf_path.is_file():
    raise FileNotFoundError(f"PDF not found: {pdf_path}")

# Load the PDF
loader = PyPDFLoader(file_path=str(pdf_path))
docs = loader.load()

print(f"Total pages: {len(docs)}")

# Print the 13th page
if len(docs) > 12:
    print(docs[12])
else:
    print("The PDF contains fewer than 13 pages.")
