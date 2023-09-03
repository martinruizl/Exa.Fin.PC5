{
    "celdas" : [
     {
      "tipo_celda" : " rebaja " ,
      "metadatos" : {
       "identificación" : " QFRdsO7aJRhd "
      },
      "fuente" : [
       " # Ejercicio - Busqueda de Alojamiento en Airbnb. \n " ,
       " \n " ,
       " Supongamos que somos un agente de [Airbnb](http://www.airbnb.com) localizado en Lisboa, y tenemos que atender solicitudes de varios clientes. Tenemos un archivo llamado `airbnb.csv` (en la carpeta data) donde Tenemos información de todos los alojamientos de Airbnb en Lisboa. "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 2 ,
      "metadatos" : {
       "id" : " DjibxhdiJRhj "
      },
      "salidas" : [],
      "fuente" : [
       " importar pandas como pd \n " ,
       " df_airbnb = pd.read_csv('C: \\\\ Usuarios \\\\ 51966 \\\\ datos \\\\ airbnb.csv') "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 3 ,
      "metadatos" : {
       "identificación" : " fpwgf0b6JRhl " ,
       "ID de salida" : " aa85991b-0216-4cf2-839f-7aa61c31df32 "
      },
      "salidas" : [
       {
        "datos" : {
         "texto/html" : [
          " <div> \n " ,
          " <ámbito de estilo> \n " ,
          "     .dataframe tbody tr th:solo de tipo { \n " ,
          "         alineación vertical: medio; \n " ,
          "     } \n " ,
          " \n " ,
          "     .dataframe tbody tr th { \n " ,
          "         alineación vertical: arriba; \n " ,
          "     } \n " ,
          " \n " ,
          "     .dataframe thead th { \n " ,
          "         alineación de texto: derecha; \n " ,
          "     } \n " ,
          " </estilo> \n " ,
          " <borde de tabla= \" 1 \" clase= \" marco de datos \" > \n " ,
          "   <cabeza> \n " ,
          "     <tr estilo= \" text-align: right; \" > \n " ,
          "       <th></th> \n " ,
          "       <th>room_id</th> \n " ,
          "       <th>host_id</th> \n " ,
          "       <th>tipo_habitación</th> \n " ,
          "       <th>barrio</th> \n " ,
          "       <th>opiniones</th> \n " ,
          "       <th>satisfacción_general</th> \n " ,
          "       <th>acomoda</th> \n " ,
          "       <th>dormitorios</th> \n " ,
          "       <th>precio</th> \n " ,
          "     </tr> \n " ,
          "   </thead> \n " ,
          "   <tbody> \n " ,
          "     <tr> \n " ,
          "       <th>0</th> \n " ,
          "       <td>6499</td> \n " ,
          "       <td>14455</td> \n " ,
          "       <td>Casa/apto. completo</td> \n " ,
          "       <td>Belém</td> \n " ,
          "       <td>8</td> \n " ,
          "       <td>5.0</td> \n " ,
          "       <td>2</td> \n " ,
          "       <td>1.0</td> \n " ,
          "       <td>57.0</td> \n " ,
          "     </tr> \n " ,
          "     <tr> \n " ,
          "       <th>1</th> \n " ,
          "       <td>17031</td> \n " ,
          "       <td>66015</td> \n " ,
          "       <td>Casa/apto. completo</td> \n " ,
          "       <td>Alvalade</td> \n " ,
          "       <td>0</td> \n " ,
          "       <td>0.0</td> \n " ,
          "       <td>2</td> \n " ,
          "       <td>1.0</td> \n " ,
          "       <td>46.0</td> \n " ,
          "     </tr> \n " ,
          "     <tr> \n " ,
          "       <th>2</th> \n " ,
          "       <td>25659</td> \n " ,
          "       <td>107347</td> \n " ,
          "       <td>Casa/apto. completo</td> \n " ,
          "       <td>Santa María Mayor</td> \n " ,
          "       <td>63</td> \n " ,
          "       <td>5.0</td> \n " ,
          "       <td>3</td> \n " ,
          "       <td>1.0</td> \n " ,
          "       <td>69.0</td> \n " ,
          "     </tr> \n " ,
          "     <tr> \n " ,
          "       <th>3</th> \n " ,
          "       <td>29248</td> \n " ,
          "       <td>125768</td> \n " ,
          "       <td>Casa/apto. completo</td> \n " ,
          "       <td>Santa María Mayor</td> \n " ,
          "       <td>225</td> \n " ,
          "       <td>4.5</td> \n " ,
          "       <td>4</td> \n " ,
          "       <td>1.0</td> \n " ,
          "       <td>58.0</td> \n " ,
          "     </tr> \n " ,
          "     <tr> \n " ,
          "       <th>4</th> \n " ,
          "       <td>29396</td> \n " ,
          "       <td>126415</td> \n " ,
          "       <td>Casa/apto. completo</td> \n " ,
          "       <td>Santa María Mayor</td> \n " ,
          "       <td>132</td> \n " ,
          "       <td>5.0</td> \n " ,
          "       <td>4</td> \n " ,
          "       <td>1.0</td> \n " ,
          "       <td>67.0</td> \n " ,
          "     </tr> \n " ,
          "   </tbody> \n " ,
          " </tabla> \n " ,
          " </div> "
         ],
         "texto/sin formato" : [
          "    room_id host_id room_type reseñas de vecindario   \\\n " ,
          " 0 6499 14455 Casa entera/apto Belém 8    \n " ,
          " 1 17031 66015 Casa entera/apto. Alvalade 0    \n " ,
          " 2 25659 107347 Casa entera/apto. Santa Maria Maior 63    \n " ,
          " 3 29248 125768 Casa entera/apto. Santa Maria Maior 225    \n " ,
          " 4 29396 126415 Casa entera/apto. Santa Maria Maior 132    \n " ,
          " \n " ,
          "    global_satisfaction se adapta al precio de las habitaciones   \n " ,
          " 0 5,0 2 1,0 57,0   \n " ,
          " 1 0,0 2 1,0 46,0   \n " ,
          " 2 5,0 3 1,0 69,0   \n " ,
          " 3 4,5 4 1,0 58,0   \n " ,
          " 4 5,0 4 1,0 67,0   "
         ]
        },
        "recuento_ejecución" : 3 ,
        "metadatos" : {},
        "tipo_salida" : " resultado_ejecución "
       }
      ],
      "fuente" : [
       " df_airbnb.head() "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 4 ,
      "metadatos" : {
       "identificación" : " f4ThNafjJRhm " ,
       "ID de salida" : " 11807043-94f1-44bb-d619-676b069ea776 "
      },
      "salidas" : [
       {
        "datos" : {
         "texto/sin formato" : [
          " room_id int64 \n " ,
          " host_id int64 \n " ,
          " objeto tipo_habitación \n " ,
          " objeto de vecindad \n " ,
          " revisa int64 \n " ,
          " satisfacción_general float64 \n " ,
          " se adapta a int64 \n " ,
          " dormitorios float64 \n " ,
          " precio float64 \n " ,
          " tipo d: objeto "
         ]
        },
        "recuento_ejecución" : 4 ,
        "metadatos" : {},
        "tipo_salida" : " resultado_ejecución "
       }
      ],
      "fuente" : [
       " df_airbnb.dtypes "
      ]
     },
     {
      "tipo_celda" : " rebaja " ,
      "metadatos" : {
       "identificación" : " qHp3aDXZJRhn "
      },
      "fuente" : [
       " En concreto el conjunto de datos tiene las siguientes variables: \n " ,
       " - room_id: el identificador de la propiedad \n " ,
       " - host_id: el identificador del dueño de la propiedad \n " ,
       " - tipo_habitación: tipo de propiedad (vivienda completa/(habitación para compartir/habitación privada) \n " ,
       " - barrio: el barrio de Lisboa \n " ,
       " - reseñas: El numero de opiniones \n " ,
       " - global_satisfaction: Puntuación media del apartamento \n " ,
       " - acomoda: El numero de personas que se pueden alojar en la propiedad \n " ,
       " - dormitorios: El número de habitaciones \n " ,
       " - precio: El precio (en euros) por noche "
      ]
     },
     {
      "tipo_celda" : " rebaja " ,
      "metadatos" : {
       "id" : " FytFtWUsJRho "
      },
      "fuente" : [
       " ## Usando pandas "
      ]
     },
     {
      "tipo_celda" : " rebaja " ,
      "metadatos" : {
       "identificación" : " ugPnas8EJRhp "
      },
      "fuente" : [
       " ### Caso 1. \n " ,
       " \n " ,
       " Alicia va a ir a Lisboa durante una semana con su marido y sus 2 hijos. Están buscando un apartamento con habitaciones separadas para los padres y los hijos. No les importa donde se hospedaron o el precio, simplemente quieren tener una experiencia agradable. Esto significa que solo aceptan lugares con más de 10 críticas con una puntuación mayor de 4. Cuando seleccionamos habitaciones para Alicia, tenemos que asegurarnos de ordenar las habitaciones de mejor a peor puntuación. Para aquellas habitaciones que tienen la misma puntuación, debemos mostrar antes aquellas con más críticas. Debemos darle 3 alternativas. "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 5 ,
      "metadatos" : {
       "identificación" : " 2Bb-BJ5_JRhq "
      },
      "salidas" : [
       {
        "nombre" : " salida estándar " ,
        "tipo_salida" : " transmisión " ,
        "texto" : [
         "       room_id host_id room_type reseñas de vecindario   \\\n " ,
         " 120 176153 842219 Casa entera/apto Misericórdia 438    \n " ,
         " 1369 1745355 9186518 Casa entera/apto. Olivais 419    \n " ,
         " 16 44043 192830 Casa entera/apto. Santa Maria Maior 316    \n " ,
         " \n " ,
         "       global_satisfaction se adapta al precio de las habitaciones   \n " ,
         " 120 5,0 4 2,0 ​​102,0   \n " ,
         " 1369 4,5 5 2,0 50,0   \n " ,
         " 16 5,0 7 3,0 80,0   \n "
        ]
       }
      ],
      "fuente" : [
       " df_filtrado = df_airbnb[df_airbnb['dormitorios'] > 1] \n " ,
       " df_filtrado = df_filtrado[(df_filtrado['reviews'] > 10) & (df_filtrado['overall_satisfaction'] > 4)] \n " ,
       " df_ordenado = df_filtrado.sort_values(by=['reviews', 'overall_satisfaction'], ascending=[False, False]) \n " ,
       " alternativas = df_ordenado.head(3) \n " ,
       " imprimir(alternativas) \n " ,
       " \n " ,
       " \n " ,
       " \n "
      ]
     },
     {
      "tipo_celda" : " rebaja " ,
      "metadatos" : {
       "id" : " sEtivcU_JRhq "
      },
      "fuente" : [
       " ### Caso 2 \n " ,
       " \n " ,
       " Roberto es un casero que tiene una casa en Airbnb. De vez en cuando nos llama preguntando sobre cuáles son las críticas de su alojamiento. Hoy está particularmente enfadado, ya que su hermana Clara ha puesto una casa en Airbnb y Roberto quiere asegurarse de que su casa tiene más críticas que las de Clara. Tenemos que crear un dataframe con las propiedades de ambos. Las id de las casas de Roberto y Clara son 97503 y 90387 respectivamente. Finalmente guardamos este dataframe como excel llamado \ " roberto.xls "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 6 ,
      "metadatos" : {
       "identificación" : " lIZ_kTnXJRhr " ,
       "etiquetas" : []
      },
      "salidas" : [],
      "fuente" : [
       " datos_roberto = df_airbnb[df_airbnb['room_id'] == 97503] \n " ,
       " datos_clara = df_airbnb[df_airbnb['room_id'] == 90387] \n " ,
       " df_propiedades = pd.concat([datos_roberto, datos_clara]) "
      ]
     },
     {
      "tipo_celda" : " rebaja " ,
      "metadatos" : {
       "id" : " uLzCBtabJRhr "
      },
      "fuente" : [
       " \n " ,
       " ### Caso 3 \n " ,
       " \n " ,
       " Diana va a Lisboa a pasar 3 noches y quiere conocer a gente nueva. Tiene un presupuesto de 50€ para su alojamiento. Debemos buscarle las 10 propiedades más baratas, dandole preferencia a aquellas que sean habitaciones compartidas *(room_type == Shared room) *, y para aquellas viviendas compartidas debemos elegir aquellas con mejor puntuación. "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 9 ,
      "metadatos" : {
       "identificación" : " Xzg1uKFDJRhs " ,
       "etiquetas" : []
      },
      "salidas" : [
       {
        "nombre" : " salida estándar " ,
        "tipo_salida" : " transmisión " ,
        "texto" : [
         "         room_id host_id room_type reseñas de vecindario   \\\n " ,
         " 1010 1179457 5799522 Habitación compartida Santo António 42    \n " ,
         " 3562 5557699 28812904 Habitación compartida Santa Maria Maior 22    \n " ,
         " 7584 13116032 72951043 Habitación compartida Arroios 1    \n " ,
         " 13148 19314160 135270245 Habitación compartida Santa Clara 0    \n " ,
         " 9065 14933182 91501272 Habitación compartida Santo António 5    \n " ,
         " 4353 6728244 28812904 Habitación compartida Santa Maria Maior 8    \n " ,
         " 5616 9317561 48360716 Habitación compartida Arroios 13    \n " ,
         " 6640 11693356 28812904 Habitación compartida Santa Maria Maior 3    \n " ,
         " 6641 11693442 28812904 Habitación compartida Santa Maria Maior 16    \n " ,
         " 8908 14708916 91501272 Habitación compartida Santo António 18    \n " ,
         " \n " ,
         "        global_satisfaction se adapta al precio de las habitaciones   \n " ,
         " 1010 4,0 16 1,0 10,0   \n " ,
         " 3562 4,0 1 1,0 10,0   \n " ,
         " 7584 0,0 8 1,0 10,0   \n " ,
         " 13148 0,0 1 1,0 10,0   \n " ,
         " 9065 5,0 8 1,0 11,0   \n " ,
         " 4353 4,5 1 1,0 11,0   \n " ,
         " 5616 4,5 4 1,0 11,0   \n " ,
         " 6640 4,5 1 1,0 11,0   \n " ,
         " 6641 4,5 1 1,0 11,0   \n " ,
         " 8908 4,5 4 1,0 11,0   \n "
        ]
       }
      ],
      "fuente" : [
       " propiedades_compartidas = df_airbnb[(df_airbnb['room_type'] == 'Habitación compartida')] \n " ,
       " \n " ,
       " propiedades_ordenadas = propiedades_compartidas.sort_values(by=['price', 'overall_satisfaction'], ascending=[True, False]) \n " ,
       " \n " ,
       " propiedades_baratas = propiedades_ordenadas.head(10) \n " ,
       " \n " ,
       " imprimir(propiedades_baratas) "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "execution_count" : nulo ,
      "metadatos" : {
       "identificación" : " SUL3hjq8JRht "
      },
      "salidas" : [],
      "fuente" : []
     },
     {
      "tipo_celda" : " rebaja " ,
      "metadatos" : {
       "identificación" : " ArL1NJCKJRht "
      },
      "fuente" : [
       " ## Usando MatPlot "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 10 ,
      "metadatos" : {
       "identificación" : " OXung2vcJRht "
      },
      "salidas" : [],
      "fuente" : [
       " importar matplotlib.pyplot como plt "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 11 ,
      "metadatos" : {
       "id" : " h0mnikWcJRhu "
      },
      "salidas" : [],
      "fuente" : [
       " %matplotlib en línea "
      ]
     },
     {
      "tipo_celda" : " rebaja " ,
      "metadatos" : {
       "identificación" : " hXxRZJ_DJRhu "
      },
      "fuente" : [
       " ### Caso 1. \n " ,
       " \n " ,
       " Realizar un gráfico circular, de la cantidad de tipo de habitaciones `room_type`   "
      ]
     },
     {
      "tipo_celda" : " código " ,
      "recuento_ejecución" : 12 ,
      "metadatos" : {
       "identificación" : " dH9h2OzwJRhu "
      },
      "salidas" : [
       {
        "datos" : {
         "imagen/png":"iVBORw0KGgoAAAANSUhEUgAAAoAAAAH3CAYAAAArAu7HAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQ GoP6dpAABmuklEQVR4nO3dd3xT5eI/8M9pdnfS0tIBLWWvsvcGEUQUAUVlf1Wue13Bq/5kOS6ict2i1wFeARUVEBBBQUSQvbfMMrv3SrPO74/aSGhLd5+c5PN+vfKCJifJJ+n69DnnPI8ky7IMIiIiI vIaPqIDEBEREVH9YgEkIiIi8jIsgERERERehgWQiIiIyMuwABIRERF5GRZAIiIiIi/DAkhERETkZVgAiYiIiLwMCyARERGRl2EBJPJQ//znPxEVFYVLly6JjkJERG6GBZDcxuLFiyFJkvOi1+vRsGFDDBo0C PPmzUNKSkqp+8yZMweSJFXpeQoKCjBnzhz89ttvVbpfWc8VGxuLkSNHVulxakNFr3vlypX4/PPP8dNPP6FRo0b1kkmSJMyZM6fGj1Py2iq6DBw4EAkJCZAkCYsXL67x89angQMHYuDAgbX2eFOnToW/v 3+5t/v7+2Pq1KnVemxJkvDYY49VuN1vv/0GSZJcvq/WrVtXK18TFanOzwEib6cWHYDoeosWLUKrVq1gtVqRkpKCbdu2Yf78+XjzzTfxzTff4KabbnJu+8ADD2D48OFVevyCggLMnTsXAKr0S7g 6z1VXbpTl3LlzePDBB/H9998jPj6+npPV3PWvLTExEWPGjMHjjz+O8ePHO68PDAxEREQEduzYgaZNm4qIStfo3LkzduzygTZt2jivW7duHT744IM6L4Hu9L1JpBQsgOR22rVrh65duzo/Hjt2LJ5++mn07dsXY8aMwenTpxEeHg4AiI6ORnR0dJ3mKSgogK+vb708V2XdKEtcXFyZo6VKcf1rS0hIAAA0btwYPXv2LLV9 WddR/QsMDBT2uXCn700ipeAuYFKExo0bY8GCBcjNzcXHH3/svL6sXT+//vorBg4ciJCQEBgMBjRu3Bhjx45FQUEBEhIS0KBBAwDA3LlznbsTS3aPlTze/v37ceedd8JoNDpHl260m2nlypWIj4+HXq9HXFw c3n33XZfbS3Zvl5SZEmXtNgOA9evXY8iQIQgKCoKvry9at26NefPm3fB1OxwOvP7662jVqhV0Oh3CwsIwefJkXL582WW7gQMHol27dtizZw/69esHX19fxMXF4bXXXoPD4Sjz9V0rJycH0 6ZNQ0hICPz9/TF8+HCcOnWqzG1Pnz6N8ePHIywsDDqdDq1bt8YHH3xQ4XNUVlm7gEvemwMHDmDMmDEIDAxEUFAQJk6ciNTUVJf7V/Y9O3DgAEaOHOl8HZGRkbj11ltLbXc9WZbx+uuvIyYmBnq9Hp0 7d8ZPP/1U5rY5OTmYPn06mjRpAq1Wi6ioKDz11FPIz8+v3ptzA2azGc888ww6duyIoKAgmEwm9OrVCz/88EO59/n444/RokUL6HQ6tGnTBl9//bXL7dd/LU+dOtX5ub52133J98AHH3yA/v 37IywsDH5+fmjfvj1ef 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 sFacCKB4CldwFZl0SnIVIEFkCiCqzYfxk3v/ U7fj3JdV+pmKkgW3QEKsvpn4GFvYFDX4tOQuT2eAwgUTlScs14YcVRbDyRLDoKuRljXproCFSeohxg5YPA6V+Akf8B9EGiExG5JY4AEpVh3ZFE3PzW7yx/VIpBbYDOZhYdgypy9DtgYV/gwnbRSYjcEgsg0TUsNgfmrD6GR5buR1aBVXQcckMmbaDoCFRZ2ReBxSOBTS8Ddh67S3QtFkCiv1zJKsS4j3dg8fYE 0VHIjXEdYIWR7cDWN4HPbwbSz4pOQ+Q2WACJAGz+MwW3vrsVBy9liY5Cbs7ooxcdgarjyj7g4/7AgSWikxC5BRZA8mp2h4w3NpzEfYv3cJcvVYpR4rlzimXJK15TeOXDgJXHcZJ3408y8lq puUV48usD2H42XXQUUhCTLImOQDV1aBmQcgwY9yVgjBGdhkgIjgCSV9p9PgO3vruV5Y+qLJjrAHuGxEPAfwcCZ38VnYRICBZA8iqyLOOjLWcx/pOdSMnleq5UdSYbDxXwGIUZwJKxwNYFopMQ1T vuAiavkV1oxTPLD3FuP6oRo4XHjnkU2QFsegm4sh8Y/RGgCxCdiKhecASQvMLRK9kY+d5Wlj+qMWMR1wH2SCfXAp8MBlL/FJ2EqF6wAJLH+/VkMu76aAcuZRSKjkIegOsAe7C0U8AnQ4BTP4tOQl TnWADJo321+yKm/W8fCq08cJ9qhzE/Q3QEqkuWXOCre4A9n4lOQlSnWADJY/3n5z/x/IojsDtk0VHIQ2h8NPA354iOQXVNtgM//hP4eSYg8+cHeSaeBEIex2Z34LkVR/Ddvsuio5CHMXI dYO+y/V0g+ xIw+mNArROdhqhWcQSQPEp+kQ33fbGX5Y/qhFHjLzoC1bdjK4EvbgcKuOufPAsLIHmMlFwz7v7vDvx+KlV0FPJQRhXXAfZKl3YCnw0FMs6JTlJrBg4ciKeeekp0DBKIBZA8wtnUPIz5cDuOXuHxWVR3jJJGdAQSJf0M8OlNwKXdopO4mDp1KiRJgiRJ0Gg0iIuLw/Tp05Gfn3/D+61YsQIvv/xyrWaRJAmrVq2q1cekusMCSIq370IG7ly4HZczOc0L1S2TzB+ZX q0gvXh38JlNopO4GD58OBITE3Hu3Dm88sor+PDDDzF9+vQyt7Vai1eyMZlMCAhQxqTXFotFdASPxJ9mpGjrjyZh/Ce7kFnA5bmo7gU7HKIjkGi2QuCre4GT60QncdLpdGjYsCEaNWqE8ePHY8K ECc6RuDlz5qBjx474/PPPERcXB51OB1mWXXYBP//88+jZs2epx42Pj8fs2bMBAHv27MHQoUMRGhqKoKAgDBgwAPv373duGxsbCwAYPXo0JElyfgwAa9asQZcuXaDX6xEXF4e5c+fCZrOV+3qmTp 2KO+64A/PmzUNkZCRatGgBADhy5AgGDx4Mg8GAkJAQ/OMf/0BeXp7zfg6HAy+99BKio6Oh0+nQsWNHrF+/3nl7QkICJEnC8uXL0a9fPxgMBnTr1g2nTp3Cnj170LVrV/j7+2P48OFITfX8Q 4lYAEmx/rcjAY8s3YciG38pU/0w2cv /pUVexF4ELJ8EHF0hOkmZDAaDc6QPAM6cOYPly5fj+++/x8GDB0ttP2HCBOzatQtnz551Xnfs2DEcOXIEEyZMAADk5uZiypQp2Lp1K3bu3InmzZtjxIgRyM0tXhlnz549AIBFixYhMTHR+fGGDRswceJEP PHEEzh+/Dg+/vhjLF68GK+++uoNX8OmTZtw4sQJ/PLLL1i7di0KCgowfPhwGI1G7NmzB99++y02btyIxx57zHmfd955BwsWLMCbb76Jw4cPY9iwYbj99ttx+vRpl8eePXs2XnzxRezfvx9qtRr33nsvnn32WbzzzjvYunUrzp49i1mzZlXhHVcmTgNDivTJ7+fw6roTomOQl+E6wOTksAHfPwDYzEDH8aLTOO3evRvLli3DkCFD nNdZLBZ8+eWXaNCgQZn3adeuHeLj47Fs2TLMnDkTALB06VJ069bNOfo2ePBgl/t8/PHHMBqN2LJlC0aOHOL87ODgYDRs2NC53auvvornnnsOU6ZMAQDExcXh5ZdfxrPPPuscXSyLn58fPv30U2i 1WgDAJ598gsLCQvzvf/+Dn58fAOD999/Hbbfdhvnz5yM8PBxvvvkm/vWvf+Gee+4BAMyfPx+bN2/G22+/jQ8++MD52NOnT8ewYcMAAE8++STuvfdebNq0CX369AEA3H///Vi8ePGN3maPwBFAUpzF f5xn+SMhjEU3PrCevIxsB1Y9InzVkLVr18Lf3x96vR69evVC//798d577zlvj4mJKbf8lZgwYQKWLl0KAJBlGV999ZVz9A8AUlJS8NBDD6FFixYICgpCUFAQ8vLycPHixRs+7r59+/DSSy / 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 REqGTO+ 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 M2/HDShsS84l3LRoEL+4wYPKqQnT/ JA+TO2gwrJka03824/HuWpzPcqDTx3lo92EevjvOlYyq5NgKIDdJdAoSRF3xJuSJluy8ALuDB00TlcUkcZfijTy2zozDyXZsu8/Ped2+q3a8s8uC/Q/6QZIqfzzeO8P1mLbGjFYf5EMC0NT kg//rqMGig3+XudGtNRh9zW7e3xJsOJJix/sj9Gj2bh6+GmtAQ38J3T/NR/8YFcL8OLZRKXYLsOdTYPCLopOQACyAXqjIZsfXey6JjkHktowyTygoz+PrCrH6lA2/T/VDdODfRWvrRRtS8mU0fuvvSYbtMvDMz0V4e6cFCU8FlPl4Dfx8sOoeX5htMtILZEQGSHhuYxGaGMsucUU2GY/8aMaSMQacyXDA5gAGxBb/KmsR4oNdl+ 24rSULYKXtXQT0mw5ouCvd27AAeqE1hxKRkc9lrojKY7RzjrTrybKMx38yY+VJG36b4luqoE2K1+CmONdfKcOWFGBSvAb/17HiEVW9WkJUoASrXcb3J6wY17bs+7z8exFuaaZG5wgVDiTaYb tmT4bVXlw6qQoK0oCj3wGdJopOQvWMBdAL/W9HgugIRG7NZOOxZNd7dJ0Zy45Y8cM9vgjQSUjKKz4TN0gnwaCREOLrg5Drzp3R+AAN/SW0DP37OMHJKwsRFSBh3k3FI067LttwJVdGx4YqX MlxYM6WIjhk4Nk+pY/DPJZixzfHbDj4YPGu51ahPvCRJHy234KG/hJOpjnQLbJyJ5/QNfZ/yQLohVgAvcyBi5mc+oWoAkaLueKNvMzCvcWleOAXrmskLxqlx9SOlT/p42K2Az7S36OHZlvx XIDnMh3w10oY0VyNL0cbEKx33Q0vyzL+sdaMt4bp4Kctvs2gkbD4Dj0eXWdGkQ14f4QeUYHc/Vtll3YCaWeA0Gaik1A9kmRZ5oC5F3l+xRF8tfui6BhEbiGg9XNlXv+lzYiOlw7Vcxoig fo+ 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 gs/ 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 dfrikie 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\n",
         "texto/sin formato" : [
          " <Tamaño de figura 800x600 con 1 Eje> "
         ]
        },
        "metadatos" : {},
        "tipo_salida" : " datos_visualización "
       }
      ],
      "fuente" : [
       " habitaciones = df_airbnb['tipo_habitación'].value_counts() \n " ,
       " \n " ,
       " plt.figure(tamaño de figura=(8, 6)) \n " ,
       " plt.pie(habitaciones, etiquetas=habitaciones.index, autopct='%1.1f%%', startangle=90) \n " ,
       " plt.title('Distribución de Tipos de Habitaciones') \n " ,
       " plt.axis('igual') \n " ,
       " \n " ,
       " plt.mostrar() "
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