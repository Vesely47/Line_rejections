import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:\\Users\\Tomáš\\Pandas tutorial\\Rejets_ligne\\Rejets.xlsx')


All = df[['Référence','Semaine','Date','MDE D1','MDE D2','Rejets TU','Rejets_TRQ','Camera_total','Rejets_TPMS']].groupby(['Semaine','Date','Référence']).sum().reset_index()


def pareto_semaine():
    semaine = int(input('Choisir la semaine:'))
    semaine='S'+str(semaine)
    Pareto = All[['MDE D1','MDE D2','Rejets TU','Camera_total','Rejets_TRQ','Rejets_TPMS']].loc[All['Semaine']==semaine].sum().reset_index()
    Pareto=Pareto.sort_values(by=0,ascending=False,ignore_index=True)
    Pareto.rename(columns={'index':'Process',0:'N'},inplace=True)
    print(Pareto.loc[0:4,['Process','N']])
    x=Pareto.loc[0:4,'Process']
    y=Pareto.loc[0:4,'N']
    plt.title(f'Pareto rejets ligne semaine {semaine}')
    plt.bar(x,y)
    plt.savefig('graph'+str(semaine))
    plt.close()
    return semaine
def pareto_semaine_process():
    semaine = int(input('Choisir la semaine:'))
    semaine='S'+str(semaine)
    Pareto = All[['MDE D1','MDE D2','Rejets TU','Camera_total','Rejets_TRQ','Rejets_TPMS']].loc[All['Semaine']==semaine].sum().reset_index()
    Pareto=Pareto.sort_values(by=0,ascending=False,ignore_index=True)
    Pareto.rename(columns={'index':'Process',0:'N'},inplace=True)
    for x1 in range(5):
        paretox_name=Pareto.loc[x1,'Process']
        paretox=All[['Référence',paretox_name]].loc[All['Semaine']==semaine].groupby(['Référence']).sum()
        paretox=paretox.sort_values(by=paretox_name,ascending=False).head(5).reset_index()
        x=paretox.loc[0:4,'Référence']
        y=paretox.loc[0:4,paretox_name]
        plt.title(f'Semaine {semaine} '+str(paretox_name))
        plt.bar(x,y)
        plt.savefig('graph'+str(x1))
        plt.close()
        return semaine
        print(paretox.columns)
    