# TFM-Matias
---------------------------------------------------------------------------------------------------------------------------------------------------
Esta base de datos ha sido realizada por Matías Rivera Iglesias como parte de la metodología empelada
para desarrollar el Trabajo de Fin de Master "IDENTIFICACIÓN DE ALTERNATIVAS PARA LA SIMBIOSIS INDUSTRIAL EN LA INDUSTRIA GALLEGA"

Si desea ponese en contacto, escriba un correo a: matias.rivigl@gmail.com
----------------------------------------------------------------------------------------------------------------------------------------------------
Explicación del contenido de la Base de Datos

# TABLAS
	cnae09_cnae25_nace: Contiene las conversiones entre los códigos.
	industrias_prtr: Industrias recogidas en el PRTR dentro de la región de Galicia
	maestri: Base de datos de MAESTRI.
	residuos_prtr_espanha: Residuos generados por las industrias españoles desde el año 2007 al 2024, sin incluir el 2013 ya que el archivo se encontraba dañado en el momento de realización del trabajo.
	z1_galicia_si: Todas las SI potenciales de la región de Galicia.
	z2_galicia_si_ler: SI tras la criba por Código LER de los grupos 2, 3, 19 y 20.
	z3_galicia_si_X: SI potenciales de la región de Galicia tras la criba a distancia menor de X.
	z4_galicia_si_X_ler: SI potenciales de la región de Galicia tras la criba a distancia menor de X y Código LER de los grupos 2, 3, 19, y 20.
	z5_Y: Industrias a 20 km de la industria Y.

# TUTORIAL:

En el caso de querer acceder a la información contenida en cada una de las tablas, puede emplear la siguiete query:

select *
from tabla

donde tabla es el nombre de la tabla que desee consultar.
