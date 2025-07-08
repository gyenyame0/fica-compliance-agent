from agents.file_processor import extract_data_from_docs
from agents.compliance_checker import check_compliance
from agents.str_generator import generate_str

def run_full_pipeline(id_doc, por_doc):
    extracted = extract_data_from_docs(id_doc, por_doc)
    summary, is_compliant = check_compliance(extracted)

    if not is_compliant:
        str_report = generate_str(summary)
        status = "❌ Non-Compliant. STR generated."
    else:
        str_report = "No suspicious activity detected."
        status = "✅ All documents are compliant."

    return {
        "status": status,
        "summary": summary,
        "str_draft": str_report
    }
