from langchain.document_loaders import  PyPDFLoader

## PDF Loader

def pdf_loader(path):
    loader = PyPDFLoader(path)
    pages=loader.load()
    content=''
    for page in pages:
        content.join(page.page_content[:])
    return content

