# Crie um sistema de apoio ao diagnóstico médico usando Python e a biblioteca rule_engine.
# Use a base de dados ao lado. Para cada paciente, aplique as regras abaixo e informe os
# diagnósticos identificados:
#
# ● Gripe forte: o paciente apresenta temperatura superior a 38 °C, tosse e falta de ar.
# ● Risco cardiovascular: o paciente tem frequência cardíaca acima de 100 bpm e idade superior a 50 anos.
# ● Febre simples: o paciente tem temperatura entre 37.5 °C e 38 °C e não apresenta tosse.
# ● Cefaleia: o paciente apresenta dor de cabeça e temperatura abaixo de 37.5 °C.
# ● Caso crítico: o paciente tem temperatura superior a 39 °C ou apresenta falta de ar com frequência  cardíaca acima de 110 bpm.
# ● Suspeita de virose: o paciente relata sintomas como náusea ou diarreia.

import pandas as pd
import rule_engine as RuleEngine
# eu não consegui instalar e importar a biblioteca rule_engine nem a pandas, então não consegui rodar o código

# dictionary of patients
patients = [
    {
        "name": "Carlos",
        "age": 55,
        "temperature": 37.8,
        "cough": False,
        "shortness_of_breath": False,
        "headache": False,
        "heart_rate": 98,
        "symptoms": ["diarrhea"]
    },
    {
        "name": "Ana",
        "age": 32,
        "temperature": 38.5,
        "cough": True,
        "shortness_of_breath": True,
        "headache": False,
        "heart_rate": 95,
        "symptoms": ["nausea"]
    },
    {
        "name": "Marcos",
        "age": 67,
        "temperature": 36.7,
        "cough": False,
        "shortness_of_breath": False,
        "headache": True,
        "heart_rate": 105,
        "symptoms": ["weakness", "back pain"]
    },
    {
        "name": "Juliana",
        "age": 45,
        "temperature": 39.2,
        "cough": True,
        "shortness_of_breath": False,
        "headache": True,
        "heart_rate": 88,
        "symptoms": ["muscle pain", "chills"]
    },
    {
        "name": "Fernanda",
        "age": 60,
        "temperature": 37.0,
        "cough": False,
        "shortness_of_breath": True,
        "headache": False,
        "heart_rate": 115,
        "symptoms": ["diarrhea"]
    },
]

# dataframe to manulate the whole table at once
df = pd.DataFrame(patients)

# dictionary of rules
rules = {
    "Severe Flu":            "temperature > 38 and cough and shortness_of_breath",
    "Cardiac Risk":          "heart_rate > 100 and age > 50",
    "Mild Fever":            "temperature >= 37.5 and temperature <= 38 and not cough",
    "Headache (Cefalea)":    "headache and temperature < 37.5",
    "Critical Case":         "temperature > 39 or (shortness_of_breath and heart_rate > 110)",
    "Suspected Viral Infection":  "'nausea' in symptoms or 'diarrhea' in symptoms",
}

# Compile each rule into an object
compiled_rules = {name: RuleEngine.Rule(expr) for name, expr in rules.items()}

# Define a function to apply the rules to each patient
def get_diagnoses(patient):
    diagnoses = []
    for name, rule in compiled_rules.items():
        # rule.matches accepts either an object with attributes or a dict
        if rule.matches(patient):
            diagnoses.append(name)
    return diagnoses

# Apply to every row in the DataFrame
df["diagnoses"] = df.apply(get_diagnoses, axis=1)

# Print the DataFrame with the diagnoses
print(df[["name", "diagnoses"]])

#  chat gpt disse que esse é o output
#       name                   diagnoses
# 0    Carlos      ['Suspected Viral Infection']
# 1       Ana  ['Severe Flu', 'Suspected Viral Infection']
# 2    Marcos  ['Cardiac Risk', 'Headache (Cefalea)']
# 3   Juliana        ['Severe Flu', 'Critical Case']
# 4  Fernanda    ['Cardiac Risk', 'Suspected Viral Infection']
