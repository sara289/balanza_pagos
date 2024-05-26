import streamlit as st
import pandas as pd
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
 
# st.set_page_config(page_title='2015',page_icon=':calendar')
st.header('Resultados Globales')

 
col1, col2, col3 = st.columns(3, gap='large')
 
with col1:
    st.info('Cuenta Corriente :bar_chart:')
    st.metric(label='Déficit', value= "US$18.925", delta="6.5% PIB", delta_color= "inverse")
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$19.201", delta="6.6% PIB", delta_color= "inverse")
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$642")
 
# Resultados Globales
 
st.markdown('''- Durante 2015 el balance de la cuenta corriente arrojó un resultado deficitario de US\$ 18.925 m,
            lo que representó una leve reducción en US\$ 668 frente al año 2014. Como proporción del PIB, el
            déficit se ubicó en 6.5% lo que representa un aumento de 1.3 p.p. frente al déficit de 5.2% registrado
            en 2014.
''')
st.error('''**Importante:** El incremento del déficit como proporción del PIB no solo refleja el menor valor absoluto del déficit,
           si no que a su vez está explicado por la reducción del PIB corriente en dólares, debido a la depreciación
           del 37% del peso entre 2014 y 2015.''', icon='🚨')
 
st.markdown('''- La cuenta financiera incluyendo variación de reservas internaciones, registró entradas de capital por US\$ 19.201 m,
            inferiores en US\$ 635 m a lo registrado en 2014. La cuenta financiera se elevó de 5.2% a 6.6%, también explicado por
            el efecto de la depreciación del peso sobre la medición en dólares del PIB corriente.
- Los errores y omisiones en 2015 se estimaron en US$ 276m.''')
 
# Cuenta Corriente
 
st.header(':blue[Cuenta Corriente]', anchor='cuenta-corriente')
 
st.markdown('''El **resultado deficitario** de US\$18.925 m de la cuenta corriente **está explicado por un balance negativo de la balanza
            comercial de bienes** (US\$14.026 m) y en menor proporción por los balances deficitarios en la **renta de los factores** (US\$ 5.989 m)
            y **comercio exterior de servicios** (US\$ 3.981 m), estos desbalances fueron **compensados parcialmente por** lo ingresos netos de
            **transferencias corrientes** (US\$5.071).
''')
 
st.markdown('''El **déficit disminuyó** levemente en US\$ 668m, **gracias a menores egresos netos de la cuenta de renta de los factores** (US\$ 6.650 m)
             y a su vez por la **reducción del déficit del componente de servicios** (US\$ 2.701 m)
''')
 
st.sidebar.markdown('[Cuenta Corriente](#cuenta-corriente)')
 
# Gráfica
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[2:15,]
df = df.drop(['Cuenta corriente'], axis=1).loc[2:15,]
 
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
 
st.markdown('''En 2015 la balanza comercial obtuvo un **balance deficitario** de US$14.026 m, **muy superior** al balance negativo de 2014.''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
 
# Gráfica Balanza Comercial Bienes
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[2:15,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[2:15,]
 
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
 
st.info('''Las **exportaciones totales** de bienes del país **registraron** US\$38.125 m con **una variación anual de -33.0%**. El descenso en el valor total
         exportado se originó principalmente **por menores ventas de petróleo y sus derivados** (US\$ 14.646 m), y en menor medida por la **caída del
        valor de las exportaciones de carbón** (US\$ 2.250m) y de **productos industriales** (US\$ 1.403m).  La caída en valor exportado del crudo se dio
        por una reducción del 50.1% del precio de exportación.''',icon="🚨")
 
st.markdown('''Por su parte, las compras externas bienes se ubicaron en US$52.151 m, representado una disminución anual del 15.3%.''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios'+ ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''Al igual que la balanza comercial de bienes, el comercio exterior de servicios registró en 2015 un déficit de US\$ 3.981m,
            cifra que estuvo US\$ 2.701m por debajo del déficit de 2014.
            ''')
 
st.sidebar.markdown('- [Balanza comercial Servicios](#balanza-servicios)')
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[2:15,]
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
 
st.markdown('''Las **exportaciones de servicios reportaron un crecimiento anual de 5.7%** al ascender a US\$ 7.265 m. Este resultado
            estuvo impulsado por mayores ingresos por concepto de viajes (US\$ 4.245 m) y transporte (US\$ 1.593 m), que en conjunto
            representan el 80% de las exportaciones.
''')
 
st.markdown('''Las **importaciones de servicios registraron una caída anual de 17.0%**, en razón a una reducción de los egresos por
             servicios empresariales y de construcción especialmente vinculados a la actividad petrolera.''')
 
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''Se estima que el **balance deficitario del ingreso primario** fue de US\$ 5.989 m. En comparación con 2014, el déficit de
            este rubro **fue inferior en US\$ 6.650 m (52.6%), motivo que explica la reducción del déficit corriente durante 2015**. El
            menor balance deficitario se explica por caída en los egresos por renta factorial, principalmente por concepto de utilidades,
            y en menor proporción por el aumento de sus ingresos.)
''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[2:15,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[2:15,]
 
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
 
st.markdown('''Del total de egresos (US\$ 10.427 m), el 57% correspondió a la renta obtenida por las empresas con IED (US\$ 5.921 m)
             y en menor cuantía en los pagos de interese por títulos de duda y préstamos y otros créditos externos. ''')
 
st.info('''**Los egresos por utilidades de la IED cayeron 51% anualmente por menores ganancias de las firmas que operan en la actividad
         petrolera** (95.0%) debido a menores precios de exportación de petróleo crudo.''',icon='🔎')
 
st.markdown('''Los ingresos por renta de los factores registraron un crecimiento anual del 11.0% ascendiendo a US$ 4.439 m. Estos ingresos
             se originaron en las inversiones directas de Colombia en el exterior efectuadas por empresas manufactureras, bancarias,
            eléctricas y de pensiones. ''')
 
 
# Transferencias corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias-corrientes')
 
st.markdown('''En 2015 se obtuvieron **ingresos netos superiores en 16.4% a los registrados en 2014**, con un monto total de US\$ 5.071 m.Las remesas de
             trabajadores totalizaron US\$ 4.636 (1.6% del PIB), registrando un incremento anual del 13.2% ''')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias-corrientes)')
 
st.warning('''El 45% de las transferencias fueron remitidas desde Estados unidos''', icon='💡')
 
st.markdown('''Los ingresos por otras transferencias tuvieron un nivel similar al registrado en el año inmediatamente anterior al sumar
             US$ 1.212 m. Los egresos por transferencias al exterior tuvieron una reducción anual de 18%.''')
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[2:14,]
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
 
st.markdown('''**La cuenta financiera (incluyendo activos de reserva) en 2015, registró entradas netas de capital
            por US\$ 19.201m (6.6% del PIB)**. Cifra inferior en US\$635m a lo observado en 2014. Estas entradas se
            explican por ingresos de capital extranjero (US\$24.991m), salidas de capital colombiano (US\$3.849m), pagos por conceptos de derivados
            financieros (US\$1.526m) y aumento de reservas internacionales por transacciones de la balanza de pagos
            (US\$415m)''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[14:15,]
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