from __future__ import annotations
from typing import Any, Dict
import numpy as np


def promediar_submatrices(matriz, submatriz:int, ddof:int=1, permitir_incompleta:bool=False):
    a=np.asarray(matriz,float)
    if a.ndim!=2: raise ValueError('La matriz debe ser bidimensional.')
    if submatriz<1: raise ValueError('submatriz debe ser positiva.')
    if a.shape[1]%submatriz and not permitir_incompleta: raise ValueError('Columnas no divisibles entre submatriz.')
    medias=[]; desv=[]; sem=[]; n=[]
    for inicio in range(0,a.shape[1],submatriz):
        bloque=a[:,inicio:inicio+submatriz]
        if bloque.shape[1]<submatriz and not permitir_incompleta: break
        medias.append(np.nanmean(bloque,axis=1)); n.append(np.sum(np.isfinite(bloque),axis=1))
        desv.append(np.nanstd(bloque,axis=1,ddof=ddof))
        sem.append(desv[-1]/np.sqrt(np.maximum(n[-1],1)))
    return {'mean':np.column_stack(medias),'std':np.column_stack(desv),'sem':np.column_stack(sem),'n':np.column_stack(n)}


def procesar_matrices(crudas:Dict[Any,np.ndarray], submatriz:int, restar_blanco:bool=True, modo_blanco:str='constante', ddof:int=1):
    if 'blanco' not in crudas: raise KeyError("Falta la matriz 'blanco'.")
    blanco=np.asarray(crudas['blanco'],float)
    salida={'blanco':blanco, 'blanco_promedio':promediar_submatrices(blanco,submatriz,ddof)}
    for t,m in crudas.items():
        if t=='blanco': continue
        a=np.asarray(m,float)
        if a.shape!=blanco.shape: raise ValueError(f'Tiempo {t}: forma {a.shape} diferente al blanco {blanco.shape}.')
        corregida=a-blanco if restar_blanco else a.copy()
        salida[t]={'raw':a,'corrected':corregida,**promediar_submatrices(corregida,submatriz,ddof)}
    return salida


def normalizar_vector(y, modo:str='ninguno', epsilon:float=1e-12):
    y=np.asarray(y,float)
    if modo in {None,'ninguno','raw','corregida'}: return y.copy()
    if modo in {'delta','dOD'}: return y-y[0]
    if modo in {'relativa','rel'}:
        if abs(y[0])<=epsilon: return np.full_like(y,np.nan)
        return y/y[0]
    if modo=='ln': return np.where(y>0,np.log(y),np.nan)
    if modo=='log10': return np.where(y>0,np.log10(y),np.nan)
    raise ValueError(f'Modo de normalización desconocido: {modo}')
