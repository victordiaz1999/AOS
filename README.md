# AOS-Grupo 6
      Juan José Meneses Fernández
	  Víctor Díaz de Diego
	  Raúl Nuñez Alonso
	  Víctor Sánchez Corrales
	 
# Descripción

Creación de un subsistema para gestión de clientes de un taller

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

		PUT http://x.x.x.x:8080/clientes/42
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

		GET http://x.x.x.x:8080/clientes/452
		
#### Para obtener datos de un cliente del taller (identificado por su NIF)

		GET http://x.x.x.x:8080/clientes/nifnie/67834236-N
		
#### Para obtener una lista de clientes por nombre 

		GET http://x.x.x.x:8080/clientes/nombre/Juanjo
		
