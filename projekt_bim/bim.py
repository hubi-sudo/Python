import ifcopenshell
import ifcopenshell.util.element

file_path = "ifc.ifc"
model = ifcopenshell.open(file_path)

#1: Analiza okien
print("\n")
windows = model.by_type("IfcWindow")

for window in windows:
    name = window.Name if window.Name else "Brak nazwy"
    tag = window.Tag if window.Tag else "Brak tagu"
    psets = ifcopenshell.util.element.get_psets(window)
    ilosc_zbiorow = len(psets)

    if ilosc_zbiorow > 0:
        nazwa_psetu = list(psets.keys())[0]
        print(f"-> Okno: {name} | Tag: {tag} | Znaleziono zestawy danych: {ilosc_zbiorow} (np. {nazwa_psetu})")
    else:
        print(f"-> Okno: {name} | Brak dodatkowych danych PropertySet")

#2: Analiza ścian
print("\n")
walls = model.by_type("IfcWall")

for wall in walls:
    psets = ifcopenshell.util.element.get_psets(wall)
    czy_zewnetrzna = False

    # slownik
    for pset_name, properties in psets.items():
        if properties.get("IsExternal") == True:
            czy_zewnetrzna = True

    if czy_zewnetrzna:
        print(f"-> Zidentyfikowano ścianę zewnętrzną: {wall.Name} (ID: {wall.GlobalId})")

#3: Relacje przestrzenne
print("\n")
relacje_przestrzenne = model.by_type("IfcRelContainedInSpatialStructure")

for rel in relacje_przestrzenne:
    kondygnacja = rel.RelatingStructure
    elementy = rel.RelatedElements
    licznik_scian = 0

    for el in elementy:
        if el.is_a("IfcWall"):
            licznik_scian += 1

    if len(elementy) > 0:
        print(f"Kondygnacja '{kondygnacja.Name}' zawiera {len(elementy)} elementy, w tym {licznik_scian} ścian.")
