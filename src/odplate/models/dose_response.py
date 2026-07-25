from __future__ import annotations
import numpy as np
from scipy.optimize import curve_fit


def cuatro_parametros(c, inferior, superior, ic50, pendiente):
    c=np.asarray(c,float)
    return inferior+(superior-inferior)/(1+(c/ic50)**pendiente)


def ajustar_ic(concentraciones, respuestas_pct, p0=None):
    c=np.asarray(concentraciones,float); y=np.asarray(respuestas_pct,float)
    mask=np.isfinite(c)&np.isfinite(y)&(c>0); c,y=c[mask],y[mask]
    if len(c)<4: return {'exito':False,'error':'Se requieren al menos cuatro concentraciones positivas.'}
    if p0 is None: p0=[max(0,float(np.nanmin(y))),min(100,float(np.nanmax(y))),float(np.median(c)),1.0]
    try:
        pars,cov=curve_fit(cuatro_parametros,c,y,p0=p0,bounds=([-np.inf,-np.inf,1e-12,1e-6],[np.inf,np.inf,np.inf,np.inf]),maxfev=50000)
        inferior,superior,ic50,pend=map(float,pars)
        def concentracion_objetivo(inhibicion):
            # La respuesta se interpreta como inhibición porcentual creciente.
            objetivo=float(inhibicion)
            ratio=(superior-inferior)/(objetivo-inferior)-1
            return float(ic50*(ratio**(1/pend))) if ratio>0 else np.nan
        pred=cuatro_parametros(c,*pars); sse=float(np.sum((y-pred)**2)); sst=float(np.sum((y-y.mean())**2))
        return {'exito':True,'inferior':inferior,'superior':superior,'ic50_parametro':ic50,'pendiente':pend,'IC50':concentracion_objetivo(50),'IC90':concentracion_objetivo(90),'r2':1-sse/sst if sst else np.nan,'covarianza':cov.tolist()}
    except Exception as e: return {'exito':False,'error':str(e)}


def mic_aparente(concentraciones, delta_od, umbral=0.05):
    pares=sorted((float(c),float(d)) for c,d in zip(concentraciones,delta_od) if np.isfinite(c) and np.isfinite(d))
    for c,d in pares:
        if d<=umbral: return c
    return np.nan
