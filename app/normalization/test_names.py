"""
Maps different laboratory test names to standardized canonical names.
"""

TEST_NAME_MAP = {
    # CBC
    "hb": "hemoglobin",
    "hgb": "hemoglobin",
    "haemoglobin": "hemoglobin",
    "hemoglobin": "hemoglobin",

    "rbc": "rbc_count",
    "rbc count": "rbc_count",
    "red blood cell count": "rbc_count",

    "wbc": "wbc_count",
    "wbc count": "wbc_count",
    "white blood cell count": "wbc_count",

    "platelets": "platelet_count",
    "platelet count": "platelet_count",
    "plt": "platelet_count",

    "hct": "hematocrit",
    "hematocrit": "hematocrit",
    "pcv": "hematocrit",

    "mcv": "mcv",
    "mch": "mch",
    "mchc": "mchc",
    "rdw": "rdw",

    "neutrophils": "neutrophils",
    "neutrophil": "neutrophils",

    "lymphocytes": "lymphocytes",
    "lymphocyte": "lymphocytes",

    "monocytes": "monocytes",
    "monocyte": "monocytes",

    "eosinophils": "eosinophils",
    "eosinophil": "eosinophils",

    "basophils": "basophils",
    "basophil": "basophils",

    # Blood glucose
    "fbs": "fasting_blood_glucose",
    "fbG": "fasting_blood_glucose",
    "fasting blood glucose": "fasting_blood_glucose",
    "fasting blood sugar": "fasting_blood_glucose",

    "rbs": "random_blood_glucose",
    "random blood glucose": "random_blood_glucose",
    "random blood sugar": "random_blood_glucose",

    "ppbs": "postprandial_blood_glucose",
    "ppbg": "postprandial_blood_glucose",
    "postprandial blood glucose": "postprandial_blood_glucose",
    "postprandial blood sugar": "postprandial_blood_glucose",

    # HbA1c
    "hba1c": "hba1c",
    "hb a1c": "hba1c",
    "glycated hemoglobin": "hba1c",
    "glycosylated hemoglobin": "hba1c",
}


def normalize_test_name(test_name: str) -> str | None:
    """
    Convert a laboratory test name into its canonical name.

    Returns None if the test name is not recognized.
    """

    normalized = test_name.strip().lower()

    return TEST_NAME_MAP.get(normalized)