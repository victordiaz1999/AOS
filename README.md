# AOS-Grupo 6
      Juan José Meneses Fernández
	  Víctor Díaz de Diego
	  Raúl Núñez Alonso
	  Víctor Sánchez Corrales
	 
# Descripción

Creación de un subsistema para gestión de clientes de un taller

# Instalación y Uso
-Para la creación de una imagen con un nombre que identifique el contenedor ejecutamos:

docker build -t ss1:0.1

-Para ejecutar la imagen creando un contenedor usamos el siguiente comando:

docker run -p 8080:8080 ss1:0.1

-Para levantar el servicio es necesario ejecutar el siguiente comando:

docker-compose up


# Guía de Uso

#### Para registrar un nuevo cliente

		POST http://x.x.x.x:8080/clientes
		Body:
		{
				"nif/nie": "90596299-X",
				"idCliente": 452,
				"nombre": "Juanjo",
				"apellidos": "Meneses",
				"domicilio": "Calle Indalecio 32",
				"telefono": "638765432",
				"email": "jjmeneses@outlook.es"
			}

#### Para obtener los clientes del taller 

	  GET http://x.x.x.x:8080/clientes

#### Para modificar datos de un cliente del taller (identificado por idCliente)

		PUT http://x.x.x.x:8080/clientes/2022
		headers:
			  if-match = 24f21ae791234aeb
		Body:
		{
				"nif/nie": "67834236-N",
				"idCliente": 42,
				"nombre": "Victor",
				"apellidos": "Diaz",
				"domicilio": "Calle Europa 4",
				"telefono": "665492318",
				"email": "vidiaz@gmail.com"
			}

#### Para obtener datos de un cliente del taller (identificado por idCliente)

		GET http://x.x.x.x:8080/clientes/2022
		
#### Para obtener datos de un cliente del taller (identificado por su NIF o NIE)

		GET http://x.x.x.x:8080/clientes/nifnie/52013776-T
		
#### Para obtener una lista de clientes por nombre 

		GET http://x.x.x.x:8080/clientes/nombre/Francisco
		
