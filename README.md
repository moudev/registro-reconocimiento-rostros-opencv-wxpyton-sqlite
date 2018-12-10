## Registro de usuarios con Sqlite y wxPython

El proyecto consta de realizar un registro de usuarios con [wxPython](https://wxpython.org) como interfaz gráfica, y [Sqlite](https://www.sqlite.org/) para registro de información. Como agregado almacenar fotografía del usuario.

## Utilizando OpenCV
Para la toma de la fotografía se hace uso básico de [OpenCV](https://opencv.org/) para acceder a la webcam y realizar la toma.

## Detección y reconocimiento de rostros
Para utilizar mejor lo que es OpenCV y una de sus famosas características se hizo la implementación que pudiera tomar multiples fotografías del usuario, para posteriormente hacer el entrenamiento y pueda reconocerlo. Se creó desde cero la lógica de la aplicación, que consisitió en investigar como usar wxPython junto con OpenCV y pasar imagen de la webcam hacia la interfaz gráfica, así como también la estructura de las carpetas para un mayor orden de las imagenes y posterior procesamiento.

## Explicación rápida del flujo de la aplicación
- Login
- Registro usuario
- Entrar al formulario de busqueda
- Escojer un usuario del listado
- Escojer la opción "Entrenamiento"
- En el formulario abierto presionar "Captura" y se empezará a realizar la toma de 10 fotografías para luego hacer el entrenamiento, en la parte baja del formulario se mostrarán las fotografías tomadas, y en la parte superior se mostrará una imagen con el número de la fotografía que será tomada, solo se necesita presionar una vez la opción "Captura"
- Luego de la toma de fotografías presionar "Entrenar" para que las imagenes se guarden para posterior entrenamiento.
- Ir al menú principal y seleccionar el icono similar al de reciclaje, para empezar el procesamiento de las fotografías de usuarios y empezar el entrenamiento.
- Se mostrará ventana para confirmar si se desea entrenar, seleccionar que sí
- Luego empieza el entrenamiento que puede llevar una cantidad de tiempo no muy grande debido a que solo son 10 fotografías por usuario, en dado caso hayan 100 usuarios con 10 fotografías cada uno, el tiempo de entrenamiento puede durar unos 10 mins aprox.
- Una vez terminado el entrenamiento se mostrará la ventana de éxito.
- Para empezar con el reconocimiento puedes seleccionar el icono que tiene figura de humano.
- Si te reconoce se mostrará una ventana emergente con el usuario con el que tienes coincidencias.
- **Recuerda revisar el log de consola para ver los procesos que se realizan**


### Notas
Este proyecto únicamente fué desarrollado y testeado en una máquina con bajos recursos (Intel Celeron 1.6GHz, 2GB RAM, 2GB swap), y bajo el S.O _GNU/Linux Debian Jessie stable_. Es una base para futuros proyectos cuando se disponga de mayor hardware y poder hacer uso del entrenamiento con miles de imagenes, no específicamente para entrenamiento y reconocimiento de rostros. La cantidad de 10 fotografías por usuario no es suficiente para entrenar bien, se requieren de una gran cantidad para que se acerque a tener un resultado decente. Revisar cada uno de los archivos .py en donde tiene con un poco de buena explicación su funcionamiento. Revisa la carpeta de _"/capturas"_ para ver el diseño de la interfaz gráfica y de los procesos en consola.
