import streamlit as st
import pandas as pd
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
 
# st.set_page_config(page_title='2021',page_icon=':calendar')
st.header('Resultados Globales')

col1, col2, col3 = st.columns(3, gap='large')
 
with col1:
    st.info('Cuenta Corriente :bar_chart:')
    st.metric(label='Déficit', value= "US$17.833", delta="5.7% PIB",delta_color='inverse')
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$16.679", delta="5.3% PIB",delta_color='inverse')
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$1.154")
 
# Resultados Globales
 
st.markdown('''- Los resultados globales de la balanza de pagos para 2021 señalan un déficit de la cuenta corriente de
            US\$17.833m quivalente al 5.7% del PIB, este desbalance es superior en US\$8.626m y en 2.3 p.p. a lo observado en 2020.
- La cuenta financiera, incluyendo un aumento de reservas internacionales por US\$654m, registró entradas netas de capital por
            US\$16.679 que equivalen al 5.3% del PIB. Este monto fue superior en USD\$8.488m y en 2.3 p.p. frente a lo reportado en el año
            anterior.
- Se estimaron errores y omisiones por US\$1.154m''')
 
# Cuenta Corriente
st.header(':blue[Cuenta Corriente]')
 
st.markdown('''**El resultado deficitario se origina por balances deficitarios en los rubros de  comercios exterior de bienes y servicios y renta de los factores**
            que tuvieron cifras de US\$13,984 m, US\$6,517 m y US\$ 8,054 m respectivamente. Estos resultados fueron **compensados por un superávit de los ingresos
            secundarios** con un monto de US\$10.722. **Este nuevo balance deficitario se explica principalmente por la ampliación del déficit de bienes (US\$5.114m)**
            y en menor medida por el ingreso primario y la balanza de servicios (US\$8.054m y US\$6.157m)''')
 
st.info('''El incremento (2.3 pp.) se originó en el aumento en dólares
del déficit corriente (3.0 pp.) y por el efecto de la depreciación del peso frente al dólar en la
medición del PIB nominal en dólares (0.1 pp.), que estuvo compensado por el crecimiento
del PIB nominal (0.8 pp.)''',icon='🚨')
 
st.sidebar.markdown("[Cuenta Corriente](#cuenta-corriente)")
 
# Gráfica Cuenta Corriente
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[8:21,]
df = df.drop(['Cuenta corriente'], axis=1).loc[8:21,]
 
 
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
 
st.markdown(''' **El comercio exterior durante 2023 registró un balance deficitario de US\$ 13.984m**, superior en US\$5.114 m al reportado un año atrás.
            **Este resultado se produjo ya que aumento el valor de importaciones (US\$ 56.719 m) por encima de los ingresos asociados a exportaciones (US\$ 42.375m)** ''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[8:21,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[8:21,]
 
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
 
st.markdown('''**Los ingresos por exportaciones de mercancías sumaron US\$42.375m, con un crecimiento anual del 32.3%.**
            Este aumento se originó por **mayores ventas de petróleo y sus derivados**, y en menor proporción, en los **productos
            industriales, carbón y café.**''')
 
st.info('''**El mayor valor exportado** de petróleo crudo, carbón y café se produjo por un **aumento
        en sus precios de exportación** (62.7%, 59.8% y 27.3% respectivamente) que compensó parcialmente la **disminución en las
        cantidades despachadas** (14.5%, 16.2% y 1.2% respectivamente).''',icon='🔎')
 
st.markdown('''El valor de las importaciones totalizó US\$56.719m con un incremento anual de 37.7%. Este aumento fue generalizado
            y se explica por mayores ventas en el exterior de insumos y bienes de capital para la industria, seguida
            de bienes de consumo y combustibles y lubricantes.''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios'+ ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''Durante 2020 el comercio exterior de servicios registró un déficit de US\$6.517m, cifra superior en US\$ 4.286m (52.0%) respecto a lo
            reportado el año anterior (US\$ 4.286m) ''')
 
st.sidebar.markdown('- [Balanza comercial Servicios](#balanza-servicios)')
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[8:21,]
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
 
st.markdown('''Las exportaciones de servicios estuvieron compuestas principalmente por ventas de servicios
            tradicionales (transporte y turismo) y de servicios modernos (contact center, servicios administrativos y de gestión empresarial)
             con participaciones del 52% y 41% repectivamente.''')
 
st.warning('''El crecimiento exportador se dio por un mayor número de viajeros internacionales que arribaron al país. En lo que respecta a los
           servicios modernos, aumentaron principalmente con servicios de contact center.''', icon='💡')
 
st.markdown('''Por su parte,dentro de los egresos asociados a la importación se destaca la participación de servicios tradicionales
            y servicios modernos (pagos por uso de propiedad intelectual y servicios de informática) y demás servicios que aportaron
            el 52%, 27%, 21% del valor total, respectivamente.''')
 
 
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''**Se estimó un balance deficitario en el ingreso primario por US\$3.215m**. En comparación con 2020, el resultado deficitario
            fue superior en US\$3.215m, explicado mayoritariamente por los mayores egresos de las utilidades vinculadas a la IED.''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[8:21,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[8:21,]
 
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
 
st.markdown('''Del total de egresos US$9.835 m, el 54.8% correspondió a la renta de las empresas con IED,
             el 32.5% a los pagos de dividendos e intereses por inversiones extranjeras directas y en menor
             cuantía por los pagos de intereses de créditos externos.''')
 
st.info('''**El aumento de los egresos se origina principalmente en el incremento de las utilidades con IED de compañias
        dedicadas a actividades de explotación petrolera**, minas y cantera, establecimientos financieros y servicios
        empresariales y transporte y telecomunicaciones.''', icon ='🔎')
 
st.markdown('''Los ingresos por renta de los factores se estimaron en US\$ 5,852 m, cifra que estuvo por encima en US\$ 1,447
            a lo estimado un año atrás. Estos ingresos se originaron principalmente  en la renta asociada con las inversiones
            directas de Colombia en el exterior.''')
 
# Transferencias Corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias-corrientes')
 
st.markdown('''**Los ingresos netos asociados con el rubro de ingreso secundario totalizaron US\$10.722m lo que representó un aumento del 22% (US\$1.935m) respecto a 2020.**
            Los ingresos por remesas de trabajadores ascendieron a US$8.957m, con un incremento anual del 24.4%. Estas transferencias equivalen al 2.7% del PIB anual. Se destacó
            el crecimiento de los envios provinientes de USA,España y América Latina con crecimientos respectivos del 24%, 19% y 29% anualmente.''')
 
st.warning('''Las mayores remesas de USA se asocian a mejores ingresos de los migrantes, gracias a menores tasas de desempleo en los últimos meses y al efecto compensador de los
           seguros de desempleo.En lo que respecta a España, el nivel de envios se recupero por mejores niveles de empleo y las ayudas gubernamentales
           que permiten mantener el ingreso de los hogares.''', icon='💡')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias-corrientes)')
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[8:21,]
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
 
st.markdown('''Los ingresos por otras transferencias totalizaron US\$3.253 m en 2021, monto superior en US\$508m respecto al año anterior. Los recursosnuevamente fueron
            recibidos en su mayoría por entidades públicas,el gonierno, organismos no gubernamentales e instituciones sin ánimo de lucro''')
 
#  Cuenta financiera
 
st.header(':blue[Cuenta Financiera]',anchor='cuenta-financiera')
 
st.markdown('''**La cuenta financiera, incluyendo activos de reserva en 2021, registró entradas netas de capital
            por US\$ 16.679m (5.3% del PIB)**. Cifra superior en US\$8.488m a lo reportada en 2020. Estas entradas se
            explican por ingresos de capital extranjero (US\$27.238m), salidas de capital colombiano (US\$9.539m), pagos por conceptos de derivados
            financieros (US\$366m) y aumento de reservas internacionales por transacciones de la balanza de pagos
            (US\$654m)''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[8:21,]
 
total = financiera[['Año','Cuenta financiera']]
total['Año'] = total['Año'].astype('str')
financiera = financiera.drop('Cuenta financiera',axis=1)
 
financiera_melted=pd.melt(financiera,id_vars='Año',var_name='Grupo',value_name='Valor')
financiera_melted['Año'] = financiera_melted['Año'].astype('str')
 
paleta= sns.color_palette(['#6A8CAF','#7A4F6D','#C5C6C7','#E8D2A6','#96C5F7'])
 
 
sns.barplot(x='Año',y='Valor',hue='Grupo',data=financiera_melted,dodge=False,palette= paleta)
sns.lineplot(x='Año',y='Cuenta financiera',data=total,color='navy')
 
plt.title('Cuenta Financiera',weight ='bold')
plt.axhline(0,linewidth=0.5,color='black')
plt.xlabel('Año')
plt.ylabel('Millones USD')
plt.xticks(rotation=45)
plt.legend(loc='lower center',bbox_to_anchor=(0.5,-0.30),ncol=3)
 
 
st.pyplot()
st.caption('Fuente: Banco de la República, elaboración propia.')