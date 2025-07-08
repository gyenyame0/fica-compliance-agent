def str_drafting_prompt(summary):
    return f"""
You are a compliance officer drafting a Suspicious Transaction Report (STR).
Use the following summary of a FICA client onboarding:

{summary}

Write a concise, formal STR explaining why this case is non-compliant and suspicious.
"""
