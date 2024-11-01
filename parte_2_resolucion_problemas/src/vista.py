class LeadsView:
    def mostrar_mensaje_inicial(self):
        print("Se han cargado los leads desde el archivo. ¿Qué filtro desea aplicar?")

    def mostrar_menu(self):
        print("\nMenú de opciones:")
        print("1. Filtrar leads por la ubicación")
        print("2. Calcular presupuesto total de leads filtrados")
        print("3. Ordenar leads filtrados por presupuesto")
        print("4. Salir")

    def obtener_opcion(self):
        return input("Seleccione una opción: ")

    def mostrar_resultados(self, leads_filtrados, total_presupuesto=None):
        print("\nLeads filtrados y ordenados:")
        print(leads_filtrados[['id', 'name', 'location', 'budget']])
        if total_presupuesto is not None:
            print(f"\nPresupuesto total de los leads filtrados: {total_presupuesto}")

    def mostrar_mensaje_despedida(self):
        print("Saliendo del programa. ¡Hasta luego!")
