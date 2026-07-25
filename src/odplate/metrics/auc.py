from .core import metricas_serie

def auc_serie(*args, **kwargs):
    return metricas_serie(*args, **kwargs)['auc']
__all__=['auc_serie']
