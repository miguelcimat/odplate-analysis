from __future__ import annotations
import numpy as np
from scipy.optimize import curve_fit

def exponencial(t,od0,mu): return od0*np.exp(mu*np.asarray(t))
def logistico_t0(t,K,r,t0): return K/(1+np.exp(-r*(np.asarray(t)-t0)))
def gompertz_modificado(t,A,mu,lam): return A*np.exp(-np.exp((mu*np.e/A)*(lam-np.asarray(t))+1))
MODELOS={'exponencial':(exponencial,2),'logistico':(logistico_t0,3),'gompertz':(gompertz_modificado,3)}

def calidad_ajuste(y,pred,p):
    y=np.asarray(y,float); pred=np.asarray(pred,float); n=len(y); res=y-pred; sse=float(np.sum(res**2)); mse=sse/n; rmse=float(np.sqrt(mse)); sst=float(np.sum((y-y.mean())**2)); r2=1-sse/sst if sst else np.nan; r2a=1-(1-r2)*(n-1)/(n-p-1) if n>p+1 and np.isfinite(r2) else np.nan; aic=n*np.log(max(sse/n,1e-300))+2*p
    return {'sse':sse,'mse':mse,'rmse':rmse,'r2':r2,'r2_ajustado':r2a,'aic':float(aic)}

def ajustar_modelo(t,y,modelo='logistico',p0=None,bounds=(-np.inf,np.inf),maxfev=50000):
    f,p=MODELOS[modelo]; t=np.asarray(t,float); y=np.asarray(y,float); mask=np.isfinite(t)&np.isfinite(y); t=t[mask]; y=y[mask]
    if len(y)<=p: return {'modelo':modelo,'exito':False,'error':'Puntos insuficientes'}
    if p0 is None:
        if modelo=='exponencial': p0=[max(y[0],1e-6),0.1]
        elif modelo=='logistico': p0=[max(y),0.5,float(np.median(t))]
        else: p0=[max(y),max(np.ptp(y)/max(np.ptp(t),1e-9),1e-6),float(t[0])]
    try:
        pars,cov=curve_fit(f,t,y,p0=p0,bounds=bounds,maxfev=maxfev); pred=f(t,*pars)
        return {'modelo':modelo,'exito':True,'parametros':list(map(float,pars)),'covarianza':cov.tolist(),'prediccion':pred.tolist(),**calidad_ajuste(y,pred,p)}
    except Exception as e: return {'modelo':modelo,'exito':False,'error':str(e)}

def seleccionar_mejor_modelo(t,y,modelos=('exponencial','logistico','gompertz')):
    ajustes=[ajustar_modelo(t,y,m) for m in modelos]; validos=[a for a in ajustes if a.get('exito')]
    return {'mejor':min(validos,key=lambda a:a['aic']) if validos else None,'ajustes':ajustes}
