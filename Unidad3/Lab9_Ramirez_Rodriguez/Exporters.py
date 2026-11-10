import csv
import json
from fpdf import FPDF

class Exportador:
    def exportar(self, datos, ruta_archivo):
        """Método que debe ser sobrescrito por las clases hijas"""
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

class ExportadorTXT(Exportador):
    def exportar(self, datos, ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for producto in datos:
                # Ajustar los índices según cómo su Modelo retorna los datos de la BD
                file.write(f"ID: {producto[0]} | Nombre: {producto[1]} | Precio: ${producto[2]}\n")
        print(f"Archivo TXT generado en: {ruta_archivo}")

# TODO: Implementar ExportadorCSV (heredando de Exportador)
class CSVexporter(Exportador):
    def export(self, datos, ruta_archivo):
        with open(ruta_archivo, 'w', newline = '', econding= 'utf-8') as f:
            writer = csv.writer(f)
            writer.writerow('ID', 'PRODUCT', 'STOCK')
            writer.writerows(datos)
# TODO: Implementar ExportadorJSON (heredando de Exportador)
class JSONexporter(Exportador):
    def export(self, datos_f, ruta_archivo):
        datos_f=({"id": p[0], "product": p[1], "price": p[2], "stock": p[3]} for p in datos_f)
        with open(ruta_archivo, 'w', newline = '', econding= 'utf-8') as f:
            json.dump(datos_f, f, indent=4, ensuer_ascii=False)



class ExportadorPDF(Exportador):
    def exportar(self, datos, ruta_archivo):
        pdf = FPDF()
        pdf.add_page()
        
        # Configuración del título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Reporte de Inventario de Productos", ln=True, align='C')
        
        # Salto de línea
        pdf.ln(10)
        
        # Configuración del cuerpo del documento
        pdf.set_font("Arial", size=12)
        
        for producto in datos:
            # Reemplazar producto[1], producto[2], etc., según la estructura de sus datos
            texto_linea = f"Producto: {producto[1]} - Precio: ${producto[2]}"
            pdf.cell(200, 10, txt=texto_linea, ln=True)
            
        pdf.output(ruta_archivo)
        print(f"Archivo PDF generado en: {ruta_archivo}")
