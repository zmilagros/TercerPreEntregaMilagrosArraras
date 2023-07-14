# CODERHOUSE - PYTHON - TercerEntrega - Arraras Milagros #

## PROYECTO: ONLINE CLOTHING STORE :shopping:

simp("bt.rojo")### INDICE ###

-Notas
-Enlace página
-Acceder al admin
-Autor
-Sobre el proyecto
-Flujo
-Extensiones



### NOTAS ###
Utilizar la rama main



### ENLACE PÁGINA ###

(http://127.0.0.1:8000/admin/)

(http://127.0.0.1:8000/TIENDA/)

(http://127.0.0.1:8000/TIENDA/about/)

(http://127.0.0.1:8000/TIENDA/products/)

(http://127.0.0.1:8000/TIENDA/store/)



### ACCEDER AL ADMIN  :old_key:

**username**: milagros

**password**: 123456789



### AUTOR ###

Milagros Arraras, aprendiz de Python.




### SOBRE EL PROYECTO ###

El proyecto consiste en una base de datos de un comercio donde tiene:

**-Clientes**

**-Productos**

**-Categorías**

En **Clientes** se puede ingresar los datos de los nuevos usuarios que se quieran adherir a nuestra página y los mismos se pueden visualizar ahi mismo, luego de haberse registrado.

En **Productos** está orientado a los vendedores para que ingresen los datos de los productos en stock con sus respectiva descripción, para que los administradores puedan agregar ese nuevo modelo( prenda) a las categorías de la página.

En **Categorías** encontramos los tipos de prendas separadas por secciones como parte superior; remeras y tops; parte inferior; pantalones y faldas; segundapiel; abrigos. La idea es que con las actualizaciones se pueda distribuir en sección invierno, verano, es decir que filtre más categorías y que al entrar en ellas se vean los productos correspondientes a comprar online.


La página está orientada en este caso a comercios femeninos, pero al ser pensada como una base para vender a tiendas de ropa en un futuro, fue creada para ser flexible en caso de reutilizar el proyecto para otro comercio. 





### FLUJO  :triangular_flag_on_post:

Para iniciar nuestro código hay que instalar **pip install django**
Luego, dentro de la carpeta project, ejecutar **python manage.py runserver**

Luego nos dará una urls con nuestra página web donde veremos una lo que contiene TIENDA/index.html que es nuestro inicio/página principal. Podemos navegar a clientes gracias a la urls asociada a TIENDA/about.html que nos mostrá un formulario a completar y visualizaremos nuestros registros debajo. Al lado tenemos a productos dirigida por TIENDA/products.html que contiene un formulario a completar por los vendedores y se ven nuestros productos en stock abajo. Por último tenemos a categorias dirigida por TIENDA/store.html que muestra nuestras categorías explicado en la parte superior. Todas estas secciones logran visualizarse gracias a navegacion.html que heredan los htmls mencionados anteriormente. Esta práctica de navegación funciona por los urls asociados que llegarán a la carpeta config y urls.py.




### 🔗Dependencias Externas ###

**Visual Studio Code**

**Django**

**Bootstrap**







