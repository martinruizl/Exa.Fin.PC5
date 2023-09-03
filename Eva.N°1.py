{
 "celdas" : [
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "identificación" : " tp1PuTXr8hQf "
   },
   "fuente" : [
    " #Importar Pandas "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 4 ,
   "metadatos" : {
    "identificación" : " 7V5ec9ex8hQl "
   },
   "salidas" : [],
   "fuente" : [
    " #importa pandas \n " ,
    " importar pandas como pd "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 5 ,
   "metadatos" : {},
   "salidas" : [
    {
     "datos" : {
      "texto/sin formato" : [
       " '1.5.3' "
      ]
     },
     "recuento_ejecución" : 5 ,
     "metadatos" : {},
     "tipo_salida" : " resultado_ejecución "
    }
   ],
   "fuente" : [
    " pd.__versión__ "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 7 ,
   "metadatos" : {},
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      " Requisito ya satisfecho: pandas en c: \\ users \\ 51966 \\ anaconda3 \\ lib \\ site-packages (1.5.3) \n " ,
      " Requisito ya satisfecho: numpy>=1.21.0 en c: \\ users \\ 51966 \\ anaconda3 \\ lib \\ site-packages (de pandas) (1.23.5) \n " ,
      " Requisito ya satisfecho: python-dateutil>=2.8.1 en c: \\ users \\ 51966 \\ anaconda3 \\ lib \\ site-packages (de pandas) (2.8.2) \n " ,
      " Requisito ya satisfecho: pytz>=2020.1 en c: \\ users \\ 51966 \\ anaconda3 \\ lib \\ site-packages (de pandas) (2022.7) \n " ,
      " Requisito ya satisfecho: seis>=1.5 en c: \\ usuarios \\ 51966 \\ anaconda3 \\ lib \\ site-packages (de python-dateutil>=2.8.1->pandas) (1.16.0) \n "
     ]
    }
   ],
   "fuente" : [
    " !pip instalar pandas "
   ]
  },
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "identificación" : " uQcJ3FUX8hQn "
   },
   "fuente" : [
    " #Crear una Serie "
   ]
  },
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "id" : " Yd-mDtrg8hQo "
   },
   "fuente" : [
    " Explore series en python en el siguiente [link](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) en las primeras líneas del documento "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 8 ,
   "metadatos" : {
    "identificación" : " oYHZImpb8hQo " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      " 0 10 \n " ,
      " 1 20 \n " ,
      " 2 10 \n " ,
      " tipo d: int64 \n "
     ]
    }
   ],
   "fuente" : [
    " # Crea una Serie de los números 10, 20 y 10. \n " ,
    " numeros = [10, 20, 10] \n " ,
    " serie_numeros = pd.Series(numeros) \n " ,
    " imprimir(serie_numeros) "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 9 ,
   "metadatos" : {
    "identificación" : " itO9hqcO8hQp " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      " 0 Rojo \n " ,
      " 1 Verde \n " ,
      " 2 Azul \n " ,
      " tipo d: objeto \n "
     ]
    }
   ],
   "fuente" : [
    " # Crea una serie con tres objetos: 'rojo', 'verde', 'azul' \n " ,
    " objetos = ['Rojo','Verde','Azul'] \n " ,
    " serie_objetos = pd.Series(objetos) \n " ,
    " imprimir(serie_objetos) \n "
   ]
  },
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "identificación" : " R_S7B7Ve8hQp "
   },
   "fuente" : [
    " # Crear un marco de datos "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 12 ,
   "metadatos" : {
    "identificación" : " rfhUQAoL8hQq " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      " Marco de datos vacío \n " ,
      " Columnas: [] \n " ,
      " Índice: [] \n "
     ]
    }
   ],
   "fuente" : [
    " # Crea un marco de datos vacío llamado 'df' \n " ,
    " importar pandas como pd \n " ,
    " \n " ,
    " df = pd.DataFrame() \n " ,
    " \n " ,
    " imprimir(df) "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 13 ,
   "metadatos" : {
    "identificación" : " Pe6CTVlO8hQr " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      "    Nueva Columna \n " ,
      " 0 10 \n " ,
      " 1 20 \n " ,
      " 2 10 \n "
     ]
    }
   ],
   "fuente" : [
    " # Crea una nueva columna en el dataframe, y asignale la primera serie que has creado \n " ,
    " df['Nueva Columna'] = serie_numeros \n " ,
    " imprimir(df) "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 14 ,
   "metadatos" : {
    "identificación" : " wVHF6wkf8hQr " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      "    Nueva Columna objetos \n " ,
      " 0 10 Rojo \n " ,
      " 1 20 Verde \n " ,
      " 2 10 Azul \n "
     ]
    }
   ],
   "fuente" : [
    " # Crea otra columna en el dataframe y asignale la segunda serie que has creado \n " ,
    " df['objetos'] = serie_objetos \n " ,
    " imprimir(df) "
   ]
  },
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "identificación" : " 3mNSx4sA8hQs "
   },
   "fuente" : [
    " # Leer un marco de datos "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 24 ,
   "metadatos" : {
    "identificación" : " khKyzh3t8hQs " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      "                                                    URL   \\\n " ,
      " 0 http://marvel.wikia.com/Henry_Pym_(Tierra-616)    \n " ,
      " 1 http://marvel.wikia.com/Janet_van_Dyne_(Tierra-...    \n " ,
      " 2 http://marvel.wikia.com/Anthony_Stark_(Tierra-616)    \n " ,
      " 3 http://marvel.wikia.com/Robert_Bruce_Banner_(E...    \n " ,
      " 4 http://marvel.wikia.com/Thor_Odinson_(Tierra-616)    \n " ,
      " ... ...    \n " ,
      " 168 http://marvel.wikia.com/Eric_Brooks_(Tierra-616)#    \n " ,
      " 169 http://marvel.wikia.com/Adam_Brashear_(Tierra-6...    \n " ,
      " 170 http://marvel.wikia.com/Victor_Alvarez_(Tierra-...    \n " ,
      " 171 http://marvel.wikia.com/Ava_Ayala_(Tierra-616)#    \n " ,
      " 172 http://marvel.wikia.com/Kaluu_(Tierra-616)#    \n " ,
      " \n " ,
      "                           nombre n_apariciones genero actual fecha_inicio   \\\n " ,
      " 0 Henry Jonathan \" Hank \ " Pym 1269 SÍ MASCULINO 1963    \n " ,
      " 1 Janet van Dyne 1165 SÍ MUJER 1963    \n " ,
      " 2 Anthony Edward \" Tony \" Stark 3068 SÍ MASCULINO 1963    \n " ,
      " 3 Robert Bruce Banner 2089 SÍ MASCULINO 1963    \n " ,
      " 4 Thor Odinson 2402 SÍ MASCULINO 1963    \n " ,
      " .. ... ... ... ... ...    \n " ,
      " 168 Eric Brooks 198 SÍ MASCULINO 2013    \n " ,
      " 169 Adam Brashear 29 SÍ MASCULINO 2014    \n " ,
      " 170 Victor Alvarez 45 SI MASCULINO 2014    \n " ,
      " 171 Ava Ayala 49 SÍ MUJER 2014    \n " ,
      " 172 Kaluu 35 SÍ MASCULINO 2015    \n " ,
      " \n " ,
      "                                                  Notas   \n " ,
      " 0 Fusionado con Ultron en Rage of Ultron Vol. 1. A...   \n " ,
      " 1 muere en Secret Invasion V1:I8. En realidad fue se...   \n " ,
      " 2 Muerte: \" Más tarde, mientras estaba bajo la influencia de Imm...   \n " ,
      " 3 muere en el arco de Fantasmas del futuro. Sin embargo \" él...   \n " ,
      " 4 Dies in Fear It mismo regresa porque eso'...   \n " ,
      " ... ...   \n " ,
      " 168 NaN   \n " ,
      " 169 NaN   \n " ,
      " 170 NaN   \n " ,
      " 171 NaN   \n " ,
      " 172 NaN   \n " ,
      " \n " ,
      " [173 filas x 7 columnas] \n "
     ]
    }
   ],
   "fuente" : [
    " # Lee el archivo llamado 'avengers.csv \" localizado en la carpeta \" data \" y crea un DataFrame, llamado 'avengers'. \n " ,
    " # El archivo está localizado en \" data/avengers.csv \"\n " ,
    " importar pandas como pd \n " ,
    " vengadores = pd.read_csv('C: \\\\ Usuarios \\\\ 51966 \\\\ datos \\\\ vengadores.csv') \n " ,
    " imprimir(vengadores) \n "
   ]
  },
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "identificación" : " oPDPL4nj8hQt "
   },
   "fuente" : [
    " # Inspeccionar un marco de datos "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 26 ,
   "metadatos" : {
    "identificación" : " C90ntYhk8hQt " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      "                                                  URL   \\\n " ,
      " 0 http://marvel.wikia.com/Henry_Pym_(Tierra-616)    \n " ,
      " 1 http://marvel.wikia.com/Janet_van_Dyne_(Tierra-...    \n " ,
      " 2 http://marvel.wikia.com/Anthony_Stark_(Tierra-616)    \n " ,
      " 3 http://marvel.wikia.com/Robert_Bruce_Banner_(E...    \n " ,
      " 4 http://marvel.wikia.com/Thor_Odinson_(Tierra-616)    \n " ,
      " \n " ,
      "                         nombre n_apariciones genero actual fecha_inicio   \\\n " ,
      " 0 Henry Jonathan \" Hank \ " Pym 1269 SÍ MASCULINO 1963    \n " ,
      " 1 Janet van Dyne 1165 SÍ MUJER 1963    \n " ,
      " 2 Anthony Edward \" Tony \" Stark 3068 SÍ MASCULINO 1963    \n " ,
      " 3 Robert Bruce Banner 2089 SÍ MASCULINO 1963    \n " ,
      " 4 Thor Odinson 2402 SÍ MASCULINO 1963    \n " ,
      " \n " ,
      "                                                Notas   \n " ,
      " 0 Fusionado con Ultron en Rage of Ultron Vol. 1. A...   \n " ,
      " 1 muere en Secret Invasion V1:I8. En realidad fue se...   \n " ,
      " 2 Muerte: \" Más tarde, mientras estaba bajo la influencia de Imm...   \n " ,
      " 3 muere en el arco de Fantasmas del futuro. Sin embargo \" él...   \n " ,
      " 4 Dies in Fear Itself regresa porque eso'...   \n "
     ]
    }
   ],
   "fuente" : [
    " # Muestra las primeras 5 filas del DataFrame. \n " ,
    " \n " ,
    " primeras5filas = vengadores.head(5) \n " ,
    " imprimir(primeras5filas) "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "execution_count" : nulo ,
   "metadatos" : {
    "identificación" : " dGcQ3MUV8hQu " ,
    "etiquetas" : []
   },
   "salidas" : [],
   "fuente" : [
    " # Muestra las primeras 10 filas del DataFrame. \n " ,
    " primeras10filas = vengadores.head(10) \n " ,
    " imprimir(primeras10filas) "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 27 ,
   "metadatos" : {
    "identificación" : " y9RxRXZ98hQu " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      "                                                    URL nombre   \\\n " ,
      " 163 http://marvel.wikia.com/Tony_Masters_(Tierra-616)# Tony Masters    \n " ,
      " 164 http://marvel.wikia.com/Victor_Mancha_(Tierra-6... Víctor Mancha    \n " ,
      " 165 http://marvel.wikia.com/Monica_Chang_(Tierra-616)# Monica Chang    \n " ,
      " 166 http://marvel.wikia.com/Doombot_(Avenger)_(Oído... NaN    \n " ,
      " 167 http://marvel.wikia.com/Alexis_(Tierra-616)# Alexis    \n " ,
      " 168 http://marvel.wikia.com/Eric_Brooks_(Tierra-616)# Eric Brooks    \n " ,
      " 169 http://marvel.wikia.com/Adam_Brashear_(Tierra-6... Adam Brashear    \n " ,
      " 170 http://marvel.wikia.com/Victor_Alvarez_(Tierra-... Victor Alvarez    \n " ,
      " 171 http://marvel.wikia.com/Ava_Ayala_(Tierra-616)# Ava Ayala    \n " ,
      " 172 http://marvel.wikia.com/Kaluu_(Tierra-616)# Kaluu    \n " ,
      " \n " ,
      "      n_apariciones actual genero fecha_inicio   \\\n " ,
      " 163 173 NINGÚN HOMBRE 2013    \n " ,
      " 164 75 SÍ MASCULINO 2013    \n " ,
      " 165 12 SÍ MUJER 2013    \n " ,
      " 166 14 SÍ MASCULINO 2013    \n " ,
      " 167 13 SÍ MUJER 2013    \n " ,
      " 168 198 SÍ MASCULINO 2013    \n " ,
      " 169 29 SÍ MASCULINO 2014    \n " ,
      " 170 45 SÍ MASCULINO 2014    \n " ,
      " 171 49 SÍ MUJER 2014    \n " ,
      " 172 35 SÍ MASCULINO 2015    \n " ,
      " \n " ,
      "                                                  Notas   \n " ,
      " 163 NaN   \n " ,
      " 164 Murió en Avengers_A.I._Vol_1_4. Regresó en Ave...   \n " ,
      " 165 NaN   \n " ,
      " 166 NaN   \n " ,
      " 167 NaN   \n " ,
      " 168 NaN   \n " ,
      " 169 NaN   \n " ,
      " 170 NaN   \n " ,
      " 171 NaN   \n " ,
      " 172 NaN   \n "
     ]
    }
   ],
   "fuente" : [
    " # Muestra las últimas 5 filas del DataFrame. \n " ,
    " ultimas5filas = vengadores.tail(10) \n " ,
    " imprimir(ultimas5filas) \n "
   ]
  },
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "identificación" : " d3xon0_L8hQu "
   },
   "fuente" : [
    " # Tamaño del marco de datos "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 28 ,
   "metadatos" : {
    "identificación" : " DzT5qiVp8hQu " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      " Número de filas: 173 \n " ,
      " Número de columnas: 7 \n "
     ]
    }
   ],
   "fuente" : [
    " # Muestra el tamaño del DataFrame \n " ,
    " tamaño = vengadores.forma \n " ,
    " print( \" Número de filas: \" , tamaño[0]) \n " ,
    " print( \" Número de columnas: \" , tamaño[1]) "
   ]
  },
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "identificación" : " K2B8JwSS8hQv "
   },
   "fuente" : [
    " # Tipos de datos en un DataFrame "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 29 ,
   "metadatos" : {
    "identificación" : " dlQE90uc8hQv " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      " Objeto URL \n " ,
      " nombre objeto \n " ,
      " n_apariciones int64 \n " ,
      " objeto real \n " ,
      " objeto genero \n " ,
      " fecha_inicio int64 \n " ,
      " Objeto de notas \n " ,
      " tipo d: objeto \n "
     ]
    }
   ],
   "fuente" : [
    " # Muestra los tipos de datos del dataframe \n " ,
    " tipos_datos = vengadores.dtypes \n " ,
    " imprimir(tipos_datos) \n "
   ]
  },
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "id" : " TYLapFJL8hQv "
   },
   "fuente" : [
    " # Editar el índice (index) "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 30 ,
   "metadatos" : {
    "id" : " fUayCaep8hQv " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      "                                                             URL   \\\n " ,
      " fecha_inicio                                                       \n " ,
      " 1963 http://marvel.wikia.com/Henry_Pym_(Tierra-616)    \n " ,
      " 1963 http://marvel.wikia.com/Janet_van_Dyne_(Tierra-...    \n " ,
      " 1963 http://marvel.wikia.com/Anthony_Stark_(Tierra-616)    \n " ,
      " 1963 http://marvel.wikia.com/Robert_Bruce_Banner_(E...    \n " ,
      " 1963 http://marvel.wikia.com/Thor_Odinson_(Tierra-616)    \n " ,
      " ... ...    \n " ,
      " 2013 http://marvel.wikia.com/Eric_Brooks_(Tierra-616)#    \n " ,
      " 2014 http://marvel.wikia.com/Adam_Brashear_(Tierra-6...    \n " ,
      " 2014 http://marvel.wikia.com/Victor_Alvarez_(Tierra-...    \n " ,
      " 2014 http://marvel.wikia.com/Ava_Ayala_(Tierra-616)#    \n " ,
      " 2015 http://marvel.wikia.com/Kaluu_(Tierra-616)#    \n " ,
      " \n " ,
      "                                    nombre n_apariciones genero actual   \\\n " ,
      " fecha_inicio                                                               \n " ,
      " 1963 Henry Jonathan \" Hank \ " Pym 1269 SÍ MASCULINO    \n " ,
      " 1963 Janet van Dyne 1165 SÍ MUJER    \n " ,
      " 1963 Anthony Edward \" Tony \" Stark 3068 SÍ MASCULINO    \n " ,
      " 1963 Robert Bruce Banner 2089 SÍ MASCULINO    \n " ,
      " 1963 Thor Odinson 2402 SÍ MASCULINO    \n " ,
      " ... ... ... ... ...    \n " ,
      " 2013 Eric Brooks 198 SÍ MASCULINO    \n " ,
      " 2014 Adam Brashear 29 SÍ HOMBRE    \n " ,
      " 2014 Víctor Álvarez 45 SÍ MASCULINO    \n " ,
      " 2014 Ava Ayala 49 SÍ MUJER    \n " ,
      " 2015 Kaluu 35 SÍ HOMBRE    \n " ,
      " \n " ,
      "                                                           Notas   \n " ,
      " fecha_inicio                                                      \n " ,
      " 1963 Fusionada con Ultrón en Rage of Ultron Vol. 1. A...   \n " ,
      " 1963 Muere en Secret Invasion V1:I8. En realidad fue se...   \n " ,
      " 1963 Muerte: \" Más tarde, mientras estaba bajo la influencia de Imm...   \n " ,
      " 1963 Muere en el arco de Fantasmas del futuro. Sin embargo \" él...   \n " ,
      " 1963 Dies in Fear Itself recuperado porque eso'...   \n " ,
      " ... ...   \n " ,
      " 2013 NaN   \n " ,
      " 2014 NaN   \n " ,
      " 2014 NaN   \n " ,
      " 2014 NaN   \n " ,
      " 2015 NaN   \n " ,
      " \n " ,
      " [173 filas x 6 columnas] \n "
     ]
    }
   ],
   "fuente" : [
    " # Cambia el índice a la columna \" fecha_inicio \" . \n " ,
    " vengadores = vengadores.set_index('fecha_inicio') \n " ,
    " imprimir(vengadores) \n "
   ]
  },
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "identificación" : " uZ5hP6oF8hQv "
   },
   "fuente" : [
    " # Ordenar el índice "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 31 ,
   "metadatos" : {
    "identificación" : " YwrBhJ388hQw " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      "                                                             URL   \\\n " ,
      " fecha_inicio                                                       \n " ,
      " 2015 http://marvel.wikia.com/Kaluu_(Tierra-616)#    \n " ,
      " 2015 http://marvel.wikia.com/Sam_Alexander_(Tierra-6...    \n " ,
      " 2014 http://marvel.wikia.com/Ava_Ayala_(Tierra-616)#    \n " ,
      " 2014 http://marvel.wikia.com/Victor_Alvarez_(Tierra-...    \n " ,
      " 2014 http://marvel.wikia.com/Adam_Brashear_(Tierra-6...    \n " ,
      " ... ...    \n " ,
      " 1900 http://marvel.wikia.com/Emery_Schaub_(Tierra-616)#    \n " ,
      " 1900 http://marvel.wikia.com/James_Santini_(Tierra-6...    \n " ,
      " 1900 http://marvel.wikia.com/Elvin_Haliday_(Tierra-6...    \n " ,
      " 1900 http://marvel.wikia.com/William_Baker_(Tierra-6...    \n " ,
      " 1900 http://marvel.wikia.com/Julie_Power_(Tierra-616)#    \n " ,
      " \n " ,
      "                       nombre n_apariciones genero actual   \\\n " ,
      " fecha_inicio                                                  \n " ,
      " 2015 Kaluu 35 SÍ HOMBRE    \n " ,
      " 2015 Sam Alexander 78 SÍ MASCULINO    \n " ,
      " 2014 Ava Ayala 49 SÍ MUJER    \n " ,
      " 2014 Víctor Álvarez 45 SÍ MASCULINO    \n " ,
      " 2014 Adam Brashear 29 SÍ HOMBRE    \n " ,
      " ... ... ... ... ...    \n " ,
      " 1900 Emery Schaub 26 SÍ HOMBRE    \n " ,
      " 1900 James Santini 40 SÍ MASCULINO    \n " ,
      " 1900 Elvin Haliday 158 NINGÚN HOMBRE    \n " ,
      " 1900 William Baker 355 NINGÚN HOMBRE    \n " ,
      " 1900 Julie Power 153 SÍ MUJER    \n " ,
      " \n " ,
      "                                                           Notas   \n " ,
      " fecha_inicio                                                      \n " ,
      " 2015 NaN   \n " ,
      " 2015 NaN   \n " ,
      " 2014 NaN   \n " ,
      " 2014 NaN   \n " ,
      " 2014 NaN   \n " ,
      " ... ...   \n " ,
      " 1900 NaN   \n " ,
      " 1900 NaN   \n " ,
      " 1900 NaN   \n " ,
      " 1900 Murió en Identity_Disc_Vol_1_1. Más tarde se reveló...   \n " ,
      " 1900 NaN   \n " ,
      " \n " ,
      " [173 filas x 6 columnas] \n "
     ]
    }
   ],
   "fuente" : [
    " # Ordena el índice de forma descendiente \n " ,
    " vengadores = vengadores.sort_index (ascendente = Falso) \n " ,
    " imprimir (vengadores) "
   ]
  },
  {
   "tipo_celda" : " rebaja " ,
   "metadatos" : {
    "identificación" : " kx7ti3P48hQw "
   },
   "fuente" : [
    " #Resetear el indice "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "recuento_ejecución" : 32 ,
   "metadatos" : {
    "identificación" : " KGKNsFiP8hQw " ,
    "etiquetas" : []
   },
   "salidas" : [
    {
     "nombre" : " salida estándar " ,
     "tipo_salida" : " transmisión " ,
     "texto" : [
      "      fecha_inicio URL   \\\n " ,
      " 0 2015 http://marvel.wikia.com/Kaluu_(Tierra-616)#    \n " ,
      " 1 2015 http://marvel.wikia.com/Sam_Alexander_(Tierra-6...    \n " ,
      " 2 2014 http://marvel.wikia.com/Ava_Ayala_(Tierra-616)#    \n " ,
      " 3 2014 http://marvel.wikia.com/Victor_Alvarez_(Tierra-...    \n " ,
      " 4 2014 http://marvel.wikia.com/Adam_Brashear_(Tierra-6...    \n " ,
      " .. ... ...    \n " ,
      " 168 1900 http://marvel.wikia.com/Emery_Schaub_(Tierra-616)#    \n " ,
      " 169 1900 http://marvel.wikia.com/James_Santini_(Tierra-6...    \n " ,
      " 170 1900 http://marvel.wikia.com/Elvin_Haliday_(Tierra-6...    \n " ,
      " 171 1900 http://marvel.wikia.com/William_Baker_(Tierra-6...    \n " ,
      " 172 1900 http://marvel.wikia.com/Julie_Power_(Tierra-616)#    \n " ,
      " \n " ,
      "              nombre n_apariciones genero actual   \\\n " ,
      " 0 Kaluu 35 SÍ MASCULINO    \n " ,
      " 1 Sam Alexander 78 SÍ HOMBRE    \n " ,
      " 2 Ava Ayala 49 SI MUJER    \n " ,
      " 3 Víctor Álvarez 45 SI MASCULINO    \n " ,
      " 4 Adam Brashear 29 SÍ HOMBRE    \n " ,
      " .. ... ... ... ...    \n " ,
      " 168 Emery Schaub 26 SÍ HOMBRE    \n " ,
      " 169 James Santini 40 SÍ HOMBRE    \n " ,
      " 170 Elvin Haliday 158 NINGÚN HOMBRE    \n " ,
      " 171 William Baker 355 NINGÚN HOMBRE    \n " ,
      " 172 Julie Power 153 SÍ MUJER    \n " ,
      " \n " ,
      "                                                  Notas   \n " ,
      " 0 NaN   \n " ,
      " 1 NaN   \n " ,
      " 2 NaN   \n " ,
      " 3 NaN   \n " ,
      " 4 NaN   \n " ,
      " ... ...   \n " ,
      " 168 NaN   \n " ,
      " 169 NaN   \n " ,
      " 170 NaN   \n " ,
      " 171 murió en Identity_Disc_Vol_1_1. Más tarde se reveló...   \n " ,
      " 172 NaN   \n " ,
      " \n " ,
      " [173 filas x 7 columnas] \n "
     ]
    }
   ],
   "fuente" : [
    " # Resetea el índice \n " ,
    " \n " ,
    " vengadores = vengadores.reset_index() \n " ,
    " imprimir (vengadores) "
   ]
  },
  {
   "tipo_celda" : " código " ,
   "execution_count" : nulo ,
   "metadatos" : {},
   "salidas" : [],
   "fuente" : []
  }
],
 "metadatos" : {
  "colaboración" : {
   "procedencia" : []
  },
  "especificación del núcleo" : {
   "display_name" : " Python 3 (ipykernel) " ,
   "idioma" : " pitón " ,
   "nombre" : " python3 "
  },
  "información_idioma" : {
   "codemirror_mode" : {
    "nombre" : " ipython " ,
    "versión" : 3
   },
   "extensión_archivo" : " .py " ,
   "mimetype" : " texto/x-python " ,
   "nombre" : " pitón " ,
   "nbconvert_exporter" : " pitón " ,
   "pygments_lexer" : " ipython3 " ,
   "versión" : " 3.10.9 "
  }
},
 "nbformato" : 4 ,
 "nbformat_minor" : 4
}