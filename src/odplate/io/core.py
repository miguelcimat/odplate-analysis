from __future__ import annotations
from pathlib import Path
from typing import Callable, Optional, Pattern, Dict, Any
import re
import numpy as np
import pandas as pd


def nombre_fila(i:int)->str:
    s=''; n=i+1
    while n:
        n,r=divmod(n-1,26); s=chr(65+r)+s
    return s


def leer_matriz_absorbancia(ruta_excel:str|Path, filas:int=8, columnas:int=12, hoja:Optional[str]=None, marcador:str='Abs')->np.ndarray:
    ruta=Path(ruta_excel)
    if not ruta.exists(): raise FileNotFoundError(ruta)
    contenido=pd.read_excel(ruta, sheet_name=hoja if hoja is not None else 0, header=None)
    posiciones=[]
    for f in range(contenido.shape[0]):
        for c in range(contenido.shape[1]):
            v=contenido.iat[f,c]
            if isinstance(v,str) and v.strip().lower()==marcador.lower(): posiciones.append((f,c))
    for fi,ci in posiciones:
        enc=pd.to_numeric(contenido.iloc[fi,ci+1:ci+columnas+1],errors='coerce')
        if len(enc)!=columnas or enc.isna().any() or not np.array_equal(enc.to_numpy(int),np.arange(1,columnas+1)): continue
        etiquetas=contenido.iloc[fi+1:fi+filas+1,ci].astype(str).str.strip().str.upper().tolist()
        if etiquetas!=[nombre_fila(i) for i in range(filas)]: continue
        datos=contenido.iloc[fi+1:fi+filas+1,ci+1:ci+columnas+1].apply(pd.to_numeric,errors='coerce')
        if datos.shape==(filas,columnas) and not datos.isna().any().any(): return datos.to_numpy(float)
    raise ValueError(f'No se encontró una matriz válida {filas}x{columnas} encabezada por {marcador!r}.')


def extractor_tiempo_por_defecto(nombre:str):
    partes=Path(nombre).stem.split('_')
    for p in partes[1:]:
        try: return float(p) if '.' in p else int(p)
        except ValueError: pass
    m=re.search(r'(?<!\d)(\d+(?:\.\d+)?)(?!\d)',Path(nombre).stem)
    if not m: return None
    x=float(m.group(1)); return int(x) if x.is_integer() else x


def leer_carpeta_cruda(ruta_carpeta:str|Path, nombre_blanco:str, filas:int=8, columnas:int=12, hoja:Optional[str]=None, extractor_tiempo:Callable[[str],Any]=extractor_tiempo_por_defecto, coincidencia_blanco:str='igual')->Dict[Any,np.ndarray]:
    carpeta=Path(ruta_carpeta)
    if not carpeta.is_dir(): raise NotADirectoryError(carpeta)
    archivos=sorted(p for p in carpeta.iterdir() if p.suffix.lower() in {'.xlsx','.xls','.xlsm'} and not p.name.startswith('~$'))
    if not archivos: raise ValueError('No se encontraron archivos Excel.')
    objetivo=nombre_blanco.lower().strip()
    salida={}; blanco=None
    for p in archivos:
        stem=p.stem.lower().strip()
        es=(stem==objetivo) if coincidencia_blanco=='igual' else (objetivo in stem)
        if es:
            if blanco is not None: raise ValueError('Se encontró más de un archivo blanco; use un nombre más específico.')
            blanco=leer_matriz_absorbancia(p,filas,columnas,hoja)
            salida['blanco']=blanco
    if blanco is None: raise ValueError(f'No se encontró el blanco {nombre_blanco!r}.')
    for p in archivos:
        stem=p.stem.lower().strip()
        es=(stem==objetivo) if coincidencia_blanco=='igual' else (objetivo in stem)
        if es: continue
        t=extractor_tiempo(p.name)
        if t is None: continue
        if t in salida: raise ValueError(f'Tiempo repetido {t}: {p.name}')
        salida[t]=leer_matriz_absorbancia(p,filas,columnas,hoja)
    tiempos=sorted(k for k in salida if isinstance(k,(int,float)))
    if not tiempos: raise ValueError('No se extrajeron tiempos de los nombres de archivo.')
    return {'blanco':salida['blanco'], **{t:salida[t] for t in tiempos}}
