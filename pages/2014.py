import streamlit as st
import pandas as pd
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
 
st.header('Resultados Globales')

col1, col2, col3 = st.columns(3, gap='large')
 
with col1:
    st.info('Cuenta Corriente :bar_chart:')
    st.metric(label='Déficit', value= "US$12.722", delta="3.2% PIB", delta_color= "inverse")
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$19.740", delta="5.1% PIB", delta_color= "inverse")
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$625")
 
# Resultados Globales
 
st.markdown('''- En comparación con el año 2012, se incrementó en US$887 millones en déficit de cuenta corriente.  
            Como proporción del PIB el déficit pasó de 3.1% a 3.2%.
- La cuenta financiera registró un monto superior de US$1.779 millones al 2012.
         En términos del PIB, este superávit se elevó anualmente de 4.7% a 5.1%.
- Se registró una acumulación de reservas de US\$6.165 m originadas en transacciones de balanza de pagos y en
        valorizaciones por tipo de cambio y precio. Esta acumulación fue superior en US\$994 m que en 2012.''')
 
# Cuenta Corriente
 
st.header(':blue[Cuenta Corriente]',anchor='cuenta-corriente')
 
st.markdown('''El **déficit de la cuenta corriente** se explica por el **balance deficitario en la renta de factores**
(US\$ 14.656 m) y del **comercio exterior de servicios** (US \$5.470 m) que fue compensado parcialmente por **ingresos
netos por transferencias corrientes** (US\$4.572 m) y el superávit obtenido en la cuenta de bienes (US\$2.832 m). El
**resultado deficitario** se originó principalmente por el menor superávit comercial que superó los **menores egresos
netos por renta de los factores.**
''')
 
st.sidebar.markdown('[Cuenta Corriente](#cuenta-corriente)')
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[0:13,]
df = df.drop(['Cuenta corriente'], axis=1).loc[0:13,]
 
 
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
 
# Balanza Comercial: Bienes
 
st.subheader('Balanza Comercial de Bienes'+':shopping_trolley:',anchor='balanza-bienes')
 
st.markdown('''La balanza comercial de bienes registró un superávit de US\$2.832, pero menor en US\$1.911 m al superávit
            registrado en 2012, este comportamiento se dio por una reducción de las exportaciones y un incremento de las
            importaciones.''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
 
# Gráfica Balanza Comercial Bienes
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[0:13,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[0:13,]
 
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
    st.pyplot()
 
st.markdown('''El grupo de exportaciones principales representó el 79% de valor exportado por el país.
            Estas a su vez **registraron una disminución del 4.2% que se explicó por una reducción en el
            precio y el volumen exportado de carbón y oro**.
''')
 
st.warning(''':bulb:
            Este grupo está conformado por: carbón, ferroníquel, café, flores, banano, petróleo y oro ''')
 
st.markdown('''En 2013 las compras externas registraron un monto total de US$ 55.031 m, lo que significó un
            aumento anual del 0.7%. Esta cifra se da en razón a un incremento en los volúmenes importados.''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios' + ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''La balanza de servicios tuvo un **balance deficitario** (US$5.470 m), pero su resultado fue similar
            al obtenido en 2012.  Tanto **las exportaciones de servicios como las importaciones registraron
            incrementos anuales**, sin embargo, las exportaciones lo hicieron en mayor proporción que las
            importaciones (9.5% vs 4.3%).  Se destacó la participación de actividades relacionadas con viajes,
            transporte y servicios empresariales.''')
 
st.sidebar.markdown('- [Balanza Comercial Servicios](#balanza-servicios)')
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[0:13,]
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
 
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''Se obtuvo un balance deficitario para el rubro de la renta de los factores, más
            sin embargo este fue 6.4% menor que el registrado en 2012.  Este déficit está explicado
             en mayor proporción por giros netos de las utilidades (US\$ 11.442 m)  y en menor medida
             por pagos netos de intereses (US\$ 3.193m)
''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[0:13,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[0:13,]
 
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
 
# Transferencias corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias_corrientes')
 
st.markdown('''Se registraron ingresos netos de US\$4.572 m, con un nivel similar al registrado en 2012.
             Las remesas de los trabajadores totalizaron US\$ 4.071 m (1.1% del PIB) representado un
            incremento anual del 2.5%. Los ingresos por otras transferencias registraron una caída anual del 3.1%.''')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias_corrientes)')
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[0:13,]
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
 
#Cuenta Financiera
st.header(':blue[Cuenta Financiera]',anchor='cuenta-financiera')
 
st.markdown('''En 2013 la cuenta de capital y financiera registró un superávit de US\$ 19,174 m (5.1% del PIB),
monto superior en US\$ 1,779 m al registrado en 2012. Los ingresos de capital extranjero
ascendieron a US\$ 32,772 m y las salidas de capital colombiano a US\$ 13,598 m.''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[0:13,]
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