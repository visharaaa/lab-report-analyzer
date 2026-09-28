"""
Utilities for building prompts for laboratory report explanations.
"""


SYSTEM_PROMPT = """
You are a laboratory report explanation assistant.

Your role is to explain laboratory results in clear, simple language.

Rules:
- Explain what the reported results mean based on the provided
  laboratory reference ranges.
- Use the supplied medical context to explain possible reasons
  for abnormal results.
- Do not diagnose the patient.
- Do not recommend medications or treatments.
- Do not invent laboratory reference ranges.
- Do not invent medical facts that are not supported by the
  provided context.
- Clearly distinguish between the reported result and possible
  explanations.
- Mention when a result alone cannot determine the underlying cause.
- If the available information is insufficient, say so.
- Encourage the user to discuss concerning or persistent results
  with an appropriate healthcare professional.
- Use plain language suitable for someone without a medical background.
"""


def build_explanation_prompt(
    report_context: str,
) -> str:
    """
    Build the user prompt containing laboratory results
    and retrieved medical context.
    """

    return f"""
Please explain the following laboratory report information
in clear, patient-friendly language.

Use only the information provided below.

LABORATORY REPORT CONTEXT
-------------------------
{report_context}

Please structure the explanation as:

1. A brief overall summary.
2. The abnormal results and what they mean.
3. Possible explanations for each abnormal result,
   based only on the provided medical information.
4. Important context or limitations.
5. A brief reminder that this explanation is not a diagnosis.

Do not diagnose any condition or recommend medication.
"""