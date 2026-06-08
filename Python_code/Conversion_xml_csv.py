 import xml.etree.ElementTree as ET
import pandas as pd

def parse_element(element, prefix=""):
    
    #Convierte etiquetas anidadas en un diccionario plano
    
    data = {}

    for child in element:
        tag = f"{prefix}{child.tag}"

        # Caso 1: texto simple
        if len(child) == 0:
            data[tag] = child.text if child.text else ""
        else:
            # Caso 2: elemento anidado → llamada recursiva
            data.update(parse_element(child, prefix=f"{tag}_"))

    return data


def xml_to_table(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    rows = []

    for residuo in root.findall(".//Residuo"):
        row = parse_element(residuo)
        rows.append(row)

    return pd.DataFrame(rows)


df = xml_to_table("residuos.xml") #archivo .xml 

# Exportar a CSV
df.to_csv("residuos_prtr.csv", index=False, encoding="utf-8")

# Exportar a Excel
df.to_excel("residuos_prtr.xlsx", index=False)
