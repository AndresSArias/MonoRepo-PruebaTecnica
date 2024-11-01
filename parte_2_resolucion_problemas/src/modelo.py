import pandas as pd

from utils.constants import FILE_PATH_LEADS

class LeadsModel:
    def __init__(self):
        self.leads_df = pd.read_csv(FILE_PATH_LEADS)

    def filtrar_por_ubicacion(self, location="Medellín"):
        return self.leads_df[self.leads_df['location'] == location]

    def calcular_presupuesto_total(self, leads_filtrados):
        return leads_filtrados['budget'].sum()

    def ordenar_por_presupuesto(self, leads_filtrados):
        return leads_filtrados.sort_values(by='budget', ascending=False)
