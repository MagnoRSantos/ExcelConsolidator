# absenteeism_generator.py

from faker import Faker
import pandas as pd
import random

def generate_absenteeism_data():
    faker = Faker("pt_BR")
    
    departments = ["Recursos Humanos", "Financeiro", "Marketing", "TI", "Vendas", "Operações", "Jurídico", "Engenharia", "Atendimento ao Cliente", "P&D"]
    reasons = ["Doença", "Problemas pessoais", "Consulta médica", "Viagem de negócios", "Outros"]

    data = {
        "Colaborador_id": [faker.unique.random_number(digits=5) for _ in range(10)],
        "Colaborador_nome": [faker.name() for _ in range(10)],
        "Departamento": [faker.random_element(elements=departments) for _ in range(10)],
        "Motivo_da_ausência": [faker.random_element(elements=reasons) for _ in range(10)],
        "Horas_de_ausência": [faker.random_int(min=1, max=8) for _ in range(10)],
        "Data_da_ausência": [faker.date_between_dates(date_start=pd.to_datetime("2023-06-01"), date_end=pd.to_datetime("2023-06-30")) for _ in range(10)],
        "Salário": [round(random.uniform(2500, 12500), 2) for _ in range(10)]
    }

    df = pd.DataFrame(data)
    df['absence_date'] = pd.to_datetime(df['absence_date'])

    return df