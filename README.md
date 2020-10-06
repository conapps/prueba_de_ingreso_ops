# Prueba de Ingreso - Operaciones

## Introducción

Este `playbook` levanta un ambiente de desarrollo en la nube de AWS para realizar la prueba de ingreso del puesto de operaciones.

Para poder correr los `playbooks` es necesario configurar previamente las variables de entorno `AWS_ACCESS_KEY_ID` y `AWS_SECRET_ACCESS_KEY`. Las mismas serán utilizadas por los `playbook` para levantar la infraestructura en la nube de AWS.

**OBS 1: El proyecto requiere de Ansible 2.10+ para funcionar."

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

## Variables

Para poder levantar la infraestructura es necesario configurar las siguientes variables de entorno:

| Nombre | Ejemplo | Descripción |
| ---    | ---               | ---         |
| `AWS_ACCESS_KEY_ID` | `""` | Llave de acceso de la cuenta de AWS. |
| `AWS_SECRET_ACCESS_KEY` | `""` | Llave secreta de acceso de la cuenta de AWS. |
| `AWS_SUBNET_ID` | `""` | ID de la subnet sobre la cual se levantarán las instancias de EC2. |
| `AWS_SUBNET_CIDR` | `192.168.1.0/24` | Bloque CIDR configurado en la subnet. |
| `AWS_SECURITY_GROUP_ID` | `""` | ID del security group que se le aplicarán a las imagenes. |
| `DOMAIN` | `labs.exampel.com` | Dominio sobre el cual se escribirán los recursos para acceder a los equipos. |
| `POSITION` | `sysadmin` | Rol de la posición que se esta evaluando. |
| `PROYECT_REPO` | `https://github.com/conatel-i-d/prueba_de_ingreso` | URL con el repositorio con el proyecto a levantar. |
| `PROYECT_REPO_NAME` | `prueba_de_ingreso` | Nombre del repo. |

Pueden utilizar el siguiente template para crear un archivo `.env`:

```ini
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_SUBNET_ID=
AWS_SUBNET_CIDR=
AWS_SECURITY_GROUP_ID=
DOMAIN=
POSITION=
PROJECT_REPO=https://github.com/conatel-i-d/prueba_de_ingreso
PROJECT_REPO_NAME=prueba_de_ingreso
```

Una vez creado el archivo, se pueden cargar estas variables en la consola de la siguiente manera:

```bash
source .env
```

**Es importante recordar que el proyecto esta diseñado para operar de forma exclusiva sobre la región `us-east-1` de AWS. Por lo tanto, las subnetes y security groups tienen que exisitir previamente en esta región. Este proyecto no levanta ninguna otro recurso además de las instancias.**

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

