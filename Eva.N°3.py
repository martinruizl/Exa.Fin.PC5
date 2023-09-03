{
    "celdas" : [
     {
      "tipo_celda" : " rebaja " ,
      "identificación" : " 9a004934-be26-482d-b9c4-d4cfac05ce29 " ,
      "metadatos" : {
       "identificación" : " 9a004934-be26-482d-b9c4-d4cfac05ce29 "
      },
      "fuente" : [
       " ## Procesamiento de Datos Pandas \n " ,
       " \n " ,
       " Para esta prueba deberá emplear los datos del archivo candidatos.csv para lo cual deberá: \n " ,
       " \n " ,
       " 1. Almanecar los datos en una base de datos. (Asegurar el almacenamiento con el tipo de dato apropiado) \n " ,
       " 2. A partir de la lectura de los datos deberá generar un informe de procesamiento. \n " ,
       "     \n " ,
       "     (Cree el proceso que considere más conveniente, realicelo más complejo que le sea posible) \n " ,
       "     \n " ,
       " 3. Realizar un código de envío de correos integrado en su solución. \n " ,
       " \n " ,
       " \n " ,
       " El archivo candidatos.csv contiene 50k filas de datos sobre candidatos. Los campos que estamos usando son: \n " ,
       " - Nombre \n " ,
       " - Apellido \n " ,
       " - Correo electrónico \n " ,
       " - País \n " ,
       " - Fecha de solicitud \n " ,
       " - Yoe (años de experiencia) \n " ,
       " - Antigüedad \n " ,
       " - Tecnología \n " ,
       " - Puntuación del desafío de código \n " ,
       " - Entrevista técnica \n "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 4 ,
      "identificación" : " 59cd2be4-533a-46cd-a117-0903c90a97e9 " ,
      "metadatos" : {
       "identificación" : " 59cd2be4-533a-46cd-a117-0903c90a97e9 " ,
       "id de salida" : " 94e20d73-fa0f-4d47-d630-8110ef980fdb "
      },
      "salidas" : [
       {
        "nombre" : " salida estándar " ,
        "tipo_salida" : " transmisión " ,
        "texto" : [
         " Requisito ya satisfecho: pandas en c: \\ users \\ 51966 \\ anaconda3 \\ lib \\ site-packages (1.5.3) \n " ,
         " Requisito ya satisfecho: python-dateutil>=2.8.1 en c: \\ users \\ 51966 \\ anaconda3 \\ lib \\ site-packages (de pandas) (2.8.2) \n " ,
         " Requisito ya satisfecho: pytz>=2020.1 en c: \\ users \\ 51966 \\ anaconda3 \\ lib \\ site-packages (de pandas) (2022.7) \n " ,
         " Requisito ya satisfecho: numpy>=1.21.0 en c: \\ users \\ 51966 \\ anaconda3 \\ lib \\ site-packages (de pandas) (1.23.5) \n " ,
         " Requisito ya satisfecho: seis>=1.5 en c: \\ usuarios \\ 51966 \\ anaconda3 \\ lib \\ site-packages (de python-dateutil>=2.8.1->pandas) (1.16.0) \n "
        ]
       }
      ],
      "fuente" : [
       " importar pandas como pd \n " ,
       " !pip instalar pandas \n " ,
       " df_candidates = pd.read_csv('C: \\\\ Usuarios \\\\ 51966 \\\\ datos \\\\ candidatos.csv') "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 5 ,
      "identificación" : " 5289e29f-ba7a-48e3-b884-9a7d56b4f71b " ,
      "metadatos" : {
       "identificación" : " 5289e29f-ba7a-48e3-b884-9a7d56b4f71b "
      },
      "salidas" : [
       {
        "nombre" : " salida estándar " ,
        "tipo_salida" : " transmisión " ,
        "texto" : [
         "       Nombre;Apellido;Correo electrónico;Fecha de solicitud;País;YOE;Antigüedad;Tecnología;Puntuación del desafío del código;Puntuación de la entrevista técnica \n " ,
         " 0 Bernadette;Langworth;leonard91@yahoo.com;2021-...                                                                          \n " ,
         " 1 Camryn;Reynolds;zelda56@hotmail.com;2021-09-09...                                                                          \n " ,
         " 2 Larue;Spinka;okey_schultz41@gmail.com;2020-04-...                                                                          \n " ,
         " 3 Arco;Spinka;elvera_kulas@yahoo.com;2020-10-01;...                                                                          \n " ,
         " 4 Larue;Altenwerth;minnie.gislason@gmail.com;202...                                                                          \n " ,
         " ... ...                                                                          \n " ,
         " 49995 Betania;Escudos;rocky_mitchell@hotmail.com;202...                                                                          \n " ,
         " 49996 Era;Swaniawski;dolores.roob@hotmail.com;2020-0...                                                                          \n " ,
         " 49997 Martín;Lakin;savanah.stracke@gmail.com;2018-12...                                                                          \n " ,
         " 49998 Aliya;Abernathy;vivienne.fritsch@yahoo.com;202...                                                                          \n " ,
         " 49999 Coleman;Wisozk;abigayle.crooks@yahoo.com;2022-...                                                                          \n " ,
         " \n " ,
         " [50000 filas x 1 columnas] \n "
        ]
       }
      ],
      "fuente" : [
       " imprimir(df_candidatos) "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 7 ,
      "identificación" : " a3761f9f-9685-4c4f-bc03-f334cc78599f " ,
      "metadatos" : {
       "identificación" : " a3761f9f-9685-4c4f-bc03-f334cc78599f "
      },
      "salidas" : [
       {
        "ename" : " Error de base de datos " ,
        "evalue" : " La ejecución falló en sql ' \n     SELECCIONAR País, AVG(Yoe) AS Average_Yoe \n     FROM candidatos \n     GROUP BY Country \n     ORDER BY Average_Yoe DESC \n     LIMIT 10 \n ': no ​​existe tal columna: País " ,
        "tipo_salida" : " error " ,
        "rastreo" : [
         " \u001b [1;31m------------------------------------------- -------------------------------- \u001b [0m " ,
         " \u001b [1;31mOperationalError \u001b [0m Traceback (última llamada más reciente) " ,
         " Archivo \u001b [1;32m~ \\ anaconda3 \\ lib \\ site-packages \\ pandas \\ io \\ sql.py:2018 \u001b [0m, en \u001b [0;36mSQLiteDatabase.execute \u001b [ 1;34m(self, *args, **kwargs) \u001b [0m \n \u001b [0;32m 2017 \u001b [0m \u001b [38;5;28;01mtry \u001b [39;00m: \n \ u001b [1;32m-> 2018 \u001b [0m cur \u001b [38;5;241m. \u001b [39mexecute(\u001b [38;5;241m* \u001b [39margs, \u001b [38;5;241m* \u001b [39m \u001b [38;5;241m* \u001b [39mkwargs) \n \u001b [0;32m 2019 \u001b [0m      \u001b [38;5;28;01mreturn \u001b [39;00m cur \n " ,
         " \u001b [1;31mOperationalError \u001b [0m: no existe tal columna: País " ,
         " \n La excepción anterior fue la causa directa de la siguiente excepción: \n " ,
         " \u001b [1;31mDatabaseError \u001b [0m Traceback (última llamada más reciente) " ,
         "Celda \u001b[1;32mIn[7], línea 25\u001b[0m\n\u001b[0;32m 17\u001b[0m \u001b[38;5;66;03m# Ejemplo de procesamiento y generación de reporte\ u001b[39;00m\n\u001b[0;32m 18\u001b[0m consulta \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m''\u001b[39m\n\ u001b[0;32m 19\u001b[0m \u001b[38;5;124m SELECCIONAR País, PROMEDIO(Yoe) COMO Promedio_Yoe\u001b[39m\n\u001b[0;32m 20\u001b[0m \u001b[38;5 ;124m DE candidatos\u001b[39m\n\u001b[1;32m (...)\u001b[0m\n\u001b[0;32m 23\u001b[0m \u001b[38;5;124m LÍMITE 10\u001b [39m\n\u001b[0;32m 24\u001b[0m \u001b[38;5;124m'''\u001b [39m\n\u001b[1;32m---> 25\u001b[0m df_report \u001b [38;5;241m=\u001b[39m \u001b[43mpd\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mread_sql_query\u001b[49m\u001b[43m(\ u001b[49m\u001b[43mconsulta\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mconn\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m 27\u001b[0m \u001b[38;5;66 ;03m# Cierra la conexión con la base de datos\u001b[39;00m\n\u001b[0;32m 28\u001b[0m conn\u001b[38;5;241m.\u001b[39mclose()\n",
         "Archivo \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\sql.py:397\u001b[0m, en \u001b[0;36mread_sql_query\u001b[1; 34m(sql, con, index_col, coerce_float, params, parse_dates, chunksize, dtype)\u001b[0m\n\u001b[0;32m 339\u001b[0m \u001b[38;5;124;03m\"\"\ "\u001b[39;00m\n\u001b[0;32m 340\u001b[0m \u001b[38;5;124;03mLeer consulta SQL en un DataFrame.\u001b[39;00m\n\u001b[0;32m 341\u001b[0m \n\u001b[1;32m (...)\u001b[0m\n\u001b[0;32m 394\u001b[0m \u001b[38;5;124;03parámetro se convertirá a UTC .\u001b[39;00m\n\u001b[0;32m 395\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m 396\u001b[0m pandas_sql \u001b[38;5;241m=\u001b[39m pandasSQL_builder(con)\n\u001b[1;32m--> 397\u001b[0m \u001b[38;5;28;01mreturn\ u001b[39;00m\u001b[43mpandas_sql\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mread_query\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m 398\u001b[0m \u001b[43m \u001b[49m\u001b[43msql\u001b [49m\u001b[43m,\u001b[49m\n\u001b[0;32m 399\u001b[0m \u001b[43m \u001b[49m\u001b[43mindex_col\u001b[49m\u001b[38;5;241;43m =\u001b[39;49m\u001b[43mindex_col\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m 400\u001b[0m \u001b[43m\u001b[49m\u001b[43mparams\ u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mparams\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m 401\u001b[0m \u001b[43m \u001b[49m\u001b[43mcoerce_float\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mcoerce_float\u001b[49m\u001b[43m,\u001b [49m \n\u001b[0;32m 402\u001b[0m \u001b [43m \u001b[49m\u001b[43mparse_dates\u001b [49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mparse_dates \u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m 403\u001b[0m \u001b[43m \u001b[49m\u001b[43mchunksize\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m \u001b[43mchunksize\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m 404\u001b[0m \u001b[43m \u001b[49m\u001b[43mdtype\u001b[49m\u001b[38 ;5;241;43m=\u001b[39;49m\u001b[43mdtype\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m 405\u001b[0m \u001b[43m\u001b[ 49m\u001b[43m)\u001b[49m\n",
         "Archivo \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\sql.py:2078\u001b[0m, en \u001b[0;36mSQLiteDatabase.read_query\u001b[ 1;34m(self, sql, index_col, coerce_float, params, parse_dates, chunksize, dtype)\u001b[0m\n\u001b[0;32m 2066\u001b[0m \u001b[38;5;28;01mdef\u001b[ 39;00m \u001b[38;5;21mread_query\u001b[39m(\n\u001b[0;32m 2067\u001b[0m \u001b[38;5;28mself\u001b[39m,\n\u001b[0;32m 2068\u001b[0m sql,\n\u001b[1;32m (...)\u001b[0m\n\u001b[0;32m 2074\u001b[0m dtype: DtypeArg \u001b[38;5;241m|\ u001b[39m \u001b[38;5;28;01mNinguno\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNinguno\u001b[39;00m,\ n\u001b[0;32m 2075\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m DataFrame \u001b[38;5;241m|\ u001b[39m Iterador[Marco de datos]:\n\u001b[0;32m 2077\u001b[0m args \u001b[38;5;241m=\u001b[39m _convert_params(sql, params)\n\u001b[1;32m-> 2078\u001b[0m cursor \ u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mexecute\ u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m)\u001b[49m\n\u001b [0;32m 2079\u001b[0m columnas \u001b[38;5;241m=\u001b[39m [col_desc[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;28;01mfor\ u001b[39;00m col_desc \u001b[38;5;129;01min\u001b[39;00m cursor\u001b[38;5;241m.\u001b[39mdescription]\n\u001b[0;32m 2081\u001b[0m \u001b[38;5;28;01mif\u001b [39;00m tamaño de trozo \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \ u001b[38;5;28;01mNinguno\u001b[39;00m:\n",params)\n\u001b[1;32m-> 2078\u001b[0m cursor \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[ 38;5;241;43m.\u001b[39;49m\u001b [43mejecutar\u001b [49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b [43margs\u001b[49m\u001b[43m)\u001b [49m\n\u001b[0;32m 2079\u001b[0m columnas \u001b[38;5;241m=\u001b[39m [col_desc[\u001b[38; 5;241m0\u001b[39m] \u001b[38;5;28;01mfor\u001b[39;00m col_desc \u001b[38;5;129;01min\u001b[39;00m cursor\u001b[38;5;241m .\u001b[39mdescripción]\n\u001b[0;32m 2081\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m tamaño de fragmento \u001b[38;5;129;01mis\u001b[39 ;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNinguno\u001b[39;00m:\n",params)\n\u001b[1;32m-> 2078\u001b[0m cursor \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[ 38;5;241;43m.\u001b[39;49m\u001b [43mejecutar\u001b [49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b [43margs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m 2079\u001b[0m columnas \u001b[38;5;241m=\u001b[39m [col_desc[\u001b[38; 5;241m0\u001b[39m] \u001b[38;5;28;01mfor\u001b[39;00m col_desc \u001b[38;5;129;01min\u001b[39;00m cursor\u001b[38;5;241m .\u001b[39mdescripción]\n\u001b[0;32m 2081\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m tamaño de fragmento \u001b[38;5;129;01mis\u001b[39 ;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNinguno\u001b[39;00m:\n",\u001b[39;49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b [43m)\u001b[49m\n\u001b[0;32m 2079\u001b[0m columnas \u001b[38;5;241m=\u001b[39m [col_desc[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;28;01mfor\u001b[39;00m col_desc \u001b[38;5;129;01min\u001b[39;00m cursor\u001b[38;5;241m.\u001b[39mdescription]\n \u001b[0;32m 2081\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m tamaño de trozo \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5 ;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNinguno\u001b[39;00m:\n",\u001b[39;49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b [43m)\u001b[49m\n\u001b[0;32m 2079\u001b[0m columnas \u001b[38;5;241m=\u001b[39m [col_desc[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;28;01mfor\u001b[39;00m col_desc \u001b[38;5;129;01min\u001b[39;00m cursor\u001b[38;5;241m.\u001b[39mdescription]\n \u001b[0;32m 2081\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m tamaño de trozo \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5 ;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNinguno\u001b[39;00m:\n",\u001b[39mdescripción]\n\u001b[0;32m 2081\u001b[0m \u001b[38;5;28;01mif\u001b [39;00m tamaño de fragmento\u001b[38;5;129;01mis\u001b[39; 00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNinguno\u001b[39;00m:\n",\u001b[39mdescripción]\n\u001b[0;32m 2081\u001b[0m \u001b[38;5;28;01mif\u001b [39;00m tamaño de fragmento\u001b[38;5;129;01mis\u001b[39; 00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNinguno\u001b[39;00m:\n",
         " Archivo \u001b [1;32m~ \\ anaconda3 \\ lib \\ site-packages \\ pandas \\ io \\ sql.py:2030 \u001b [0m, en \u001b [0;36mSQLiteDatabase.execute \u001b [ 1;34m(self, *args, **kwargs) \u001b [0m \n \u001b [0;32m 2027 \u001b [0m      \u001b [38;5;28;01mraise \u001b [39;00m ex \u001b [ 38;5;28;01mdesde \u001b [39;00m \u001b [38;5;21;01minner_exc \u001b [39;00m\n \u001b [0;32m 2029 \u001b [0m ex \u001b [38;5;241m= \u001b [39m DatabaseError( \u001b [38;5;124mf \ u001b [39m \u001b [38;5;124m \ " \u001b [39m \u001b [38;5;124mLa ejecución falló en sql \u001b [39m \u001b [38;5;124m' \ u001b [39m \ u001b [38;5;132;01m{ \u001b [39;00margs [ \u001b [38;5;241m0 \u001b [39m] \u001b [38;5;132;01m} \u001b [39;00m \u001b [38;5;124m'\u001b [39m \u001b [38;5;124m: \u001b [39m \u001b [38;5;132;01m{ \u001b [39;00mexc \u001b [38;5;132;01m} \u001b [39; 00m \u001b [38;5;124m \" \u001b [39m) \n \u001b [1;32m-> 2030 \u001b [0m \u001b [38;5;28;01mraise \u001b [39;00m ex \u001b [38;5;28;01mfrom \u001b [39;00m \u001b [38;5;21;01mexc \u001b [39;00m \n " ,
         " \u001b [1;31mDatabaseError \u001b [0m: Error de ejecución en sql ' \n     SELECCIONAR País, AVG(Yoe) AS Average_Yoe \n     FROM candidatos \n     GRUPO POR País \n     ORDEN POR Average_Yoe DESC \n     LIMIT 10 \n ' : no existe tal columna: País "
        ]
       }
      ],
      "fuente" : [
       " importar pandas como pd \n " ,
       " importar sqlite3 \n " ,
       " \n " ,
       " # Lee el archivo CSV y carga los datos en un DataFrame \n " ,
       " df_candidates = pd.read_csv('C: \\\\ Usuarios \\\\ 51966 \\\\ datos \\\\ candidatos.csv') \n " ,
       " # Crea una conexión con la base de datos SQLite \n " ,
       " conexión = sqlite3.connect('candidates.db') \n " ,
       " \n " ,
       " # Almacena los datos en una tabla de la base de datos \n " ,
       " df_candidates.to_sql('candidatos', conexión, if_exists='reemplazar', index=False) \n " ,
       " \n " ,
       " # Cierra la conexión con la base de datos \n " ,
       " conexión.close() \n " ,
       " # Vuelve a abrir la conexión con la base de datos SQLite \n " ,
       " conexión = sqlite3.connect('candidates.db') \n " ,
       " \n " ,
       " # Ejemplo de procesamiento y generación de informes \n " ,
       " consulta = ''' \n " ,
       "     SELECCIONAR País, PROMEDIO(Yoe) COMO Promedio_Yoe \n " ,
       "     DE candidatos \n " ,
       "     GRUPO POR País \n " ,
       "     ORDENAR POR Promedio_Yoe DESC \n " ,
       "     LÍMITE 10 \n " ,
       " ''' \n " ,
       " df_report = pd.read_sql_query(consulta, conexión) \n " ,
       " \n " ,
       " # Cierra la conexión con la base de datos \n " ,
       " conexión.close() \n " ,
       " \n " ,
       " # Muestra el informe \n " ,
       " imprimir(df_report) \n " ,
       " importar smtplib \n " ,
       " de email.mime.text importar MIMEText \n " ,
       " \n " ,
       " def enviar_correo electrónico (marco de datos): \n " ,
       "     # Configuración del servidor SMTP y las credenciales \n " ,
       "     smtp_host = 'smtp.example.com' \n " ,
       "     smtp_port = 587 \n " ,
       "     nombre de usuario = 'tu_correo electrónico@ejemplo.com' \n " ,
       "     contraseña = 'tu_contraseña' \n " ,
       " \n " ,
       "     # Construcción del contenido del correo electrónico \n " ,
       "     asunto = 'Informe de candidatos' \n " ,
       "     cuerpo = dataframe.to_html(index=False) \n " ,
       " \n " ,
       "     # Creación del objeto MIMEText \n " ,
       "     mensaje = MIMEText(cuerpo, 'html') \n " ,
       "     mensaje['Asunto'] = asunto \n " ,
       "     msj['De'] = nombre de usuario \n " ,
       "     msj['Para'] = 'destinatario@ejemplo.com' \n " ,
       " \n " ,
       "     # Envío del correo electrónico \n " ,
       "     con smtplib.SMTP(smtp_host, smtp_port) como servidor: \n " ,
       "         servidor.starttls() \n " ,
       "         servidor.login(nombre de usuario, contraseña) \n " ,
       "         servidor.send_message(msg) \n " ,
       " \n " ,
       " # Llamada a la función de envío de correo electrónico \n " ,
       " enviar_correo electrónico(df_report) \n "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "execution_count" : nulo ,
      "identificación" : " 998095ad-cfc2-435a-be27-331774ec36f8 " ,
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
    "nbformat_minor" : 5
   }s