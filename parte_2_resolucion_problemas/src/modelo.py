class LeadsModel:
    def __init__(self):
        self._leads_df = None

    @property
    def leads_df(self):
        return self._leads_df
    
    @leads_df.setter
    def leads_df(self, nuevo_leads_df):
        self._leads_df = nuevo_leads_df

    def obtener_ubicaciones_unicas(self):
        # Obtener una lista de ubicaciones únicas
        return self.leads_df['location'].unique()

    def filtrar_por_ubicacion(self, location):
        # Filtrar los leads según la ubicación proporcionada
        return self.leads_df[self.leads_df['location'] == location]

    def calcular_presupuesto_total(self, leads_filtrados):
        # Calcular el presupuesto total de los leads filtrados
        return leads_filtrados['budget'].sum()

    def ordenar_por_presupuesto(self, leads_filtrados):
        # Ordenar los leads filtrados por presupuesto en orden descendente
        return leads_filtrados.sort_values(by='budget', ascending=False)
