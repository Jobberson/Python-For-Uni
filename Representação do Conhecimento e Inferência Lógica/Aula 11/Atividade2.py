# Crie um sistema de automação residencial usando Python e a biblioteca rule_engine. Utilize a base
# de dados ao lado, que representa sensores e estados de dispositivos em uma casa inteligente.
# Para cada cômodo, aplique as regras abaixo e informe as ações recomendadas.
#
# Regras:
# Ligar luz automaticamente: o nível de luminosidade está abaixo de 300 lux e o cômodo está ocupado.
# Ativar ventilação: a temperatura do ambiente está acima de 28 °C.
# Desligar ar-condicionado: o cômodo está vazio ou a temperatura está abaixo de 22 °C.
# Fechar persianas: o nível de luminosidade é maior que 800 lux e o cômodo está ocupado.
# Enviar alerta de segurança: movimento detectado em cômodo com alarme ativado.
# Ativar economia de energia: o cômodo está vazio por mais de 30 minutos e há dispositivos ligados.

import pandas as pd        # for tabular data handling
import rule_engine         # for writing & evaluating human-readable rules

# Room dictionary
rooms = [
    {
        "name": "Room A",
        "temperature": 29.5,
        "illumination": 250,
        "presence": True,
        "projector_on": True,
        "minutes_no_presence": 0,
        "window_open": False,
        "alarm_enabled": False,
    },
    {
        "name": "Room B",
        "temperature": 21.0,
        "illumination": 950,
        "presence": False,
        "projector_on": True,
        "minutes_no_presence": 45,
        "window_open": True,
        "alarm_enabled": False,
    },
    {
        "name": "Room C",
        "temperature": 26.3,
        "illumination": 500,
        "presence": True,
        "projector_on": False,
        "minutes_no_presence": 0,
        "window_open": False,
        "alarm_enabled": False,
    },
    {
        "name": "Room D",
        "temperature": 30.2,
        "illumination": 860,
        "presence": False,
        "projector_on": False,
        "minutes_no_presence": 70,
        "window_open": True,
        "alarm_enabled": True,
    },
]

# Dataframe creation
df = pd.DataFrame(rooms)

# Rules dictionary
rules = {
    "Turn on light":            "illumination < 300 and presence",
    "Activate ventilation":     "temperature > 28",
    "Turn off AC":              "not presence or temperature < 22",
    "Close blinds":             "illumination > 800 and presence",
    "Send security alert":      "presence and alarm_enabled",
    "Activate energy saving":   "minutes_no_presence > 30 and projector_on",
}

# Compile each rule into an object
compiled_rules = {
    action: rule_engine.Rule(expr)
    for action, expr in rules.items()
}

# Function to evaluate rules for each room
def get_recommended_actions(room_record):
    """
    room_record: dict with keys matching our rule definitions
    returns: list of action names whose rule evaluated to True
    """
    actions = []
    for action_name, compiled in compiled_rules.items():
        if compiled.matches(room_record):
            actions.append(action_name)
    return actions

# Apply to every room in DataFrame
df["recommended_actions"] = df.apply(get_recommended_actions, axis=1)

# Print results
for _, row in df.iterrows():
    name = row["name"]
    actions = row["recommended_actions"]
    if actions:
        print(f"{name}:")
        for act in actions:
            print(f"  - {act}")
    else:
        print(f"{name}: No actions recommended.")
