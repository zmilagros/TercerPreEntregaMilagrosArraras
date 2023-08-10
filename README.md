# CODERHOUSE - PYTHON - Proyecto Final- Arraras Milagros #

## PROYECTO: ONLINE CLOTHING STORE :shopping:

### INDICE ###

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

**TIENDA/HOME**

**-Clientes**

**-Categorías/Productos**

La **TIENDA/Home** es la página inicial que nos muestra el "Sobre nosotros de la página" donde se introduce sobre la Tienda y los productos que ofrece.

En **Clientes** permitimos al personal que se cree un usuario para poder administrar los productos de la tienda. Para ingresar debe rellenar un par de campos y respetar un par de requisitos, luego de registrarse podemos ingresar y editar el usuario. Este usuario permitirá visualizar los productos dentro de categorías.

En **Categorías** encontramos los tipos de prendas separadas por secciones como parte superior; remeras y tops; parte inferior; pantalones y faldas; segundapiel; abrigos. Debajo de esa introducción a los **Productos** disponibles, debemos ingresar a el botón Iniciar sesión para ver stock de productos y luego desde allí el personal podrá editarlos según haya stock de los mismos. Entre las opiones podrá Editar, Eliminar, Agregar y Ver Detalles de los productos.


La página está orientada en este caso a comercios femeninos, pero al ser pensada como una base para vender a tiendas de ropa en un futuro, fue creada para ser flexible en caso de reutilizar el proyecto para otro comercio. 





### FLUJO  :triangular_flag_on_post:

Para iniciar nuestro código hay que instalar **pip install django**
Luego, dentro de la carpeta project, ejecutar **python manage.py runserver**

Luego nos dará una urls con nuestra página web donde veremos una lo que contiene TIENDA/index.html que es nuestro inicio/página principal. Podemos navegar a clientes gracias a la urls asociada a TIENDA/about.html que nos mostrá un formulario a completar y visualizaremos nuestros registros debajo. Al lado tenemos a productos dirigida por TIENDA/products.html que contiene un formulario a completar por los vendedores y se ven nuestros productos en stock abajo. Por último tenemos a categorias dirigida por TIENDA/store.html que muestra nuestras categorías explicado en la parte superior. Todas estas secciones logran visualizarse gracias a navegacion.html que heredan los htmls mencionados anteriormente. Esta práctica de navegación funciona por los urls asociados que llegarán a la carpeta config y urls.py.


###VIDEO###

https://www.loom.com/share/6e5500c0f6df4b5488f4247725b18978



### 🔗Dependencias Externas ###

**Visual Studio Code**

**Django**

**Bootstrap**








