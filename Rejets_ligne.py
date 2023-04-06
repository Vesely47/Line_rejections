import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_excel('C:\\Users\\Tomáš\\Pandas tutorial\\Rejets_ligne\\Rejets.xlsx')


All = df[['Référence','Semaine','Date','MDE D1','MDE D2','Rejets TU','Rejets_TRQ','Camera_total','Rejets_TPMS']].groupby(['Semaine','Date','Référence']).sum().reset_index()
#All['Date']=All['Date'].dt.strftime("%d-%m-%Y")

def rejets_semaine_total():
    semaine = int(input('Choisir la semaine:'))
    semaine='S'+str(semaine)
    return All[['MDE D1','MDE D2','Rejets TU','Camera_total','Rejets_TRQ','Rejets_TPMS']].loc[All['Semaine']==semaine].sum(axis=1).sum()
def rejets_day():
    day = input("Insert date:")
    den,month,year = day.split('/')
    day=datetime.datetime(int(year),int(month),int(den))
    return All[['MDE D1','MDE D2','Rejets TU','Camera_total','Rejets_TRQ','Rejets_TPMS']].loc[All['Date']==day].sum().sum()
def pareto_semaine():
    semaine = int(input('Choisir la semaine:'))
    semaine='S'+str(semaine)
    Pareto = All[['MDE D1','MDE D2','Rejets TU','Camera_total','Rejets_TRQ','Rejets_TPMS']].loc[All['Semaine']==semaine].sum().reset_index()
    Pareto=Pareto.sort_values(by=0,ascending=False,ignore_index=True)
    Pareto.rename(columns={'index':'Process',0:'N'},inplace=True)
    print(Pareto.loc[0:4,['Process','N']])
    x=Pareto.loc[0:4,'Process']
    y=Pareto.loc[0:4,'N']
    plt.title(f'Pareto semaine {semaine}')
    plt.bar(x,y)
    plt.savefig('graph.png')
    plt.close()
def pareto_semaine_process():
    semaine = int(input('Choisir la semaine:'))
    semaine='S'+str(semaine)
    Pareto = All[['MDE D1','MDE D2','Rejets TU','Camera_total','Rejets_TRQ','Rejets_TPMS']].loc[All['Semaine']==semaine].sum().reset_index()
    Pareto=Pareto.sort_values(by=0,ascending=False,ignore_index=True)
    Pareto.rename(columns={'index':'Process',0:'N'},inplace=True)
    pareto1_name=Pareto.loc[0,'Process']
    pareto1=All[['Référence',pareto1_name]].loc[All['Semaine']==semaine].groupby(['Référence']).sum()
    pareto1=pareto1.sort_values(by=pareto1_name,ascending=False).head(5)
    pareto2_name=Pareto.loc[1,'Process']
    pareto2=All[['Référence',pareto2_name]].loc[All['Semaine']==semaine].groupby(['Référence']).sum()
    pareto2=pareto2.sort_values(by=pareto2_name,ascending=False).head(5)    
    return pareto1,pareto2
    
    
    
    
    
    
    