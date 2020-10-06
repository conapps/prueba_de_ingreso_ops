# Prueba de Ingreso - Operaciones

## Introducción

Este `playbook` levanta un ambiente de desarrollo en la nube de AWS para realizar la prueba de ingreso del puesto de operaciones.

Para poder correr los `playbooks` es necesario configurar previamente las variables de entorno `AWS_ACCESS_KEY_ID` y `AWS_SECRET_ACCESS_KEY`. Las mismas serán utilizadas por los `playbook` para levantar la infraestructura en la nube de AWS.

## Recomendaciones

El proyecto esta configurado para hacer uso de ciertas buenas prácticas a la hora de correr `playbooks` de Ansible. Por lo tanto, se recomienda correr los `playbooks` de este proyecto utilizando el archivo de configuración `ansible.cfg`. Una forma de hacer esto es configurando la siguiente variable de entorno.

```
export ANSIBLE_CONFIG=./ansible.cfg
```

## Instalación de roles

Las tareas requieren del uso de ciertos roles que tienen que estar presentes previo a la ejecución de los `playbooks`. Por defecto, los mismos no se guardan en GitHub.

La lista de roles se encuentra definida en el archivo `requirements.yml` y se pueden instalar todos juntos ejecutando el siguiente comando:

```
ansible-galaxy install -r requirements.yml
```

## Pod Up

Cuando se ejecuta el Pod se crean dos archivos en la carpeta `secret_vars`. Uno de ellos contiene datos sobre la infraestructura implementada, y el otro es la llave privada que debe utilizarse para acceder a los servidores.

```bash
# Para levantar el POD
ansible-playbook pod_up.yml

# Para conectarse al servidor ubuntu
ssh -i secret_vars/key_pair_operaciones ubuntu@servNum1.labs.conatest.click

# Para conectarse al router CSR1000
ssh -i secret_vars/key_pair_operaciones ec2-user@router.labs.conatest.click
```

## Pod Down

Este comando destruira toda la arquitectura implementada en la nube.

```bash
ansible-playbook pod_down.yml
```

## Validación

Para verídicar que el los ejercicios se completarón correctamente es necesario:

1. Conectarse al servidor Ubuntu

```bash
ssh -i secret_vars/key_pair_operaciones ubuntu@servNum1.labs.conatest.click
```

2. Correr el comando `validate` desde la consola.

```bash
validate
```

Debería ver la ventana con el estado de las pruebas.

## Licencia 

[MIT](./LICENCE)

## Autores

- Ismael Almandos
- Guzmán Monné

## Copyright

CONATEL S.A. 2018

