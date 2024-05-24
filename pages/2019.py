import streamlit as st
import pandas as pd
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
 
# st.set_page_config(page_title='2019',page_icon=':calendar')
st.header('Resultados Globales')

 
col1, col2, col3 = st.columns(3, gap='large')
 
with col1:
    st.info('Cuenta Corriente :bar_chart:')
    st.metric(label='Déficit', value= "US$13.800", delta="4.3% PIB",delta_color='inverse')
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$13.102", delta="4.1% PIB", delta_color='inverse')
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$689")
 
# Resultados Globales
 
st.markdown('''- Durante 2019, la cuenta corriente aumentó su déficit en US\$753 al registrar un monto de US\$ 13.800 m.
            Como proporción del PIB, este déficit fue 0.4p.p mayor al estimado un año atrás y se ubicó en 4.3%.
- La cuenta financiera para 2019, registró entradas netas de capital por US\$ 13.102 m, cifra que supero en  US\$687 lo
            registrado en 2018.
- Se estimaron errores y omisiones por US\$689m''')
 
# Cuenta Corriente
st.header(':blue[Cuenta Corriente]')
 
st.markdown('''Considerando los componentes de la balanza de pagos, el **déficit corriente (US\$13.800)
            está explicado por los balances deficitarios** obtenidos en los rubros de **renta de los factores** (US\$ 10.309m), **comercio exterior de bienes** (US\$8.447)
             y **servicios** (US\$3.720m). Estos desbalances fueron **compensados parcialmente** por el **balance superavitario de las transferencias corrientes** (US\$8.676m)''')
 
st.sidebar.markdown("[Cuenta Corriente](#cuenta-corriente)")
 
st.warning('''El incremento se originó en el aumento en dólares del déficit corriente y del efecto de la depreciación del peso frente al dólar
           en la medición del PIB nominal en dólares, esto estuvo compensado parcialmente por el crecimiento del PIB nominal''', icon='⚠️')
 
# Gráfica Cuenta Corriente
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[6:19,]
df = df.drop(['Cuenta corriente'], axis=1).loc[6:19,]
 
 
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
 
st.markdown(''' El comercio exterior en 2019 registró un balance deficitario de US\$ 8.447 m, superior en  US\$5.144m.
            El descenso exportador se originó principalmente en las **menores ventas** al exterior de **carbón** (US\$1.780m), **petróleo** (US\$869m)
            y **productos industriales** (US\$171 m). En contraste se registraron **incrementos en las ventas de oro no monetario** (US\$ 435)
            y **banano** (US\$68m).
''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[6:19,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[6:19,]
 
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
 
st.info('''La reducción en las ventas externas de carbón se dió por un efecto combinado de menor volumen exportado (14.0%)
        y la reducción de su precio de exportación (11.7%). El menor valor exportado de petróleo crudo se explica por la
        reducción en su precio de venta (7.2%) que estuvo compensado parcialmente por el alza en sus cantidades vendidas (1.3%) ''',icon="🔎")
 
st.markdown('''El valor importado de mercancías durante 2019 sumó USD\$ 50.821m, con un incremento anual de 2.5%''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios'+ ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''El comercio exterior de servicios registró en 2019 un balance deficitario de US\$3.720m, cifra ligeramente inferior a la
            reportada un año atrás (US\$3.782m) ''')
 
st.sidebar.markdown('- [Balanza comercial Servicios](#balanza-servicios)')
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[6:19,]
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
 
st.markdown(''' **Las exportaciones de servicios aumentaron 3.5%**, principalmente por mayores ingresos de servicios empresariales,
            especialmente relacionada con actividades de call center. De igual manera, aumentaron los servicios de viajes y de
             transporte. Por su parte, disminuyeron los ingresos asociados a otros servicios.
            ''')
 
st.warning('''Los ingresos corrientes provenientes de servicios se concentran mayoritariamente en rubros de viajes y transporte,
            ya que representan cerca del 76% de las exportaciones.''', icon='💡')
 
st.markdown('''**Las importaciones de servicios registraron un incremento anual de 2%** por mayores egresos por conceptos de seguros
                y financieros, de viajes y de fletes. En contraste, disminuyeron los egresos externos asociados a servicios empresariales
            y otros servicios.''')
 
st.warning('''Los egresos corresponden a gastos por viajes al exterior y servicios de transporte que en conjunto aportan
           el 60% de las importaciones totales de servicios.''', icon='💡')
 
 
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''El ingreso primario obtuvo un balance deficitario por US\$17.423m. Respecto al año anterior, **el déficit disminuyó en US\$1.455m gracias
            gracias a menores egresos vinculados a la inversión extranjera directa.**''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[6:19,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[6:19,]
 
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
 
st.markdown(''' Del total de egresos US\$17.243m, el 56.7% correspondió a la renta obtenidas por empresas con IED, el 28.4% a
            los pagos de dividendos y de intereses por inversiones extranjeras de cartera y en menor cuantía a los
            pagos de intereses de créditos externos.
''')
 
st.info('''**La caída en los ingresos se dio por la reduccion de las ganancias para las empresas dedicadas a las actividades de minas y canteras
        transporte y comunicaciones, explotación petrolera e industrias manufacturera**. La caída en las ganancias
        estuvieron parcialmente compensadas por aumentos en las utilidades de las empresas extranjeras
        de los sectores de comercio, restaurantes y hoteles, suministro de servicios básicos y establecimientos financieros.''',icon ='🚨')
 
st.markdown('''Los ingresos asociados a renta de los factores tuvieron un crecimiento anual de 13.4%, asociados principalmente por inversiones directas
            de Colombia en el exterior.''')
 
# Transferencias Corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias-corrientes')
 
st.markdown('''Durante 2019 se recibieron **ingresos netos de US\$8.676 m, lo que significa un aumento 13.5% (US\$1.033m) respecto a 2018**. Los ingresos por
            remesas de trabajadores llegaron a US\$6.744m con un incremento anual de 6.7%
            inferior al crecimiento del 15.5% del año anterior. La equivalencia del PIB de este rubro es 2.1%''')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias-corrientes)')
 
st.warning('''Se destacó el incremento de las remesas transferidas desde Estados Unidos y Españas con tasas respectivas de crecimiento del 10% y 12%. El
           incremento de las transferencias estadounidenses se asocia a una mejora en los ingresos salariales y el nivel de empleo. Por su parte, las remesas hispanas
           han aumentado por una mayor cantidad de colombianos residentes.''', icon='💡')
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[6:19,]
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
 
st.markdown('''Los ingresos por otras transferencias aumentaron USD\$ 533m respecto 2018, este crecimiento
            se produjo por mayores donaciones recibidas por organismos no gubernamentales y por el incremento de las indemnizaciones
            asociadas a obras civiles.''')
 
# Cuenta Financiera
st.header(':blue[Cuenta Financiera]',anchor='cuenta-financiera')
 
st.markdown('''**La cuenta financiera, incluyendo activos de reserva en 2019, registró entradas netas de capital
            por US\$ 13.012m (4.1 % del PIB)**. Cifra superior en US\$687m a lo reportado en 2018. Estas entradas se
            explican por ingresos de capital extranjero (US\$17.051m), salidas de capital colombiano (US\$533m), salidas por conceptos de derivados
            financieros (US\$84m) y aumento de reservas internacionales por transaciiones de la balanza de pagos
            (US$3.332m)''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[6:19,]
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

