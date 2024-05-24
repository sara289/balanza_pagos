import streamlit as st
import pandas as pd
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
 
# st.set_page_config(page_title='2018',page_icon=':calendar')
st.header('Resultados Globales')

 
col1, col2, col3 = st.columns(3, gap='large')
 
with col1:
    st.info('Cuenta Corriente :bar_chart:')
    st.metric(label='Déficit', value= "US$12.661", delta="3.8% PIB",delta_color='inverse')
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$11.981", delta="3.6% PIB", delta_color='inverse')
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$679")
 
# Resultados Globales
 
st.markdown('''- Durante 2018 la cuenta corriente arrojó un resultado deficitario de US\$ 12.661 m, lo
            que representó un aumento en US\$ 2.364 frente a 2017. Como proporción del PIB, el déficit se
            ubicó en 3.8% lo que representa un aumento de 0.5 p.p. frente al déficit registrado en 2017.
- La cuenta financiera incluyendo variación de reservas internaciones, registró entradas de capital por US\$ 11.981 m,
            superior en US\$ 1.187 m a lo registrado en 2017. La cuenta financiera como porcentaje del PIB pasó de 3.1% a 3.6%.
- Los errores y omisiones en 2015 se estimaron en US$ 679m.
''')
 
# Cuenta Corriente
 
st.header(':blue[Cuenta Corriente]', anchor='cuenta-corriente')
 
st.markdown('''El **balance deficitario** de US\$12.661 m de la **cuenta corriente** se explica por los balances deficitarios del rubro de **renta de los factores**
            (USD\$11.441), **comercio exterior de bienes** (US\$5.316 m) y en **servicios** (US\$ 3.809 m). Estos desbalances fueron **compensados parcialmente por**
            ingresos netos de **transferencias corrientes** (US\$5.650).
''')
st.warning('''El balance deficitario en 2018 aumentó US\$2.634 m. Se destaca el incremento en los egresos de renta de los factores y en menor medida el déficit
           comercial de bienes. En cambio los ingresos netos por transferencias corrientes aumentaron.''', icon='⚠️')
 
# Cuenta corriente
st.sidebar.markdown('[Cuenta Corriente](#cuenta-corriente)')
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[5:18,]
df = df.drop(['Cuenta corriente'], axis=1).loc[5:18,]
 
 
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
 
st.markdown('''**Durante 2018 se registró un balance deficitario de US$ 5.316, superior al registrado en 2017**''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
# Gráfica Balanza Comercial Bienes
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[5:18,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[5:18,]
 
bcs_melted = pd.melt(bcs, id_vars=['Año'],var_name='Grupo', value_name='Valor')
 
col1,col2 =st.columns(2,gap='large')
 
with col1:
    sns.barplot(x='Año',y='Valor',hue='Grupo',data=bcs_melted, dodge= True, palette='mako')
    plt.title('Exportaciones e Importaciones de Bienes',weight='bold',fontsize=16)
    plt.xlabel('Fecha')
    plt.ylabel('Millones de USD')
    plt.legend(loc='upper left')
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
 
st.markdown('''**Los ingresos por exportaciones sumaron US\$44.316m con un aumento del 11.7%**. El mayor crecimiento exportador
        se dió por mayores ventas de petróleo y sus derivados, productos industriales,
        ferroníquel, flores, carbón y resto de productos agricolas.En contraste se redujeron las ventas de oro no monetario, café y banano''')
 
st.info('''Se dió un incremento del 8.5%, 11.1% y 19.8% en los precios de exportación de petróleo crudo, ferroníquel y carbón respectivamente. A
        su vez las cantidades disminuyeron 0.1%, 18.5% y 29.4% . La reducción del valor vendio de café se dió por una caída en su precio de exportación
        que contrastó con mayores despachadas.Las exportaciones de banano cayeron por un  menor volumen exportado.''',icon='🔎')
 
st.markdown('''El valor importado de mercancías durante 2018 se ubicó en US$49.633 m, representado un incremento anual de 12.2%.''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios'+ ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''Al igual que la balanza comercial de bienes, el comercio exterior de servicios registró en 2018 un déficit de US\$ 3.809m,
            cifra que estuvo cerca de lo registrado en 2017 (US\$3.917m)''')
 
st.sidebar.markdown('- [Balanza comercial Servicios](#balanza-servicios)')
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[5:19,]
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
 
st.markdown('''Las **exportaciones de servicios reportaron un crecimiento anual de 11.8%** al ascender a US\$ 9.457 m. Este resultado
            estuvo impulsado por mayores ingresos por concepto de viajes, transporte, servicios empresariales y de construcción y de comunicaciones,información  e informático.
''')
st.markdown('''Las **importaciones de servicios registraron un aumento anual de 7.2%**, en razón a una mayores egresos por
             gastos de viaje, servicios de transporte, servicios empresariales y de construcción..''')
 
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''Se estima que el **balance deficitario del ingreso primario** fue de US\$ 11.401m. En comparación con 2017, el déficit de
            este rubro **fue superior en US\$ 2.736 m**. El mayor balance deficitario se explica por mayores egresos (US\$ 491m)
            por las utilidades vinculadas a la inversión extranjera directa (IED) (US\$ 2.736 m).
''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[5:18,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[5:18,]
 
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
 
st.markdown('''Del total de egresos (US\$ 17.253 m), el 59% correspondió a la renta obtenida por las empresas con IED
            el 28.7% en los pagos de intereses y dividendos por inversiones extranjeras de portafolio
              ''')
 
st.info('''Los mayores egresos por utilidades de la IED se explica por el aumento de las ganancias estimadas
        para las compañias en las actividades de transporte, almacenamiento y comunicaciones, explotación petrolera, de minas
        y canteras y de comercio,restaurantes y hoteles. Las mayores ganancias fueron compensaron la reducción de utilidades
        de la industria manufacturera. ''',icon='🔎')
 
st.markdown('''Los ingresos por renta de los factores tuvieron un crecimiento anual del 11.6% ascendiendo a US$ 6.112 m. Se destaca la participación
            mayoritaria  de la renta asociada a inversiones directas de Colombia en el exterior y a su vez aunque con menor participación los ingresos
            por rendimiento de la inversión de cartera y los asociados al portafolio de la inversión de las reservas
            internacionales.''')
 
# Transferencias corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias-corrientes')
 
st.markdown('''En 2017 se obtuvieron **ingresos netos superiores en 15.3% a los registrados en 2017**, con un monto total de US\$ 7.605m.Las remesas de
             trabajadores totalizaron US\$ 6.339m (1.9% del PIB), registrando un incremento anual del 15.3% ''')
 
st.warning('''El 61% de las transferencias fueron realizadas desde Estados Unidos y España, estas
           a su vez aportaron  el 48% y 11% del crecimiento total. El 41% restante se dio por un aumento de las remesas
           provenientes de América Latina, Canadá y Australia. ''', icon='💡')
 
st.markdown('''Los ingresos por otras transferencias tuvieron un incremento del 7.7%, respecto al año anterior
             US$ 1.823 m. Los egresos por transferencias al exterior tuvieron un aumento anual de 7.7%.''')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias-corrientes)')
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[5:18,]
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
 
st.markdown('''**La cuenta financiera (incluyendo activos de reserva) en 2018, registró entradas netas de capital
            por US\$ 11.891 (3.6% del PIB)**. Cifra superior en US\$2.337m a lo observado en 2017. Estas entradas se
            explican por ingresos de capital extranjero (US\$20.143m), salidas de capital colombiano (US\$6.910m), pagos por conceptos de derivados
            financieros (US\$65m) y aumento de reservas internacionales por transacciones de la balanza de pagos
            (US\$1.718m)''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[5:18,]
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