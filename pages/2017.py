import streamlit as st
import pandas as pd
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
 
# st.set_page_config(page_title='2017',page_icon=':calendar')
st.header('Resultados Globales')

 
col1, col2, col3 = st.columns(3, gap='large')
 
with col1:
    st.info('Cuenta Corriente :bar_chart:')
    st.metric(label='Déficit', value= "US$10.359", delta="-3.2% PIB", delta_color='inverse')
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$9.694", delta="-3.1% PIB",delta_color='inverse')
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$665")
 
# Resultados Globales
 
st.markdown('''- En 2017, la cuenta corriente del país registró un déficit de US\$10.359 m, cifra que estuvo US\$1.770 m por debajo del registro de 2016.
            Como proporción del PIB de 2017, el déficit fue de 3.3, menor en 1 p.p. en comparación con  el observado en 2016. ''')
 
st.error('''**Importante:** La disminución de un punto porcentual se originó gracias a la reducción en dólares del déficit de la cuenta corriente (0.6pp),
         el crecimiento del PIB nominal en pesos (0.3pp) y el efecto de la apreciación del peso frente al dólar en la medición del PIB nominal
        en dólares (0.1 p. p)''',icon="🚨")
 
st.markdown('''- La cuenta financiera (incluyendo las reservas internacionales) contabilizó entradas de capital por US\$ 9.694 m. En términos
            del PIB las entradas de capital representaron 3.1%, menor al 4.5% del año anterior
- Los errores y omisiones en 2015 se estimaron en US$665 m.
''')
 
# Cuenta Corriente
 
st.header(':blue[Cuenta Corriente]', anchor='cuenta-corriente')
 
st.markdown('''El **déficit en la cuenta corriente** del país para 2017 (US\$10.359 m) **está explicado** principalmente **por el resultado deficitario la renta de
            los factores** (US\$8.167 m), a su vez también contribuyeron los **balances deficitarios la balanza de bienes y servicio**s con de US\$ 4.766m y
            US\$ 4.111 m, respectivamente. Estos balances deficitarios fueron **compensados parcialmente por** ingresos netos de US\$ 6.685 m por concepto
            de **transferencias corrientes.**''')
 
st.warning('''La reducción del déficit corriente en 2017 fue el resultado de un menor déficit de la balanza comercial de bienes y el incremento de
           ingresos por transferencias corrientes. Estos resultados estuvieron compensados parcialmente por los mayores egresos de la renta factorial
            y del comercio exterior de servicios.''', icon='⚠️')
 
# Gráfica Cuenta Corriente
 
st.sidebar.markdown('[Cuenta Corriente](#cuenta-corriente)')
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[4:17,]
df = df.drop(['Cuenta corriente'], axis=1).loc[4:17,]
 
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
plt.show()
 
# Mostrar la gráfica en Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
 
st.caption('Fuente: Banco de la República, elaboración propia')
 
# Balanza Comercial: Bienes
 
st.subheader('Balanza Comercial de Bienes'+ ':shopping_trolley:',anchor='balanza-bienes')
 
st.markdown('''En 2017 **la balanza comercial obtuvo un balance deficitario de US$4.766 m**, cifra muy inferior al balance negativo en 2016.''')
 
st.markdown('''Las **exportaciones totales de bienes** del país **registraron** US\$39.474 m con **una variación anual de 15.8%**. El aumento en el valor
            total exportado se originó principalmente **por mayores ventas de carbón** (US\$2.751 m), de **petróleo y sus derivados** (US\$ 2.263m) y
            en menor medida, por el incremento en los **despachos de productos industriales** (US\$643 m), de **café** (US\$ 322 m) y **bananos y flores**
            (US\$ 90 m). A su vez se registraron reducciones en la exportaciones de oro no monetario (US\$781m).
''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
 
# Gráfica Balanza Comercial Bienes
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[4:17,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[4:17,]
 
bcs_melted = pd.melt(bcs, id_vars=['Año'],var_name='Grupo', value_name='Valor')
 
col1,col2 =st.columns(2,gap='large')
 
with col1:
    sns.barplot(x='Año',y='Valor',hue='Grupo',data=bcs_melted, dodge= True, palette='mako')
    plt.title('Exportaciones e Importaciones de Bienes',weight='bold',fontsize=16)
    plt.legend(loc='upper left')
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
 
st.info('''El mayor valor exportado de petróleo crudo y carbón se explica por el alza en sus precios de exportación (30.6% y 26.9% respectivamente).
        Mientras que las cantidades exportadas de carbón aumentaron un 26.1%, las de petróleo disminuyeron 6.6%.''',icon="🔎")
 
st.markdown('''Por parte, las compras externas bienes se ubicaron en US$44.421 m, representado un aumento anual de 2.3%.''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios'+ ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''Al igual que la balanza comercial de bienes, el comercio exterior de servicios registró en 2017 un déficit de US\$ 4.111 m, cifra
            que estuvo US\$ 503 m por encima del déficit de 2016. ''')
 
st.sidebar.markdown('- [Balanza comercial Servicios](#balanza-servicios)')
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[4:17,]
serv['Año'] = serv['Año'].astype('str')
balance_servicios = serv[['Año','Balance']]
serv = serv.drop('Balance',axis=1)
serv_melted = pd.melt(serv, id_vars='Año',var_name='Grupo',value_name='Valor')
 
 
col1,col2 =st.columns(2,gap='large')
 
with col1:
    sns.barplot(x='Año',y='Valor', hue='Grupo',data=serv_melted, dodge=True, palette='mako')
    plt.title('Exportaciones e importaciones de Servicios',weight='bold',fontsize=16)
    plt.legend(loc='upper left')
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
 
st.markdown('''Las **exportaciones de servicios reportaron un crecimiento anual de 8.5%**. Este resultado estuvo impulsado
            por mayores ingresos por concepto de viajes que estuvieron parcialmente compensados por la reducción de los
            ingresos por servicios de transporte y otros empresariales.
''')
 
st.markdown('''Las **importaciones de servicios registraron una caída anual de 9.4%**, en razón a una reducción de las importaciones
             de servicios empresariales y de construcción especialmente vinculados a la actividad petrolera.''')
 
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''Se estima que el **balance deficitario del la renta de los factores** fue de US\$ 8.167 m. En comparación con el valor registrado un año atrás,
            el déficit de este rubro **fue superior en US\$ 2.918 m**. El mayor balance deficitario se produjo principalmente por mayores egresos por la renta
            vinculada a la inversión extranjera directa.
''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[4:17,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[4:17,]
 
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
    plt.title('Ingresos por renta factorial',weight='bold',fontsize=16)
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
    plt.title('Egresos por renta factorial',weight='bold',fontsize=16)
    plt.ylabel('Millones de USD')
    plt.xlabel('Fecha')
    plt.xticks(rotation=45)
    plt.legend(loc='upper center',bbox_to_anchor=(0.5,-0.15),ncol=3)
    st.pyplot()
st.caption('Fuente: Banco de la República, elaboración propia.')
 
st.markdown('''Del total de egresos (US\$ 13.641 m), el 54% correspondió a la renta obtenida por las empresas con IED (US\$ 7.630 m)
            el 34.5% a los pagos de dividendos y de intereses por inversiones extranjeras de portafolio (US\$ 4.700m) y en menor cuantía
            a los pagos de intereses de créditos externos (11.4%, US$\2.646m)''')
 
st.info(''' El aumento de los egresos (US\$ 3.396 m) se origina en su mayoría en la mayor renta obtenida por las empresas con inversión
         directa (US\$ 2.646 m). Los pagos de intereses de la deuda externa aumentaron en US$ 749 m.''',icon='🔎')
 
st.markdown('''Los ingresos por renta de los factores tuvieron un crecimiento anual del 9.6% ascendiendo a US\$ 5.475m. Estos ingresos
             se originaron principalmente en las inversiones directas de Colombia en el exterior. (US\$ 3.912m), seguidos de los
            ingresos por rendimiento de la inversión de cartera (US\$988m) y los redimientos asociados al portafolio
            de inversión de las reservas internacionales (US\$ 550m).''')
 
 
# Transferencias corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias-corrientes')
 
st.markdown('''En 2017 se obtuvieron **ingresos netos superiores en 13.6% a los registrados en 2015**, con un monto total de US\$ 6.685 m.
            Las remesas de trabajadores ascendieron a  US\$ 5.585 (1.8% del PIB), registrando un incremento anual del 15.0% ''')
 
st.warning('''El 44% de las remesas observadas fueron enviadas desde Estados Unidos, el 56% restante  estuvo explicado por un aumento
           de las remesas de América Latina, Canadá y Australia''', icon='💡')
 
st.markdown('''Los ingresos por otras transferencias tuvieron un incremento de 135m  respecto al año anterior
            al registrarse una cifra de US$ 1.973 m. Los egresos por transferencias al exterior tuvieron un incremento anual de 8.0%.''')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias-corrientes)')
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[4:17,]
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
 
st.markdown('''**La cuenta financiera (incluyendo activos de reserva) en 2017, registró entradas netas de capital
            por US\$ 9.694m (3.1% del PIB)**. Cifra inferior en US\$2.989m a lo un año atrás. Estas entradas se
            explican por ingresos de capital extranjero (US\$20.107m), salidas de capital colombiano (US\$9.665m), pagos por conceptos de derivados
            financieros (US\$203m) y aumento de reservas internacionales por transacciones de la balanza de pagos
            (US\$545m)''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[16:17,]
total = financiera[['Año','Cuenta financiera']]
financiera = financiera.drop('Cuenta financiera',axis=1)
 
financiera_melted=pd.melt(financiera,id_vars='Año',var_name='Grupo',value_name='Valor')
financiera_melted['Año'] = financiera_melted['Año'].astype('str')
total['Año'] = total['Año'].astype('str')
 
paleta= sns.color_palette(['#6A8CAF','#7A4F6D','#C5C6C7','#E8D2A6','#96C5F7'])
 
plt.figure(figsize=(10, 6))
sns.barplot(x='Año',y='Valor',hue='Grupo',data=financiera_melted,dodge=True,palette= paleta)
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