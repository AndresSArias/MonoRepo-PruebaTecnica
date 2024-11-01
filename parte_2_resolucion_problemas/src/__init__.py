
from src.modelo import LeadsModel
from src.vista import LeadsView
from src.controlador import LeadsController

def create_app():

    modelo = LeadsModel()
    vista = LeadsView()

    return LeadsController(modelo, vista)
