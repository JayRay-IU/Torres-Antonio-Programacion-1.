# Torres-Antonio-Programacion-1.
Alumno: José Antonio Yamir Torres Bermúdez

Curso: Programación 1, impartido por Sorpresa Lora Castro

Grupo: Licenciatura en Creatividad Digital (CUGDL)

# Propósito del repositorio:
archivar, documentar y subir los proyectos o trabajos de códigos realizados con anterioridad para su análisis y calificacion posteriorres, 
ademas de contar con una interfaz ordenada para su analisis mas eficiente a largo plazo.

# Estructura de carpetas:
Practicas: evidencia de las prácticas de código trabajadas a lo largo del semestre con posible organización sistemática dentro de la misma.
Proyectos: evidencia de los proyectos de gran tamaño e individuales trabajados a lo largo del ssemestre.

# Bitácora de Instalación del IDE (Visual Studio Code)
1. Información General
IDE Seleccionado: Visual Studio Code (VS Code)

Versión instalada: 1.93.x / Última versión estable

Sistema Operativo: Windows 11 (64-bit)

2. Proceso de Instalación
Descarga: Se ingresó al sitio web oficial (code.visualstudio.com) y se descargó el instalador para Windows de 64 bits.

Ejecución del instalador: Se ejecutó el archivo .exe con permisos de administrador.

Configuración inicial: Durante el asistente de instalación, se marcaron las siguientes opciones recomendadas:

Agregar al PATH (para poder abrirlo desde la terminal con el comando code).

Registrar Code como editor para los formatos de archivo compatibles.

Crear un acceso directo en el escritorio.

# Instrucciones para clonar y utilizar el repositorio en equipo:

Clonar el repositorio:
Descarga el repositorio en tu máquina local ejecutando el siguiente comando en la terminal:

Bash
git clone <URL_DEL_REPOSITORIO>
Acceder al directorio:
Entra a la carpeta generada por el comando anterior:

Bash
git basename_o_carpeta
(Sustituye por el nombre real de la carpeta del proyecto).

Abrir el entorno de trabajo:
Abre el proyecto en el IDE seleccionado. Si utilizas Visual Studio Code, puedes abrirlo directamente desde la terminal con:

Bash
code .
Crear una rama de trabajo:
Para evitar conflictos directos en la rama principal (main), crea y cámbiate a tu propia rama antes de realizar modificaciones:

Bash
git checkout -b <nombre-de-tu-rama>
Flujo de desarrollo local:

Realiza los cambios necesarios en el código dentro de tu IDE.

Prepara los archivos modificados: git add .

Guarda los cambios localmente con un mensaje descriptivo: git commit -m "Descripción del cambio"

Sube tu rama al repositorio remoto: git push origin <nombre-de-tu-rama>
