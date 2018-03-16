# Twitter-Scraper

## Método de uso:

1. Instalar virtualenv : 

    `sudo apt-get install virtualenv`

2. Activar el entorno virtual asociado.

    `source venv/bin/activate`

3. Ejecutar el programa con su ayuda para hacerse una idea de cómo funciona.

    `./twitter_scraper.py -h`
    
          `usage: twitter_scraper.py [-h] [--usuarios USUARIOS]
                          [--fecha_inicio FECHA_INICIO]
                          [--fecha_final FECHA_FINAL] [--palabras PALABRAS]
`optional arguments:
  -h, --help            show this help message and exit
  --usuarios USUARIOS, -u USUARIOS
                        Lista separada por comas de usuarios que se quieran
                        buscar
  --fecha_inicio FECHA_INICIO, -i FECHA_INICIO
                        Fecha de inicio con el formato: DD/MM/AAAA
  --fecha_final FECHA_FINAL, -f FECHA_FINAL
                        Fecha final con el mismo formato
  --palabras PALABRAS, -p PALABRAS
                        Lista de palabras separada por comas para filtrar
                        tweets `
                        
4. Ejecución de ejemplo:

    `./twitter_scraper.py --usuarios @iescolar --fecha_inicio 1/01/2018 --fecha_final 15/03/2018 --palabras hospital,feminista`
    
    
Esto creará un archivo llamado @iescolar.tsv con información sobre el tweet, por orden:
     Fecha  url_media   media_type  FAV RT  Texto   Nombre_usuario
     
Si se quisiese hacer el scrap sobre más usuarios bastara con añadirlos con una coma entre ellos y se creara un fichero para cada uno de ellos. EJ: @user1,@user2,@user3 
