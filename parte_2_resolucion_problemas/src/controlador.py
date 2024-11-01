from src.modelo import LeadsModel
from src.vista import LeadsView
from src.utils.constants import FILE_PATH_LEADS

from time import sleep
import pandas as pd



class LeadsController:
    def __init__(self, modelo:LeadsModel, vista:LeadsView):
        self.modelo = modelo
        self.vista = vista
        self.leads_filtrados = None

    def run(self):
        self.vista.mostrar_mensaje_inicio_carga()
        self.modelo.leads_df = pd.read_csv(FILE_PATH_LEADS)
        sleep(2)
        self.vista.mostrar_mensaje_fin_carga()
        sleep(3)
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.obtener_opcion()

            if opcion == "1":
                ubicaciones = self.modelo.obtener_ubicaciones_unicas()
                sleep(2)
                ubicacion_seleccionada = self.vista.mostrar_submenu_ubicaciones(ubicaciones)
                sleep(3)
                if ubicacion_seleccionada:
                    self.leads_filtrados = self.modelo.filtrar_por_ubicacion(ubicacion_seleccionada)
                    print(f"Leads filtrados por ubicación '{ubicacion_seleccionada}'.")
                    sleep(2)
                    self.vista.mostrar_resultados(self.leads_filtrados)
                    sleep(3)
                else:
                    print("Selección no válida. Vuelva a intentarlo")
                    sleep(3)

            elif opcion == "2":
                if self.leads_filtrados is None:
                    sleep(2)
                    print("Primero debe filtrar los leads por ubicación.")
                    sleep(3)
                else:
                    total_presupuesto = self.modelo.calcular_presupuesto_total(self.leads_filtrados)
                    sleep(2)
                    print("Presupuesto total calculado.")
                    sleep(2)
                    self.vista.mostrar_resultados(self.leads_filtrados, total_presupuesto=total_presupuesto)
                    sleep(3)
            elif opcion == "3":
                if self.leads_filtrados is None:
                    sleep(2)
                    print("Primero debe filtrar los leads por ubicación.")
                    sleep(3)
                else:
                    self.leads_filtrados = self.modelo.ordenar_por_presupuesto(self.leads_filtrados)
                    sleep(2)
                    print("Leads ordenados por presupuesto.")
                    sleep(2)
                    self.vista.mostrar_resultados(self.leads_filtrados)
                    sleep(3)

            elif opcion == "4":
                sleep(2)
                self.vista.mostrar_mensaje_despedida()
                sleep(3)
                break

            else:
                sleep(2)
                print("Opción no válida. Intente de nuevo.")
                sleep(3)
