# PROYECTO DE ALGORIMTOS BIOINSPIRADOS
## ALGORITMO HIBRIDO PSO-GA
### TABLA DE CONTENIDO
- Introducción
- Instalación de librerías y dependencias
- Modulos y Clases del programa
- Ejecución del programa

### INTRODUCCIÓN
El presente proyecto es una implementación de un híbrido entre dos algoritmos de optimización bioinspirados. El primero de ellos es el Particle Swarm Optimization (PSO) u Optimización por Cúmulo de Partículas, este algoritmo es un optimizador basado en trabajo colectivo de ciertas especies como los bancos de pedes o las parvadas de aves para encontrar fuentes óptimas de alimento. El otro algoritmo es el Genetic Algorithm (GA) o Algoritmo Genético, cuyo funcionamiento se basa en la evolución, incorporando técnicas de selección de padres, cruza, mutación y selección de sobrevivientes. 

El algoritmo propuesto busca explotar las virtudes de ambos algoritmos para poder optimizar funciones o modelos matemáticos en espacios continuos, por ejemplo, funciones de optimización como Ackley, Griewank y Rosenbrock.

### LIBRERIAS Y DEPENDENCIAS

![Esta es una imagen de ejemplo](https://img.shields.io/badge/numpy-1.23.5-blue)
![Esta es una imagen de ejemplo](https://img.shields.io/badge/matplotlib-3.5.3-blue)
![Esta es una imagen de ejemplo](https://img.shields.io/badge/random-8A2BE2)
![Esta es una imagen de ejemplo](https://img.shields.io/badge/math-8A2BE2)
![Esta es una imagen de ejemplo](https://img.shields.io/badge/functools-8A2BE2)
![Esta es una imagen de ejemplo](https://img.shields.io/badge/operator-8A2BE2)
![Esta es una imagen de ejemplo](https://img.shields.io/badge/copy-8A2BE2)
- Las librerías son señaladas en las badges azules junto con la versión utilizada. 
- Las dependencias de Python (aquellas que vienen con la instalación típica de python) estan marcadas en las badges moradas

### MODULOS & CLASES DEL PROGRAMA
#### CLASES
1. Clase Cromosoma (individuo.py): A lo largo del proyecto se debe tomar en cuenta que los términos individuo, cromosoma y partícula harán referencia a los objetos de la misma clase, en este caso a los objetos de la clase Cromosoma. Esta clase es la que contiene las funciones y parámetros que cada individuo y cada partícula deben tener para operar en sus respectivos algoritmos (GA Y PSO).
2. Clase Población (poblacion.py): A lo largo del proyecto se debe tomar en cuenta que los términos población y cúmulo harán referencia a los objetos de la misma clase, en este caso a los objetos de la clase Población. Esta clase es la que contiene a todos los objetos de la clase Cromosoma y que contiene también los valores del óptimo global y las funciones para extraer la información de la población a cada generación.

#### MODULOS
1. Módulo de Cruza (cruza.py): En este módulo encontramos programada la función de cruza que se ha decidido implementar para nuestro algoritmo híbrido, la cuál es la cruza uniforme binaria. Esta cruza intercambia valores de la codificación binaria de los padres sí y solo sí un valor de probabiñidad entre 0 y 1 generado aleatoriamente al momento es menor a la probabilidad de cruza del GA.
2. Módulo de Codificacón Binaria (encoder_decoder.py): En este módulo encontramos los métodos que serán útiles para transformar los vectores de soluciones candidatas a una cadena binaria (Codificación) y viceversa (Decodificación) para poder aplicar las estrategías de cruza y mutación del GA.
3. Módulo de Funciones Objetivo (funciones_objetivo.py): En este módulo encontramos programas las funciones a optimizar seleccionadas. En este caso han sido Ackley, Griewank y Rosenbrock.
4. Módulo de Mutación (mutacion.py): En este módulo esta programado el método de mutación elegido, el cuál es mutación probabilistica que consiste en recorrer la cadena binaria del cromosoma y en cada carcater decidir si cambiar el valor de 1 a 0 o viceversa con base en una probabilidad generada en el momento y en comparación a la probabilidad de mutación del GA.
5. Módulo de Selección de Padres (parents_selection.py): En este módulo encontramos el método de selección de padres implementado, selección por torneo con torneos de 4 individuos, se ha elegido un número alto para propiciar la selección de los mejores individuos y fomentar la explotación.
6. Módulo de Reparación (reparation_mod.py): Este módulo es el encargado de verificar que los valores de un vector solución no sobrepasen los límites del intervalo definido para la optimización, lee cada valor y lo ajusta al valor límite en caso de un excedente. 
7. Módulo de Selección de Sobrevivientes (survivors_selection.py): En este módulo se programó el método de selección de sobrevivientes conocido cómo elitísmo donde unícamente sobreviven los n mejores individvuos donde n es el tamaño de población.
8. Módulo de Hibrido (hibrido.py): Este es el módulo principal donde se programa de manera general el algoritmo. En el método 'particulas_geneticas' tenemos toda la implementacion de la lógica detrás del híbrido propuesto.
9. Módulo Main (main.py): Es el módulo de ejecución donde se establecen los parametros del algoritmo y la función a optimizar (minimizar).
10. Módulo Anova (anova.py): Es un módulo diseñado para realizar múltiples ejecuciones del algoritmo y guardar los resultados y gráficas en una carpeta objetivo que se especifica en la variable prefijo.

#### EJECUCIÓN DEL PROGRAMA
Para poder ejecutar el programa en modo aislado:
1. Primero, descargamos el proyecto de GitHub y lo abrímos en un IDE. 
2. Verficamos tener las librerías y dependencías necesarias, se recomienda utilizar un entorno virtual con conda. 
3. Abrir el módulo main y configurar los parametros necesarios. 
4. Ejecutar main.py

Para ejecutar el programa en modo anova:
1. Se descarga el proyecto del repositorio y se abre con un IDE, se recomienda VisualStudio Code
2. Verificamos tener las librerías y dependencias, se recomienda utilizar un entorno virtual con conda. Recordando que dependiendo de la librería puede instalarse con pip install o conda install, se recomienda revisar la documentación de cada dependencia.
3. Abrir el módulo anova y definir los parámetros necesarios (parametros de entrada, número de ejecuciones, carpeta objetivo de salida).
4. Ejecutamos anova.py