{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "g = 9.80665 # Aceleracion gravitacional de la tierra"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [],
   "source": [
    "#====Funciones============\n",
    "def sacar_k(m, delta_x):   #función para sacar el valor de la elasticidad\n",
    "    r = (m*g)/delta_x\n",
    "    print(str(r) + \" N/m²\", \"\\n\", \"=\"*50, \"\\n\")\n",
    "    \n",
    "def sacar_m(k, delta_x):   #función para sacar el valor de la masa\n",
    "    r = (k*delta_x)/g\n",
    "    print(str(r) + \" Kg\", \"\\n O tambien: \\n\", str(r*1000) + \" g\", \"\\n\",\"=\"*50, \"\\n\")\n",
    "    \n",
    "def sacar_delta_x(m, k):   #funcion para sacar el valor de ∆x\n",
    "    r = (m*g)/k\n",
    "    print(str(r) + \" m\", \"\\n O tambien: \\n\", str(r*100) + \" cm\", \"\\n\",\"=\"*50, \"\\n\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Masa (Kg)</th>\n",
       "      <th>∆x (m)</th>\n",
       "      <th>Elasticidad (N/m²)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.266</td>\n",
       "      <td>0.034</td>\n",
       "      <td>76.722615</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.160</td>\n",
       "      <td>0.020</td>\n",
       "      <td>78.453200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.610</td>\n",
       "      <td>0.077</td>\n",
       "      <td>77.689045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.300</td>\n",
       "      <td>0.038</td>\n",
       "      <td>77.420921</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.477</td>\n",
       "      <td>0.060</td>\n",
       "      <td>77.962868</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Masa (Kg)  ∆x (m)  Elasticidad (N/m²)\n",
       "0      0.266   0.034           76.722615\n",
       "1      0.160   0.020           78.453200\n",
       "2      0.610   0.077           77.689045\n",
       "3      0.300   0.038           77.420921\n",
       "4      0.477   0.060           77.962868"
      ]
     },
     "execution_count": 171,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#================== Deduciendo la elasticidad del resorte ==============================\n",
    "\n",
    "lista_m = [0.266, 0.160, 0.610,  0.300, 0.477] #En kilogramos\n",
    "lista_delta_x = [0.034, 0.02,  0.077, 0.038, 0.06] #En metros\n",
    "df = pd.DataFrame({\"Masa (Kg)\":lista_m, \"∆x (m)\":lista_delta_x}) #Tabla que agrupa los datos\n",
    "df['Elasticidad (N/m²)'] = (df[\"Masa (Kg)\"].values*g)/df[\"∆x (m)\"].values #aplica la funcion \"sacar_k\" a las filas y agrega una columna a la tabla con los resultados\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'77.64972974261187 N/m²'"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#============== Promediando los resultados de la Elasticidad =====================\n",
    "k = str(np.sum(df['Elasticidad (N/m²)'].values)/len(df['Elasticidad (N/m²)'].values)) + \" N/m²\"\n",
    "k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.4078864851911713 Kg \n",
      " O tambien: \n",
      " 407.88648519117135 g\n"
     ]
    }
   ],
   "source": [
    "#===============Calculando el valor de la masa (ejemplo) =============\n",
    "sacar_m(50, 0.08)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.6628155384356534 Kg \n",
      " O tambien: \n",
      " 662.8155384356535 g \n",
      " ================================================== \n",
      "\n",
      "0.030645781249999997 m \n",
      " O tambien: \n",
      " 3.0645781249999997 cm \n",
      " ================================================== \n",
      "\n",
      "91.06174999999999 N/m² \n",
      " ================================================== \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#=============== Problemas Resueltos ===================\n",
    "sacar_m(65, 0.1) #Problema 1\n",
    "sacar_delta_x(0.125, 40) #Problema 2\n",
    "sacar_k(0.65, 0.07) #Problema 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.6566972411577858 Kg \n",
      " O tambien: \n",
      " 656.6972411577858 g \n",
      " ================================================== \n",
      "\n",
      "1620.2291304347825 m \n",
      " O tambien: \n",
      " 162022.91304347824 cm \n",
      " ================================================== \n",
      "\n",
      "60.348615384615385 N/m² \n",
      " ================================================== \n",
      "\n",
      "0.4486751337102885 Kg \n",
      " O tambien: \n",
      " 448.6751337102885 g \n",
      " ================================================== \n",
      "\n",
      "97.28980307214074 m \n",
      " O tambien: \n",
      " 9728.980307214075 cm \n",
      " ================================================== \n",
      "\n",
      "102.45753731343281 N/m² \n",
      " ================================================== \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#================ Actividades                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ==============================\n",
    "sacar_m(92, 0.07) #Actividad 1\n",
    "sacar_delta_x(38, 0.23) #Actividad 2\n",
    "sacar_k(0.8, 0.13) #Actividad 3\n",
    "sacar_m(110, 0.04) #Actividad 4\n",
    "sacar_delta_x(18, 1.81437) #Actividad 5\n",
    "sacar_k(0.7, 0.067) #Actividad 6"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
