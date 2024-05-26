import streamlit as st
import pandas as pd
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
 
# st.set_page_config(page_title='2022',page_icon=':calendar')
st.header('Resultados Globales')

 
col1, col2, col3 = st.columns(3, gap='large')
 
with col1:
    st.info('Cuenta Corriente :bar_chart:')
    st.metric(label='Déficit', value= "US$21.466", delta="6.2% PIB",delta_color='inverse')
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$20.460", delta="5.9% PIB",delta_color='inverse')
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$1.154")
 
# Resultados Globales
 
st.markdown('''- Los resultados globales de la balanza de pagos para 2022 muestran un resultado deficitario en la cuenta corriente de
            US\$21.466m equivalente al 6.2% del PIB, este desbalance es superior en US\$3.456m y en 0.6 p.p. a lo observado el año anterior.
- La cuenta financiera, incluyendo un aumento de reservas internacionales por US\$571m, registró entradas netas de capital por
            US\$20.460 que equivalen al 5.9% del PIB. Este monto fue superior en USD\$6.946m y en 0.7 p.p. frente a lo reportado en el año
            anterior.
- Se estimaron errores y omsiones por US\$986m''')
 
# Cuenta Corriente
st.header(':blue[Cuenta Corriente]')
 
st.markdown('''**El déficit en la cuenta corriente se originó por balances deficitarios en los rubros de  renta de los factores y comercio exterior de bienes y servicios**
            que tuvieron cifras de US\$17.209 m, US\$11.818m y US\$ 4.761 m respectivamente. Estos resultados fueron **compensados por un superávit de los ingresos
            secundarios** con un monto de US\$12.342. **Este nuevo balance deficitario se explica principalmente por el  incremento en los egresos asociados a la renta de
            los factores(US\$8.646m)** y en menor medida por la balanza bienes y servicios (US\$2.166m y US\$1.287m)''')
 
st.info('''El incremento (0.6 pp.) se originó en el aumento en dólares
del déficit corriente (1.1 pp.) y por el efecto de la depreciación del peso frente al dólar en la
medición del PIB nominal en dólares (0.5 pp.), que estuvo compensado por el crecimiento
del PIB nominal (1.0 pp.)''',icon='🚨')
 
st.sidebar.markdown("[Cuenta Corriente](#cuenta-corriente)")
 
# Gráfica Cuenta Corriente
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[9:22,]
df = df.drop(['Cuenta corriente'], axis=1).loc[9:22,]
 
 
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
 
st.markdown(''' **El comercio exterior durante 2022 registró un balance deficitario de US\$ 11.818m**, inferior en US\$2.166 m al reportado en 2021.
            **Este resultado se produjo ya que aumento  abruptamente el valor de importaciones (US\$ 71.582 m) por encima de los ingresos asociados a exportaciones (US\$ 59.764m)** ''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[9:22,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[9:22,]
 
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
 
st.markdown('''**Los ingresos por exportaciones de mercancías sumaron US\$59.764m y lograron un incremento anual del 39.8%.**
            Aunque este aumento fue generalizado, se originó principalmente por mayores ventas de carbón, petróleo y sus
            derivados, y en menor medida, en los productos industriales y de café.''')
 
st.info('''El mayor valor exportado de carbón y petróleo crudo se dio tanto por un aumento en los precios de exportación
        (82.9% y 28.5% respectivamente) como en las cantidades despachadas (2.2% y 3.4% respectivamente). Las mayores compras en el extranjero de café se debe a un aumento
        en los precios (33.3%) que compesó la caída en las cantidades vendidas (8.8%)''',icon='🔎')
 
st.markdown('''**Las compras realizadas al exterior totalizaron US$71.582m, con un incremento anual de 26.2%.**
            El aumento fue generalizado y se explicó por mayores importaciones de insumos y de bienes de capital, combustibles
            y lubricantes, equipo de transporte y bienes de consumo.''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios'+ ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''En 2022 el comercio exterior de servicios registró un déficit de US\$4.761m, cifra inferior en US\$ 1.287m (21.0%) respecto a lo
            reportado el año anterior ( US\$6.517m) ''')
 
st.sidebar.markdown('- [Balanza comercial Servicios](#balanza-servicios)')
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[9:22,]
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
 
st.markdown('''La canasta exportadora de servicios estuvo compuesta principalmente por ventas de servicios tradcionales que aportaron el
            66% del valor total, seguido de las ventas de servicios modernos con una participación del 30% (se destacan las exportaciones de
            contact center, informática y consultoría y gestión empresarial)''')
 
st.warning(''' Las exportaciones de servicios aumentaron especialmente por servicios de viajes, ya que se registró un mayor
           número de viajeros internacionales  que arribaron al paí, según cifras de Migración Colombia se registaron aproximadamente
           2'200.000 viajeros más que en 2021.''', icon ='💡')
 
st.markdown(''' Por su parte, los egresos asociados a la importación de servicios sobresalen las compras de servicios
            tradicionales con una contribución del 61%, por su parte las compras de servicios modernos  tuvieron una participación de 26%. Se destaca la participación de
            uso de propiedad intelectual e informática. ''')
 
 
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''Se estimó un balance deficitario en el rubro de la renta factorial por US\$17.209m. En comparación con 2021, el resultado deficitario
            fue superior en US\$ 8.486m, explicado principalmente por los mayores egresos de las utilidades vinculadas a la IED.''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[9:22,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[9:22,]
 
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
 
st.markdown('''Del total de egresos, el 66.5% correspondió a la renta para las compañias con IED, el 21% a los pagos de dividendos
            e intereses asociados a inversiones extranjeras de cartera y el 12.5% a los pagos de intereses de créditos externos.''')
 
st.info('''El aumento de los egresos por concepto de utilidades con IED fue generalizado, sin embargo, se destacan los resultados
        obtenidos  principalmente por firmas dedicadas a las actividades de minera y cantera y explotación petrolera. También aumentaron
        pero en menor proporción las utilidades de establecimientos financieros y servicios empresariales, industrias
        manufactureras, comercio, restaurante y hoteles y suministro de servicios básicos.''',icon='🔎')
 
st.markdown('''Los ingresos por renta de los factores se estimaron en US\$ 6.850m. El 66.5% correspondió a la inversiones directas de Colombia
            en el exterior, el 26% a los rendimientos de la inversión de cartera, el 10% a asociados de reservas internacionales y el 9%
            a rentas asociadas a depósitos y otros activos en países extranjeros.''')
 
# Transferencias Corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias-corrientes')
 
st.markdown('''**El rubro de transferencias corrientes obtuvó un balance superavitario de US\$9.429m y un aumento anual del 9.7%.**
           Los ingresos por remesas de trabajadores tuvieron un aumento anual del 9.7% y ascendieron a US\$9.429m. Su equivalencia del PIB fue de 2.7%. Del total
           de transferencias se destacaron los envios de USA y Reino Unido. ''')
 
st.warning('''Se mantiene la tendencia alcista de transferencias estadounidenses gracias a mejores tasas de empleo para las personas de habla hispana. En Reino Unido,
           la actividad económica muestra una actividad económica apropiada que favorece la reducción del desempleo.''', icon='💡')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias-corrientes)')
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[9:22,]
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
 
#  Cuenta financiera
 
st.header(':blue[Cuenta Financiera]',anchor='cuenta-financiera')
 
st.markdown('''**La cuenta financiera (incluyendo activos de reserva) en 2022, registró entradas netas de capital
            por US\$ 20.460m (5.9% del PIB)**. Cifra superior en US\$3.649m a lo reportada en 2021. Estas entradas se
            explican por ingresos de capital extranjero (US\$33.020m), salidas de capital colombiano (US\$11.166m), pagos por conceptos de derivados
            financieros (US\$823m) y aumento de reservas internacionales por transacciones de la balanza de pagos
            (US\$571m)''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[21:22,]
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