from utils.extract_text import extract_text_from_pdf

def extract_data_from_docs(id_doc, por_doc):
    id_text = extract_text_from_pdf(id_doc)
    por_text = extract_text_from_pdf(por_doc)

    return {
        "id_text": id_text,
        "por_text": por_text
    }
