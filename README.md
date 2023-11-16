# estudiantes-app

> Ejemplo de app que integra un API RESTFul con un Frontend, desarrollada en Python3 con Flask. Este código puede ser utilizado como guía para el desarrollo de sus apps (6to 2da - EEST N°1)

## prerequisitos

Es necesario tener instalado los siguiente para poder correr esta app:
1. __Python3__ 
2. __Flask__
3. __Jinja2__ (creo que se instala automaticamente con Flask)

## setup
Si queremos instalar facilmente las dependencias (packages nombrados arriba) podemos ejecutar el siguiente comando en la terminal:
```
    pip3 install -r requirements.txt
```

Ahora podemos levantar la app ejecutando el siguiente comando en la terminal:
```
    python3 app.py
```

## código
Esta app es un desarrollo híbrido entre una RESTFul API y un BFF (Backend for Frontend).
Sus endpoints soportan pedidos tanto desde el FrontEnd que se encuentra en la carpeta 'frontend', como así también desde cualquier herramienta de testing de apis como Postman.

## testing
1. Si queremos testear la app desde el FrontEnd, vamos directamente a la url http://localhost:5000 en nuestro navegador.
2. Si en cambio deseamos testear directamente cada endpoint del api, podemos invocar llamados desde Postman, de igual manera que se explica en el [apunte sobre API's](https://drive.google.com/file/d/1o-Kh3bAu7Xwfezceu_DFHwIat6qFNwJp/view?usp=drive_link)