import streamlit as st
import pandas as pd
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
 
# st.set_page_config(page_title='2020',page_icon=':calendar')
st.header('Resultados Globales')

 
col1, col2, col3 = st.columns(3, gap='large')
 
with col1:
    st.info('Cuenta Corriente :bar_chart:')
    st.metric(label='Déficit', value= "US$9.083", delta="-3.3% PIB",delta_color='inverse')
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$8.092", delta="-3.0% PIB",delta_color='inverse')
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$992")
 
# Resultados Globales
 
st.markdown('''- En 2020, la cuenta corriente disminuyó su déficit en US\$5.021m al registrar un monto de US\$9.083 m.
            Como proporción del PIB, este déficit fue 1.1 p.p menor al estimado en 2018 y se estimó en 3.3%.''')
 
st.info(''' **La reducción de 1.1 p.p. se originó en la disminución en dólares del déficit en cuenta corriente (1.6 p.p.)**, el cual fue **contrarestado
        parcialmente por la contracción del PIB nominal (0.2 p.p)** y por el **efecto de la depreciación del peso
        frente al dólar en la medición del PIB nominal en dólares (0.3 p.p.)**''', icon='🚨')
 
st.markdown('''- La cuenta financiera en 2020, registró entradas netas de capital por US\$ 8.092m, cifra inferior en US\$5.148m a lo
            registrado en 2019. En términos del PIB, las entradas  netas de capital representaron 3.0%, inferior en 1.1 p.p a lo registrado el año anterior.
- Se estimaron errores y omisiones por US\$992m.''')
 
# Cuenta Corriente
st.header(':blue[Cuenta Corriente]')
 
st.markdown('''El **balance deficitario de la cuenta corriente de 2020 disminuyó  US\$5.201m**. Este resultado se dio **gracias a una disminución
            en los egresos asociados a la renta de los factores** (US\$5.386m) y, en menor proporción, por el **déficit comercial de bienes** (US\$532m).
            A diferencia de los rubros anteriores, **el déficit en la balanza de servicios aumentó en US\$78 m**. Por su parte, **los ingresos secundarios
            se incrementaron** en US\$20 m.
''')
 
st.sidebar.markdown("[Cuenta Corriente](#cuenta-corriente)")
 
# Gráfica Cuenta Corriente
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[7:20,]
df = df.drop(['Cuenta corriente'], axis=1).loc[7:20,]
 
 
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
 
st.markdown(''' **El comercio exterior en 2020 registró un balance deficitario de US\$ 7.918 m**, inferior en US\$532 m al reportado en 2019.
            Este resultado se produjo ya que la disminución en el valor de las exportaciones US\$ 8.886 m fue inferior a la reducción de las
            importaciones US\$9.419 m
''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[7:20,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[7:20,]
 
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
 
st.markdown(''' **Los ingresos asociados a exportaciones de mercancías en 2020 totalizaron US\$33.481m, con una reducción anual
        de US\$8.886m (21%)**.Este descenso fue generalizado y se originó por menores ventas de petróleo y sus derivados, carbón, ferroníquel y flores.
        En constraste aumentaron las ventas externas de oro, café y banano.
''')
 
st.info('''El **menor valor exportado de petróleo crudo, carbón y ferroniquel** se dió por un efecto combinado entre una **reducción
        en su precio de exportación** (38.6%, 22.2% y 9.2% respectivamente) y de un **menor volumen exportado** (10.5%, 4.7% y 10.4% respectivamente). Por su parte,
        **las exportaciones de oro lo hicieron tanto por un mayor volumen exportado (32.2%) como de su precio de exportacion** (27.1%), por su parte las
        mayores **ventas de café se dió por un aumento en sus precios de venta** (16.7%).''',icon='🔎')
 
st.markdown('''El valor importado de las mercancías durante 2020 fue de US\$41.400 con una reducción anual de 18.5% (US\$9.419m).
            Esta disminución fue generalizada y se explica mayoritariamente por menores compras de insumos y bienes de capital, combustibles y lubricantes,
            bienes de consumo y equipo de transporte.''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios'+ ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''Durante 2020 el comercio exterior de servicios obtuvo un balance deficitario de US\$4.503m, cifra superior en US\$ 78m respecto a lo reportado en 2019 (US\$ 4.525m) ''')
 
st.sidebar.markdown('- [Balanza comercial Servicios](#balanza-servicios)')
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[7:20,]
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
 
st.markdown('''Las exportaciones de servicios se ubicaron en US\$5.662m con una reducción anual del 46.5%. Este comportamiento
            se produjo por menores ingresos de viaje (US\$ 4,067 m, 72.0%) y de transporte (US$ 853 m, 41.9%). ''')
 
st.warning('''La reducción de los ingresos por viajes y transporte se dio por los cierres de aeropuertos a nivel mundial como medida
           de contigencia ante la pandemia, con lo que se disminuyó abruptamente el flujo de viajeros movilizados.''', icon ='⚠️')
 
st.markdown('''En cuanto a las importaciones de servicios estas totalizaron US\$ 10,165 m, inferiores
            en 32.3% (US$ 4,848 m), frente al registrado en 2019. Esta reducción está explicado por menores egresos por concepto
            de  viajes, fletes y de servicios empresariales, especialmente relacionados a la actividad petroléra.  ''')
 
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''El ingreso primario obtuvo un balance deficitario por US\$5.386m. Respecto al año anterior, **el déficit disminuyó en US\$4.728m gracias
            gracias a menores egresos vinculados a la inversión extranjera directa (IED).**''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[7:20,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[7:20,]
 
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
 
 
 
st.markdown(''' Del total de egresos US\$9.835 m, el 46.7% correspondió a los pagos de dividendos e intereses por inversiones extranjeras de cartera, el 35.7% a
            la renta obtenida por las empresas con IED y en menor cuantía por los pagos de intereses de créditos externos.
''')
 
st.info('''La caída en los ingresos se dio por la reduccion de las utilidades de las empresas con IED. **La reducción en la utilidades de las empresas fue generalizada en todos
        los sectores económicos** pero se destacan las firmas que operan en actividades de explotación petrolera, servicios financieros
        y empresariales, transporte y comunicaciones, industrias manufactureras y minas y canteras.''',icon ='🔎')
 
st.markdown('''Los ingresos por renta de los factores se estimaron en US\$4.449m, con una disminución anual del 36.8%. Estos se originaron en la renta asociadas a las inversiones
            directas de Colombia en el exterior. Es importante señalar que para 2020 los activos de reserva disminuyeron levemente a (US\$ 66m) a lo reportado en 2019.''')
 
# Transferencias Corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias-corrientes')
 
st.markdown('''En 2020 se recibieron **ingresos netos de US\$8.24 m, lo que significa un leve aumento de 0.2% (US\$20m) respecto a 2019**. Los ingresos por
            remesas de trabajadores llegaron a US\$6.853m con un incremento anual de 1.8%. La equivalencia del PIB de este rubro es 2.5% superior a 2.1% reportado en 2019.''')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias-corrientes)')
 
st.warning('''Las remesas enviadas desde USA crecieron 9.5% anual, mientras que las de América Latina y España tuvieron descensos del 20% y 1% respectivamente.''', icon='💡')
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[7:20,]
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
 
st.markdown('''Los ingresos por otras transferencias sumaron USD\$ 2.736m , eata cifra fue menor en US$196m. Estas tranferencias fueron recibidas
            principalmente por entidades pública, el gobierno central, organismos no gurbenamentales e insituciones sin ánimo de lucro.''')
 
# Cuenta Financiera
st.header(':blue[Cuenta Financiera]',anchor='cuenta-financiera')
 
st.markdown('''**La cuenta financiera, incluyendo activos de reserva en 2020, registró entradas netas de capital
            por US\$ 8.092m (3.0 % del PIB)**. Cifra inferior en US\$5.148m a lo reportado en 2019. Estas entradas se
            explican por ingresos de capital extranjero (US\$23.942m), salidas de capital colombiano (US\$11.579m), pagos por conceptos de derivados
            financieros (US\$507m) y aumento de reservas internacionales por transaciiones de la balanza de pagos
            (US\$4.328m)''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[7:20,]
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
