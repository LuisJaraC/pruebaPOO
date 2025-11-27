usuarios validos para ingresar a la interfaz
usuario: vet1  contraseña: vet123



1) Estructura del Proyecto

pruebaPOO/
│
├── app/                     # CAPA DE APLICACIÓN
│   ├── controladores/       # Lógica y coordinación (ControladorCentral y Subs)
│   ├── modelos/             # Objetos de datos (Entidades como Cuidador, Mascota)
│   └── vista/               # Interfaz de usuario ( Por consola)
│
├── infra/                   # CAPA DE INFRAESTRUCTURA
│   ├── repositorios/        # Acceso a Datos (SQL), RepoCentral y CRUDs específicos
│   ├── Conection.py         # Clase Singleton para la conexión a MySQL
│   └── DB.sql               # Script SQL para la creación de la base de datos
│
├── .env                     # Variables de entorno (Credenciales seguras)
├── .gitignore               # Archivos ignorados por Git
└── main.py                  # Inicialización e Inyección de Dependencias (DI)


2) Arquitectura y Decisiones de Diseño (SOLID)
Este proyecto prioriza la modularidad y escalabilidad mediante tres pilares:

1. Conexión Centralizada
Estrategia: Inicializamos la conexión a la base de datos una única vez en el Main y la encapsulamos en RepoCentral. Este gestor agrupa todos los repositorios específicos en un objeto unificado llamado conexionContexto. 
Motivo: Optimización de recursos (una sola conexión viva) y facilidad de mantenimiento al tener un único punto de configuración.

2. Inyección de Dependencias (DI)
Estrategia: Inyectamos el conexionContexto en el ControladorCentral, quien lo distribuye hacia los Sub-Controladores. 
Motivo: Desacoplamiento total. Los controladores comparten el acceso gestionado a los datos sin necesidad de instanciar conexiones propias, respetando los principios SOLID.

3. Responsabilidad Única (SRP)
Estrategia: Separamos roles estrictamente.
** Breves excepciones en Sub-Controladores para toma de datos y avisos breves, evitando sobre ingenieria hacia Vistas ( además de peligros de llamadas circulares ).

Controladores: Interactúan con el usuario y encapsulan los datos en objetos Modelo.

Repositorios: Reciben el modelo y ejecutan exclusivamente las transacciones SQL. Motivo: Si la base de datos o las reglas de negocio cambian, solo se modifica el módulo afectado, garantizando un sistema robusto y escalable.
