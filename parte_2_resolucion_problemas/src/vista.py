class LeadsView:

    def mostrar_mensaje_inicio_carga(self):
        print("Cargando arhivo leands... Espere por favor.")
    
    def mostrar_mensaje_fin_carga(self):
        print("Se han cargado los leads desde el archivo. ¿Qué filtro desea aplicar?")

    def mostrar_menu(self):
        print("\nMenú de opciones:")
        print("1. Filtrar leads por ubicación")
        print("2. Calcular presupuesto total de leads filtrados")
        print("3. Ordenar leads filtrados por presupuesto")
        print("4. Salir")

    def mostrar_submenu_ubicaciones(self, ubicaciones):
        print("\nSeleccione una ubicación para filtrar:")
        for i, ubicacion in enumerate(ubicaciones, 1):
            print(f"{i}. {ubicacion}")
        opcion = input("Ingrese el número de la ubicación seleccionada: ")
        return ubicaciones[int(opcion) - 1] if opcion.isdigit() and 0 < int(opcion) <= len(ubicaciones) else None

    def obtener_opcion(self):
        return input("Seleccione una opción: ")

    def mostrar_resultados(self, leads_filtrados, total_presupuesto=None):

        if total_presupuesto is not None:
            print(f"\nPresupuesto total de los leads filtrados: {total_presupuesto}")
        else:
            print("\nLeads filtrados y ordenados:")
            print(leads_filtrados[['id', 'name', 'location', 'budget']])

    def mostrar_mensaje_despedida(self):
        print("Saliendo del programa. ¡Hasta luego!")
