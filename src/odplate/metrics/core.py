from __future__ import annotations
import math
import numpy as np
from scipy import stats
from ..series import extraer_serie


def trapz(y,t): return float(np.trapezoid(np.asarray(y,float),np.asarray(t,float)))

def intervalo_confianza(mean,sem,n,confianza=.95):
    mean=np.asarray(mean,float); sem=np.asarray(sem,float); n=np.asarray(n,float)
    crit=stats.t.ppf((1+confianza)/2,np.maximum(n-1,1))
    return mean-crit*sem, mean+crit*sem

def pendiente_maxima(t,y):
    t=np.asarray(t,float); y=np.asarray(y,float); slopes=np.diff(y)/np.diff(t)
    if not len(slopes): return np.nan,np.nan
    i=int(np.nanargmax(slopes)); return float(slopes[i]),float((t[i]+t[i+1])/2)

def mu_exponencial(t,y,ventana=None,min_puntos=3):
    t=np.asarray(t,float); y=np.asarray(y,float); mask=np.isfinite(y)&(y>0)&np.isfinite(t)
    t=t[mask]; y=y[mask]
    if len(t)<min_puntos: return {'mu':np.nan,'r2':np.nan,'inicio':np.nan,'fin':np.nan}
    ln=np.log(y); mejores=[]
    tamaños=[ventana] if ventana else range(min_puntos,len(t)+1)
    for w in tamaños:
        if w is None or w<min_puntos or w>len(t): continue
        for i in range(len(t)-w+1):
            r=stats.linregress(t[i:i+w],ln[i:i+w])
            if r.slope>0: mejores.append((r.rvalue**2,r.slope,i,w))
    if not mejores: return {'mu':np.nan,'r2':np.nan,'inicio':np.nan,'fin':np.nan}
    r2,mu,i,w=max(mejores,key=lambda x:(x[0],x[1]))
    return {'mu':float(mu),'r2':float(r2),'inicio':float(t[i]),'fin':float(t[i+w-1])}

def metricas_serie(matrices,serie,submatriz,tiempos=None,normalizacion='ninguno',confianza=.95):
    d=extraer_serie(matrices,serie,submatriz,tiempos,normalizacion)
    t,y,std,sem,n=d['tiempo'],d['mean'],d['std'],d['sem'],d['n']
    lo,hi=intervalo_confianza(y,sem,n,confianza)
    vmax,tv=pendiente_maxima(t,y); mu=mu_exponencial(t,y)
    return {'n_tiempos':len(t),'od_inicial':float(y[0]),'od_final':float(y[-1]),'delta_final':float(y[-1]-y[0]),'od_max':float(np.nanmax(y)),'tiempo_od_max':float(t[np.nanargmax(y)]),'od_min':float(np.nanmin(y)),'media_temporal':float(np.nanmean(y)),'std_temporal':float(np.nanstd(y,ddof=1)) if len(y)>1 else 0.0,'auc':trapz(y,t),'vmax_aparente':vmax,'tiempo_vmax':tv,'mu':mu['mu'],'mu_r2':mu['r2'],'fase_exp_inicio':mu['inicio'],'fase_exp_fin':mu['fin'],'tiempo_duplicacion':float(math.log(2)/mu['mu']) if np.isfinite(mu['mu']) and mu['mu']>0 else np.nan,'ci_inferior_final':float(lo[-1]),'ci_superior_final':float(hi[-1])}

def calificacion_inversa(matrices, serie, submatriz, tiempos=None, **kwargs):
    """
    Califica una serie mediante 1 / promedio_t(media_t + desviación_t).

    Una puntuación mayor representa una menor absorbancia corregida, incluso
    después de penalizar la variabilidad entre réplicas. Por ello, al usar este
    criterio normalmente debe indicarse ``mayor_es_mejor=True``.
    """
    d = extraer_serie(matrices, serie, submatriz, tiempos)
    valor = float(np.nanmean(d["mean"] + d["std"]))
    return np.inf if valor == 0 else 1.0 / valor


calificacion_inversa.formula = "1 / promedio_t(media_t + desviación_estándar_t)"

def metricas_frente_control(m_trat,m_control):
    auc_t,auc_c=m_trat['auc'],m_control['auc']; dt=m_trat['delta_final']; dc=m_control['delta_final']
    return {'inhibicion_auc_pct':100*(1-auc_t/auc_c) if auc_c else np.nan,'crecimiento_relativo_pct':100*auc_t/auc_c if auc_c else np.nan,'inhibicion_final_pct':100*(1-dt/dc) if dc else np.nan}
