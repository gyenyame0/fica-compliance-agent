from utils.validators import validate_id, validate_por

def check_compliance(data):
    id_valid = validate_id(data["id_text"])
    por_valid = validate_por(data["por_text"])

    summary = {
        "ID Valid": id_valid,
        "Proof of Residence Valid": por_valid
    }
    is_compliant = id_valid and por_valid

    return summary, is_compliant
