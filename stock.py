import csv

productos = [
    # comida perro
    {"nombre": "Croquetas para Perro", "imagen": "img_croquetas_perro.jpg", "descripcion": "Croquetas nutritivas para perros adultos", "tipo_animal": "Perro", "marca": "Ricocan"},
    {"nombre": "Alimento Balanceado para Perro", "imagen": "img_alimento_perro.jpg", "descripcion": "Alimento completo y equilibrado para perros", "tipo_animal": "Perro", "marca": "Mimaskot"},
    {"nombre": "Dog Chow Premium", "imagen": "img_dog_chow.jpg", "descripcion": "Alimento premium para perros de todas las edades", "tipo_animal": "Perro", "marca": "Dog Chow"},
    {"nombre": "Pedigree Adultos", "imagen": "img_pedigree.jpg", "descripcion": "Alimento sabroso y nutritivo para perros adultos", "tipo_animal": "Perro", "marca": "Pedigree"},
    # comida gato
    {"nombre": "Whiskas para Gatos", "imagen": "img_whiskas_gatos.jpg", "descripcion": "Comida húmeda para gatos con sabor a carne", "tipo_animal": "Gato", "marca": "Whiskas"},
    {"nombre": "Royal Canin Gatos", "imagen": "img_royal_canin_gatos.jpg", "descripcion": "Alimento seco para gatos con necesidades específicas", "tipo_animal": "Gato", "marca": "Royal Canin"},
    {"nombre": "Purina Gourmet Gold", "imagen": "img_purina_gatos.jpg", "descripcion": "Comida gourmet para gatos exigentes", "tipo_animal": "Gato", "marca": "Purina"},
    # comida tortuga 
    {"nombre": "Alimento para Tortuga", "imagen": "img_alimento_tortuga.jpg", "descripcion": "Pellets nutritivos para tortugas acuáticas", "tipo_animal": "Tortuga", "marca": "Tetra"},
    {"nombre": "Sera Turtle Granules", "imagen": "img_sera_tortuga.jpg", "descripcion": "Alimento completo en gránulos para tortugas", "tipo_animal": "Tortuga", "marca": "Sera"},
    {"nombre": "ReptoMin Floating Sticks", "imagen": "img_reptomin_tortuga.jpg", "descripcion": "Palitos flotantes para tortugas acuáticas", "tipo_animal": "Tortuga", "marca": "ReptoMin"},
    # comida conejo
    {"nombre": "Heno para Conejo", "imagen": "img_heno_conejo.jpg", "descripcion": "Heno fresco y saludable para conejos", "tipo_animal": "Conejo", "marca": "Vitakraft"},
    {"nombre": "Kaytee Forti-Diet Conejos", "imagen": "img_kaytee_conejo.jpg", "descripcion": "Alimento completo y equilibrado para conejos", "tipo_animal": "Conejo", "marca": "Kaytee"},
    {"nombre": "Oxbow Essentials Conejos", "imagen": "img_oxbow_conejo.jpg", "descripcion": "Alimento premium para conejos adultos", "tipo_animal": "Conejo", "marca": "Oxbow"},
    # comida pajaro
    {"nombre": "Semillas para Pájaros", "imagen": "img_semillas_pajaros.jpg", "descripcion": "Mezcla de semillas variadas para pájaros", "tipo_animal": "Pájaro", "marca": "Zupreem"},
    {"nombre": "Kaytee Exact Rainbow", "imagen": "img_kaytee_pajaros.jpg", "descripcion": "Alimento completo para la dieta diaria de pájaros", "tipo_animal": "Pájaro", "marca": "Kaytee"},
    {"nombre": "Lafeber's Nutri-Berries", "imagen": "img_nutri_berrires_pajaros.jpg", "descripcion": "Bayas nutritivas para pájaros grandes y pequeños", "tipo_animal": "Pájaro", "marca": "Lafeber"},
    # comida para hamster
    {"nombre": "Alimento para Hamster", "imagen": "img_alimento_hamster.jpg", "descripcion": "Mezcla de granos y semillas para hamsters", "tipo_animal": "Hamster", "marca": "Vitakraft"},
    {"nombre": "Kaytee Fiesta Hamsters", "imagen": "img_kaytee_hamster.jpg", "descripcion": "Mezcla nutritiva y variada para hamsters", "tipo_animal": "Hamster", "marca": "Kaytee"},
    {"nombre": "Oxbow Garden Select Hamsters", "imagen": "img_oxbow_hamster.jpg", "descripcion": "Alimento premium para hamsters", "tipo_animal": "Hamster", "marca": "Oxbow"},
    # Juguetes para Perros
    {"nombre": "Pelota", "imagen": "img_pelota.jpg", "descripcion": "Pelota divertida para perros", "tipo_animal": "Perro", "marca": "Marca X"},
    {"nombre": "Hueso de goma", "imagen": "img_hueso.jpg", "descripcion": "Hueso duradero para perros", "tipo_animal": "Perro", "marca": "Marca Y"},
    {"nombre": "Cuerda", "imagen": "img_cuerda.jpg", "descripcion": "Cuerda resistente para perros", "tipo_animal": "Perro", "marca": "Marca Z"},
    # Juguetes para Gatos
    {"nombre": "Raton de juguete", "imagen": "img_raton.jpg", "descripcion": "Ratón de juguete para gatos", "tipo_animal": "Gato", "marca": "Marca A"},
    {"nombre": "Pluma", "imagen": "img_pluma.jpg", "descripcion": "Pluma divertida para gatos", "tipo_animal": "Gato", "marca": "Marca B"},
    {"nombre": "Rascador", "imagen": "img_rascador.jpg", "descripcion": "Rascador para gatos", "tipo_animal": "Gato", "marca": "Marca C"},
    # Juguetes para Conejos
    {"nombre": "Tunel", "imagen": "img_tunel.jpg", "descripcion": "Túnel para explorar para conejos", "tipo_animal": "Conejo", "marca": "Marca D"},
    {"nombre": "Zanahoria de juguete", "imagen": "img_zanahoria.jpg", "descripcion": "Zanahoria de juguete para conejos", "tipo_animal": "Conejo", "marca": "Marca E"},
    {"nombre": "Mordedor", "imagen": "img_mordedor.jpg", "descripcion": "Mordedor resistente para conejos", "tipo_animal": "Conejo", "marca": "Marca F"},
    # Juguetes para Roedores
    {"nombre": "Rueda de ejercicio", "imagen": "img_rueda.jpg", "descripcion": "Rueda de ejercicio para roedores", "tipo_animal": "Roedores", "marca": "Marca G"},
    {"nombre": "Casita de madera", "imagen": "img_casita.jpg", "descripcion": "Casita de madera para roedores", "tipo_animal": "Roedores", "marca": "Marca H"},
    {"nombre": "Tunel", "imagen": "img_tunel.jpg", "descripcion": "Túnel para roedores", "tipo_animal": "Roedores", "marca": "Marca I"}
]

# Guardar productos en productos.csv
with open('productos.csv', mode='w', newline='') as csvfile:
    fieldnames = ['nombre', 'imagen', 'descripcion', 'tipo_animal', 'marca']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for producto in productos:
        writer.writerow(producto)

print("Datos guardados en productos.csv")
