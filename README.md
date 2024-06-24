[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/dpfHO3Yy)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14986711&assignment_repo_type=AssignmentRepo)
![Logo de la Institución ISPC](./E%20assets/logoISPC.png)

# Proyecto Final - Capa de Almacenamiento

## Información General del Curso

- **Institución**: Instituto Superior Politécnico Córdoba (ISPC)
- **Curso**: Proyecto Integrador I
- **Docente**: Cristian Gonzalo Vera
- **Equipo de Desarrollo Opalo**:
  - Luciano Lujan | GitHub: https://github.com/lucianoilujan
  - Joaquin Garzón | GitHub: https://github.com/Joacogarzonn
  - Durigutti, Vittorio | GitHub: https://github.com/vittoriodurigutti
  - Joaquin Zalazar | GitHub: https://github.com/breaakerr
  - Lisandro Juncos | GitHub: https://github.com/Lisandro-05
  - Nahuel Velez | GitHub: https://github.com/ISPC-TST-PI-I-2024/ISPC_PI_Lucas_Nahuel_Velez 
  - Jose Marquez | GitHub: https://github.com/ISPC-TST-PI-I-2024/josemarquez.git
  - Tomas Repossi | GitHub:  https://github.com/TomasRepossi

## Sobre el Proyecto

Este repositorio está dedicado a la Capa de Almacenamiento del proyecto IoT. Incluye todos los componentes desarrollados y documentación generada por los estudiantes conforme avanzan en la implementación de esta capa del proyecto.

Nos encontramos en el desarrollo de un dispositivo IoT con el que medir en tiempo real los valores de glucemia de un paciente. Dentro del directorio programacion nos encontramos una estructura con python y con el uso de flask, ejecutamos el programa en una direccion online, dandonos acceso a la base de datos, de momento siendo una estrcutura estatica, pero proximamente, sera actualizad a tiempo real, con un dispositivo prototipo. 


### Estructura del Repositorio

- **A requisitos**: Contiene documentos de requisitos proporcionados por el docente.
- **B investigacion**: Investigaciones realizadas por los estudiantes.
- **C prototipo**: Implementaciones específicas de la capa de almacenamiento.
  - **Componentes Principales**
        - app.py: El archivo principal de la aplicación Flask, que define las rutas y la lógica del servidor web.
        - static/ y templates/: Directorios utilizados por Flask para servir archivos estáticos y plantillas HTML.
        - Dockerfile: Archivo utilizado para construir una imagen de Docker que contiene la aplicación Flask.
        - docker-compose.yml: Archivo de configuración para Docker Compose, que facilita la configuración y ejecución de servicios de Docker.
        - requirements.txt: Archivo que lista las dependencias de Python necesarias para ejecutar la aplicación Flask.
        - Proyecto PI.sql: Archivo que contiene las instrucciones SQL para la configuración de la base de datos.
- **D presentacion**: Incluye grabaciones y bitácoras de las reuniones de Scrum, así como las presentaciones de progreso.
- **zassets**: Contiene recursos gráficos como imágenes y otros archivos necesarios para la documentación.

## Stack Tecnológico Común

- Control de Versiones: **Git y GitHub**
- Metodologías Ágiles: **Scrum y Kanban**
- Aprendizaje Basado en Proyectos (ABP)
- Soporte DevOps por parte del docente

## Stack Tecnológico para el Sprint Actual

- IDE: **Visual Studio Code**
- Bases de Datos: **MySQL** (SQL), **MongoDB** (NoSQL)
- Contenedorización: **Docker y Kubernetes**
- Lenguajes de Programación: **Python y JavaScript (HTML y CSS)**
- Herramientas Adicionales: **Postman** para pruebas de API

-------------------------------------------

## Licencia

Este proyecto está licenciado bajo la Licencia Creative Commons Atribución-NoComercial (CC BY-NC). Esta licencia permite que otros remixen, adapten y construyan sobre el trabajo de forma no comercial y, aunque sus nuevos trabajos deben también reconocer al autor original y ser no comerciales, no tienen que licenciar sus obras derivadas en los mismos términos.

Esta licencia es adecuada para un uso educativo y de aprendizaje, permitiendo la libre distribución y utilización del material mientras se protege contra el uso comercial sin autorización previa. Para usos comerciales, es necesario contactar a los autores para obtener permiso. 

Para obtener más información sobre esta licencia y ver una copia completa de sus términos, visite [Creative Commons Atribución-NoComercial (CC BY-NC)](https://creativecommons.org/licenses/by-nc/4.0/)..-
