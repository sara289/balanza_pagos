import streamlit as st
import pandas as pd
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
 
# st.set_page_config(page_title='2016',page_icon=':calendar')
st.header('Resultados Globales')

col1, col2, col3 = st.columns(3, gap='large')
 
with col1:
    st.info('Cuenta Corriente :bar_chart:')
    st.metric(label='Déficit', value= "US$12.541", delta="-4.4% PIB",delta_color='inverse')
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$12.764", delta="-4.5% PIB",delta_color='inverse')
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$223")
 
# Resultados Globales
 
st.markdown('''- Durante 2016 el balance de la cuenta corriente arrojó un resultado deficitario de US\$ 12.541 m, lo
            que representó una amplia reducción en US\$ 6.239 frente al año 2015. Como proporción del PIB, el déficit se
            ubicó en 4.4% lo que representa una reducción de 2.0 p.p. frente al déficit registrado en 2015.
- La cuenta financiera incluyendo variación de reservas internaciones, registró entradas de capital por US\$ 12.674 m,
            inferiores en US\$ 5.529 m a lo registrado en 2015. La cuenta financiera como porcentaje del PIB pasó de 6.6% a 4.5%.
- Los errores y omisiones en 2015 se estimaron en US$ 223m.
''')
 
# Cuenta Corriente
 
st.header(':blue[Cuenta Corriente]', anchor='cuenta-corriente')
 
st.markdown('''El **balance deficitario** de US\$12.541 m de la cuenta corriente **se explica principalmente por un balance negativo de la balanza
            comercial de bienes** (US\$10.261 m) y en menor proporción por los balances deficitarios en la **renta de los factores** (US\$ 4.910 m)
            y **comercio exterior de servicios** (US\$ 3.020 m), estos desbalances fueron **compensados parcialmente por** lo ingresos netos de
            **transferencias corrientes** (US\$5.650).
''')
st.warning('''La reducción del déficit corriente en 2016 fue el resultado de un menor déficit de la balanza comercial de bienes, aunque también contribuyeron
          menores déficits en la balanza de servicios, menores egresos netos de ingreso primario y el incremento de ingresos por transferencias corrientes.''', icon='⚠️')
 
st.sidebar.markdown('[Cuenta Corriente](#cuenta-corriente)')
 
#Gráfica
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[3:16,]
df = df.drop(['Cuenta corriente'], axis=1).loc[3:16,]
 
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
 
st.markdown('''En 2016 la balanza comercial obtuvo un balance deficitario de US$10.261m, inferior al balance negativo de 2015.''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
 
# Gráfica Balanza Comercial Bienes
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[3:16,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[3:16,]
 
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
 
st.info('''Las **exportaciones totales** de bienes del país **registraron** US\$32.965 m con **una variación anual de -13.4%**. El descenso en el valor total
         exportado se originó principalmente **por menores ventas de petróleo y sus derivados** (US\$ 4.139 m), y en menor medida por la **caída** en los despachos
        al exterior de **productos industriales** (US\$ 880 m) y de **café** (US\$1.403 m). La caída en valor exportado del crudo se dio por una reducción más que
        proporcional de sus volúmenes despachados (24.9%) frente a un incremento de su precio de exportación (22.5%)''',icon="🚨")
 
st.markdown('''Por su parte, las compras externas bienes se ubicaron en US$43.226 m, representado una disminución anual del 17.0%.''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios'+ ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''Al igual que la balanza comercial de bienes, **el comercio exterior de servicios registró en 2016 un déficit de US\$ 3.020m**,
            cifra que estuvo US\$ 1.516 m por debajo del déficit de 2015.''')
 
st.sidebar.markdown('- [Balanza comercial Servicios](#balanza-servicios)')
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[3:16,]
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
 
st.markdown('''Las **exportaciones de servicios reportaron un crecimiento anual de 5.2%** al ascender a US\$ 7.796 m. Este resultado
            estuvo impulsado por mayores ingresos por concepto de viajes que estuvieron parcialmente compensados por la reducción de
            los ingresos asociados a servicios de transporte y otros empresariales.
''')
st.markdown('''Las **importaciones de servicios registraron una caída anual de 9.4%**, en razón a una reducción de los egresos por
             servicios empresariales y de construcción especialmente vinculados a la actividad petrolera.''')
 
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''Se estima que el **balance deficitario del ingreso primario** fue de US\$ 4.910 m. En comparación con 2015, el déficit de
            este rubro **fue inferior en US\$ 616 m (11%)**. El menor balance deficitario se explica por el aumento de los ingresos (US\$ 491m)
            y menor proporción por la caída de los egresos por renta factorial (US\$ 125 m).
''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[3:16,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[3:16,]
 
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
 
st.markdown('''Del total de egresos (US\$ 9.884 m), el 46.8% correspondió a la renta obtenida por las empresas con IED (US\$ 4.626 m)
            el 37.5% en los pagos de intereses por títulos de deuda (US\$ 3.708 m) y el 15.5% en los pagos de intereses de préstamos
            y otros créditos externos (US\$ 1.528 m)
              ''')
 
st.info('''**La disminución de los egresos por utilidades de la IED se explica por pérdidas de las firmas petroleras**, debido a una menor
         producción y menores precios promedio de las exportaciones.  A esta reducción se le suman menores ganancias obtenidas por
        compañías extranjeras de industrias manufactureras, minera, comercio, restaurantes y hoteles.''',icon='🔎')
 
st.markdown('''Los ingresos por renta de los factores mantuvieron un crecimiento anual del 11.0% ascendiendo a US$ 4.439 m. Estos ingresos
             se originaron en las inversiones directas de Colombia en el exterior efectuadas por empresas manufactureras, minera, comercio,
             restaurantes y hoteles.''')
 
 
# Transferencias corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias-corrientes')
 
st.markdown('''En 2016 se obtuvieron **ingresos netos superiores en 7.6% a los registrados en 2015**, con un monto total de US\$ 5.650 m.Las remesas de
             trabajadores totalizaron US\$ 4.858 (1.7% del PIB), registrando un incremento anual del 4.8% ''')
 
st.warning('''Para 2016 se destaca el número de transferencias remitidas desde Chile, Ecuador y Panamá''', icon='💡')
 
st.markdown('''Los ingresos por otras transferencias tuvieron un incremento del 5.9%, respecto al año anterior
             US$ 1.823 m. Los egresos por transferencias al exterior tuvieron una reducción anual de 17.4%.''')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias-corrientes)')
 
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[3:16,]
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
 
st.markdown('''**La cuenta financiera (incluyendo activos de reserva) en 2016, registró entradas netas de capital
            por US\$ 12.764 (4.5% del PIB)**. Cifra inferior en US\$5.529m a lo observado en 2015. Estas entradas de
            explican por ingresos de capital extranjero (US\$24.108m), salidas de capital colombiano (US\$11.820m), pagos por conceptos de derivados
            financieros (US\$640m) y aumento de reservas internacionales por transacciones de la balanza de pagos
            (US\$165m)''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[3:16,]
total = financiera[['Año','Cuenta financiera']]
financiera = financiera.drop('Cuenta financiera',axis=1)
 
financiera_melted=pd.melt(financiera,id_vars='Año',var_name='Grupo',value_name='Valor')
financiera_melted['Año'] = financiera_melted['Año'].astype('str')
total['Año'] = total['Año'].astype('str')
 
paleta= sns.color_palette(['#6A8CAF','#7A4F6D','#C5C6C7','#E8D2A6','#96C5F7'])
 
plt.figure(figsize=(10, 6))
sns.barplot(x='Año',y='Valor',hue='Grupo',data=financiera_melted,dodge=False,palette= paleta)
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
