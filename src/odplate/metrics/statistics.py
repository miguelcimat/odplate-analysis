from __future__ import annotations
import numpy as np
import pandas as pd
from scipy import stats

def anova_un_factor(datos:pd.DataFrame, valor='valor', grupo='grupo'):
    listas=[g[valor].dropna().to_numpy(float) for _,g in datos.groupby(grupo)]
    if len(listas)<2: return {'estadistico':np.nan,'p':np.nan,'nota':'Se requieren al menos dos grupos.'}
    f,p=stats.f_oneway(*listas); return {'estadistico':float(f),'p':float(p)}

def kruskal_wallis(datos:pd.DataFrame, valor='valor', grupo='grupo'):
    listas=[g[valor].dropna().to_numpy(float) for _,g in datos.groupby(grupo)]
    if len(listas)<2: return {'estadistico':np.nan,'p':np.nan}
    h,p=stats.kruskal(*listas); return {'estadistico':float(h),'p':float(p)}

def tukey_hsd(datos:pd.DataFrame, valor='valor', grupo='grupo', alpha=.05):
    try:
        from statsmodels.stats.multicomp import pairwise_tukeyhsd
        r=pairwise_tukeyhsd(datos[valor],datos[grupo],alpha=alpha)
        return pd.DataFrame(r._results_table.data[1:],columns=r._results_table.data[0])
    except ImportError as e: raise ImportError('Instale statsmodels para Tukey HSD.') from e

def dunnett(datos:pd.DataFrame, control, valor='valor', grupo='grupo'):
    if not hasattr(stats,'dunnett'): raise RuntimeError('La versión de SciPy no incluye scipy.stats.dunnett.')
    ctrl=datos.loc[datos[grupo]==control,valor].dropna().to_numpy(float)
    nombres=[]; muestras=[]
    for nombre,g in datos.groupby(grupo):
        if nombre==control: continue
        nombres.append(nombre); muestras.append(g[valor].dropna().to_numpy(float))
    r=stats.dunnett(*muestras,control=ctrl)
    return pd.DataFrame({'grupo':nombres,'estadistico':np.atleast_1d(r.statistic),'p':np.atleast_1d(r.pvalue)})

def modelo_mixto(datos:pd.DataFrame, formula:str, grupo_aleatorio:str):
    try:
        import statsmodels.formula.api as smf
    except ImportError as e:
        raise ImportError('Instale statsmodels para modelos mixtos.') from e
    ajuste=smf.mixedlm(formula,datos,groups=datos[grupo_aleatorio]).fit()
    return ajuste
