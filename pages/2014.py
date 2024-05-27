import streamlit as st
import pandas as pd
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
 
 
st.header('Resultados Globales')

 
col1, col2, col3 = st.columns(3, gap='large')
 
with col1:
    st.info('Cuenta Corriente :bar_chart:')
    st.metric(label='Déficit', value= "US$19.783", delta="5.2% PIB", delta_color= "inverse")
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$19.512", delta="5.2% PIB", delta_color= "inverse")
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$270")
 
# Resultados Globales
 
st.markdown('''- El déficit en cuenta corriente se profundizó para el 2014 al incrementarse en US\$ 7.450 m y
            registró un valor de US\$ 19.783, este déficit se incrementó del 3.2% al 5.2%.
- Por su parte,la cuenta financiera incluyendo variación de reservas internacionales, registró entradas de
            capital por US$ 19.512, superiores a lo observado en 2013. Su equivalencia al PIB pasó de 3.1% a 5.2%.
- La acumulación de reservas internaciones fue de US$4.437.''')
 
# Cuenta Corriente
 
st.header(':blue[Cuenta Corriente]', anchor='cuenta-corriente')
 
st.markdown('''El **déficit de la cuenta corriente** se explica por el **balance deficitario en la renta de factores**
(US\$ 12.783 m) y del **comercio exterior de bienes y servicios** (US \$11.280 m) que fue compensado parcialmente por **ingresos
netos por transferencias corrientes** (US\$4.357 m)
''')
 
st.info('''La **profundización del déficit** en 2014 se originó por el **balance negativo obtenido en la cuenta de bienes** que
           contrasta con el superávit obtenido en 2013. Este comportamiento se dio **por una fuerte caída del precio del
            petróleo** para el cuarto trimestre que afectó de manera significativa el resultado de la balanza comercial
           y por ende el balance corriente.''',icon="🚨")
 
 
st.sidebar.markdown('[Cuenta Corriente](#cuenta-corriente)')
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[1:14,]
df = df.drop(['Cuenta corriente'], axis=1).loc[1:14,]
 
df_melted= pd.melt(df, id_vars=['Año'], var_name='Grupo', value_name='Valor')
df_melted['Año']=df_melted['Año'].astype('str')
cc['Año']=cc['Año'].astype('str')
 
# Crear la gráfica de barras
plt.figure(figsize=(10, 6))
sns.barplot(x='Año', y='Valor',hue='Grupo', data=df_melted, dodge=True, palette='rocket')
sns.lineplot(x='Año', y='Cuenta corriente', data=cc, marker='o', color='black', label='Cuenta corriente')
 
# Personalizar la gráfica
plt.title('Componentes de la cuenta corriente de la balanza de pagos de Colombia',weight='bold')
plt.xlabel('Fecha')
plt.ylabel('Millones de USD')
plt.xticks(rotation =45)
plt.axhline(0, color='black',linewidth=0.5)
plt.legend(loc='lower left')
 
 
# Mostrar la gráfica en Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
 
st.caption('Fuente: Banco de la República, elaboración propia')
# Balanza Comercial: Bienes
 
st.subheader('Balanza Comercial de Bienes'+ ':shopping_trolley:',anchor='balanza-bienes')
 
st.markdown('''La balanza comercial de bienes registró un déficit de US$ 4.694, este resultado se
             explica por las tasas negativas de crecimiento de las exportaciones y una mayor actitud
             importadora por parte del país que se observa desde el segundo trimestre de 2013.''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
 
# Gráfica Balanza Comercial Bienes
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[1:14,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[1:14,]
 
bcs_melted = pd.melt(bcs, id_vars=['Año'],var_name='Grupo', value_name='Valor')
 
col1,col2 =st.columns(2,gap='large')
 
with col1:
    sns.barplot(x='Año',y='Valor',hue='Grupo',data=bcs_melted, dodge= True, palette='mako')
    plt.title('Exportaciones e Importaciones de Bienes',weight='bold',fontsize=16)
    plt.xlabel('Fecha')
    plt.ylabel('Millones de USD')
    plt.xticks(rotation=45)
    st.pyplot()
 
with col2:
    sns.barplot(x='Año',y='Balanza',data=balance_bienes, color='skyblue')
    plt.title('Balanza Comercial de Bienes',weight='bold',fontsize=16)
    plt.xlabel('Fecha')
    plt.ylabel('Millones de USD')
    plt.xticks(rotation=45)
    plt.axhline(0,color='black',linewidth=0.5)
    st.pyplot()
 
st.caption('Fuente: Banco de la República, elaboración propia')
 
st.markdown('''**El grupo de los principales commodities exportados registró una disminución anual del 5.5%.**
            Como ya se mencionó este resultado se explica por una caída en los precios de exportación de
            petróleo crudo, que se sumó a la ya observada caída del carbón, oro y ferroníquel. Es importante
            resaltar que **este descenso fue compensado ligeramente por el incremento en el volumen exportado de
            bienes como el carbón, petróleo, café, flores y bananos**.
''')
 
st.markdown('''Las compras de bienes externos se ubicaron en US$ 61.676m y tuvieron un crecimiento anual del 8.0%.''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios'+ ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''Al igual que **la balanza de bienes**, el comercio exterior de servicios **registró un balance deficitario de
            US$ 6.586 m** y fue superior al registrado en 2013. En este rubro se destacó la participación del transporte
             y los viajes que representaron el 66% de del comercio global.
            ''')
 
st.sidebar.markdown('- [Balanza comercial Servicios](#balanza-servicios)')
 
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[1:14,]
serv['Año'] = serv['Año'].astype('str')
balance_servicios = serv[['Año','Balance']]
serv = serv.drop('Balance',axis=1)
serv_melted = pd.melt(serv, id_vars='Año',var_name='Grupo',value_name='Valor')
 
 
col1,col2 =st.columns(2,gap='large')
 
with col1:
    sns.barplot(x='Año',y='Valor', hue='Grupo',data=serv_melted, dodge=True, palette='mako')
    plt.title('Exportaciones e importaciones de Servicios',weight='bold',fontsize=16)
    plt.xlabel('Fecha')
    plt.ylabel('Millones de USD')
    plt.xticks(rotation=45)
    st.pyplot()
 
with col2:
    sns.barplot(x='Año',y='Balance',data=balance_servicios,label='Balance servicios',color='midnightblue')
    plt.title('Balanza comercial de Servicios',weight='bold',fontsize=16)
    plt.xlabel('Fecha')
    plt.ylabel('Millones de USD')
    plt.xticks(rotation=45)
    st.pyplot()
 
st.caption('Fuente: Banco de la República, elaboración propia')
 
st.markdown('''Las **exportaciones de servicios ascendieron a US$ 6.937 m con un crecimiento de 1.1%**, esta
             cifra estuvo impulsada mayoritariamente por mayores ingresos por concepto de **viajes** y también
             por aumentos menores en el **rubro** de transporte.
''')
 
st.markdown('''Las **importaciones de servicios registraron un crecimiento anual de 5.7%** impulsado principalmente
            por incrementos en los egresos por viajes.
''')
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''**En el año 2014 la renta de factores obtuvo un balance deficitario (US\$12.859 m)**, pero inferior en
            US\$ 1.319 m (9.3%) a lo registrado en 2013. Este menor balance deficitario se explica por la caída en
            los egresos por renta factorial, así como por el crecimiento de los ingresos.''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[1:14,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[1:14,]
 
ingresos_netos = ingresos[['Año','Ingresos']]
ingresos_netos['Año'] = ingresos_netos['Año'].astype('str')
 
egresos_netos = egresos[['Año','Egresos']]
egresos_netos['Año'] = egresos_netos['Año'].astype('str')
 
ingresos = ingresos.drop('Ingresos',axis=1)
egresos = egresos.drop('Egresos',axis=1)
 
 
col1, col2 = st.columns(2,gap='large')
 
with col1:
    ingresos_melted=pd.melt(ingresos, id_vars='Año',var_name='Grupo',value_name='Valor')
    ingresos_melted['Año'] = ingresos_melted['Año'].astype('str')
    sns.barplot(x='Año',y='Valor',hue='Grupo',data=ingresos_melted, palette='crest',dodge=False)
    sns.lineplot(x='Año',y='Ingresos',data=ingresos_netos,color='black',marker='o',label='Ingresos netos')
    plt.ylabel('Millones de USD')
    plt.xlabel('Fecha')
    plt.xticks(rotation=45)
    plt.legend(loc='upper center',bbox_to_anchor=(0.5,-0.15),ncol=3)
    st.pyplot()
 
with col2:
    egresos_melted=pd.melt(egresos, id_vars='Año',var_name='Grupo',value_name='Valor')
    egresos_melted['Año'] = egresos_melted['Año'].astype('str')
    sns.barplot(x='Año',y='Valor',hue='Grupo',data=egresos_melted, palette='crest',dodge=False)
    sns.lineplot(x='Año',y='Egresos',data=egresos_netos,color='black',marker='o',label='Egresos')
    plt.ylabel('Millones de USD')
    plt.xlabel('Fecha')
    plt.xticks(rotation=45)
    plt.legend(loc='upper center',bbox_to_anchor=(0.5,-0.15),ncol=3)
    st.pyplot()
st.caption('Fuente: Banco de la República, elaboración propia.')
 
st.markdown('''El 73% de los egresos se originó en las utilidades de las empresas con IED y en menor cuantía
            en los pagos de intereses asociados a títulos de deuda y préstamos y otros créditos externos.''')
 
st.info('''Los **egresos por utilidades disminuyeron anualmente 10.1%**. Esto se dio por **menores ganancias** de las
        firmas con capital extranjero que operan **en el sector minero-energético** y en menor proporción por los
        **establecimientos financieros, transporte y comunicaciones**. Estas caídas fueron contrarrestadas por el
        incremento de las utilidades de las empresas comerciales y manufactureras.''',icon='🔎')
 
st.markdown('''Los ingresos por renta de los factores aumentaron 12.0%. Estos resultados se originaron mayoritariamente
            en las utilidades de la IEDC. ''')
 
 
# Transferencias corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias-corrientes')
 
st.markdown('''**Se registraron ingresos netos de US\$4.357 m, con un nivel 5.2% menor al de 2013. Las remesas de los
            trabajadores totalizaron US\$ 4.093 m (1.1% del PIB) representado una caída anual del 7.0%.** Los ingresos
             por otras transferencias registraron un aumento del 13.2% en comparación con el año anterior. Se
            registraron egresos por transferencias al exterior por US\$ 950 m, con un crecimiento del 8.0%''')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias-corrientes)')
 
st.info('''Las remesas de los trabajadores cayeron por un menor número de transferencias provenientes de Venezuela,
        que fueron compensadas por envíos mayores de Costa Rica, Chile y Brasil.''', icon='🔎')
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[1:14,]
transferencias['Año'] = transferencias['Año'].astype('str')
totales = transferencias[['Año','Transferencias corrientes']]
 
transferencias = transferencias.drop('Transferencias corrientes',axis=1)
 
transferencias_melted = pd.melt(transferencias,id_vars='Año',var_name='Grupo',value_name='Valor')
 
sns.barplot(x='Año',y='Valor',hue='Grupo',data=transferencias_melted, dodge=True,palette='viridis')
sns.lineplot(x='Año',y='Transferencias corrientes', data=totales, color='black',marker='o',label='Transferencias netas')
 
plt.title('Transferencias Corrientes Netas',weight='bold')
plt.ylabel('Millones USD')
plt.xlabel('Año')
plt.xticks(rotation=45)
st.pyplot()
 
st.caption('Fuente: Banco de la República, elaboración propia.')
 
#Cuenta Financiera
 
st.header(':blue[Cuenta Financiera]',anchor='cuenta-financiera')
 
st.markdown('''**La cuenta financiera (incluyendo activos de reserva) en 2014 registró entradas netas de capital
            por US\$ 19.512m (5.2% del PIB)**. Cifra superior en US\$7.677m a lo observado en 2013. Estas entradas de
            explican por ingresos de capital extranjero (US\$36.992m), salidas de capital colombiano (US\$12.716m), pagos por conceptos de derivados
            financieros (US\$327m) y aumento de reservas internacionales por transacciones de la balanza de pagos
            (US\$4.437m)''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[12:13,]
total = financiera[['Año','Cuenta financiera']]
financiera = financiera.drop('Cuenta financiera',axis=1)
 
financiera_melted=pd.melt(financiera,id_vars='Año',var_name='Grupo',value_name='Valor')
financiera_melted['Año'] = financiera_melted['Año'].astype('str')
total['Año'] = total['Año'].astype('str')
 
paleta= sns.color_palette(['#6A8CAF','#7A4F6D','#C5C6C7','#E8D2A6','#96C5F7'])
 
plt.figure(figsize=(10, 6))
sns.barplot(x='Año',y='Valor',hue='Grupo',data=financiera_melted,dodge=True, palette= paleta)
sns.lineplot(x='Año',y='Cuenta financiera',data=total,color='black',marker='o',label='Cuenta financiera')
 
#Personalización
plt.title('Cuenta Financiera',weight ='bold')
plt.axhline(0,linewidth=0.5,color='black')
plt.xlabel('Año')
plt.ylabel('Millones USD')
plt.xticks(rotation=45)
plt.legend(loc='lower center',bbox_to_anchor=(0.5,-0.30),ncol=3)
 
 
st.pyplot()
st.caption('Fuente: Banco de la República, elaboración propia.')