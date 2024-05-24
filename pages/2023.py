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
    st.metric(label='Déficit', value= "US$9.715", delta="2.7% PIB",delta_color='inverse')
with col2:
    st.info('Cuenta Financiera :bank:')
    st.metric(label='Entradas Netas de Capital', value= "US$8.880", delta="2.4% PIB",delta_color='inverse')
with col3:
    st.info('Errores y Omisiones :money_with_wings:')
    st.metric(label='Estimación', value= "US$836")
 
# Resultados Globales
 
st.markdown('''- Los resultados globales de la balanza de pagos para 2022 muestran un resultado deficitario en la cuenta corriente de
            US\$9.715m equivalente al 2.7% del PIB, este desbalance es inferior en US\$11.652m y en 3.5 p.p. a lo registrado en 2022.
- La cuenta financiera, incluyendo un aumento de reservas internacionales por US\$1.718m, registró entradas netas de capital por
            US\$8.880m que equivalen al 2.4% del PIB. Este monto fue inferior en USD\$11.587m y en 3.5 p.p. frente a lo reportado en el año
            anterior.
- Se estimaron errores y omsiones por US\$836m''')
 
# Cuenta Corriente
st.header(':blue[Cuenta Corriente]')
 
st.markdown('''**El déficit en la cuenta corriente se originó por balances deficitarios en los rubros de  renta de los factores y comercio exterior de bienes y servicios**
            que tuvieron cifras de US\$14.405 m, US\$6.867 m y US\$ 1.533 m respectivamente. Estos resultados fueron **compensados por un superavit de los ingresos
            secundarios** con un monto de US\$12.910.  **Este nuevo balance deficitario se explica por la reducción en los egresos asociados a la renta de
            los factores(US\$2.682)** y en mayor medida por la balanza bienes y servicios (US\$5.310m y US\$3.058m)''')
 
st.info('''La reducción de (3.5 pp.) se originó en la disminución en dólares
del déficit corriente (3.3 pp.) y por el crecimiento del PIB nominal en pesos (0.3 pp.), que estuvieron compensados por el efecto de la depreciación
        del peso frente al dólar en la medición del PIB nominal en dólares (0.1 pp.)''',icon='🚨')
 
st.sidebar.markdown("[Cuenta Corriente](#cuenta-corriente)")
 
# Gráfica Cuenta Corriente
 
df = pd.read_excel('BOP.xlsx',sheet_name='Grafica')
 
cc = df[['Año','Cuenta corriente']].loc[10:23,]
df = df.drop(['Cuenta corriente'], axis=1).loc[10:23,]
 
 
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
 
st.markdown(''' **El comercio exterior durante 2021 registró un balance deficitario de US\$ 6.867**, inferior en US\$5.310m al reportado en 2022.
            **Este resultado se produjo ya que el valor de importaciones (US\$ 59.373 m)  estuvo por encima de los ingresos asociados a exportaciones (US\$ 52.506)** ''')
 
st.sidebar.markdown('- [Balanza Comercial Bienes](#balanza-bienes)')
 
bcs = pd.read_excel('BOP.xlsx',sheet_name='Grafica B.S')
 
bcs['Año'] = pd.to_datetime(bcs['Serie']).dt.year
bcs['Año'] = bcs['Año'].astype('str')
balance_bienes = bcs[['Año','Balanza']].loc[10:23,]
 
bcs = bcs.drop(['Serie','Balanza'],axis=1).loc[10:23,]
 
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
 
st.markdown('''**Las exportaciones de bienes alcanzaron US\$52.506m con una disminución anual de 11.7%.** Esta reducción se produjo
            por menores ventas de carbón, de petróleo crudo y sus derivados y en menor proporción de café. Estas
            reducciones fueron compensadas parcialmente por mayores exportaciones de oro moetario''')
 
st.info('''El menor valor exportado de carbón se produjo por la disminución en los precios implícitos de exportación (21.9%). Por su parte,
        las menores ventas de carbón y café se dio por una reducción de los precios implícitos de exportación (15.0% y 23.2% respectivamente) y por menores cantidades
        vendidas (1.1% y 7.8% en su orden). Las exportaciones de oro, se dieron gracias a un incremento en su precio (7.8%) y las cantidades despachadas (1.3%).''',icon='🔎')
 
st.markdown('''**Al igual que las exportaciones, las importaciones registaron una reducción anual de 17.1 al totalizar  US\$59.373m.**. La reducción está explicada por menores compras de insumos
            y bienes de capital, y en meor medida por las compras de equipo de transporte y de combustibles y lubricantes.''')
 
#Balanza Comercial Servicios
 
st.subheader('Balanza de Servicios'+ ':beach_with_umbrella::oncoming_bus:',anchor='balanza-servicios')
 
st.markdown('''En 2021 el comercio exterior de servicios registró un déficit de US\$1.353m, cifra inferior en US\$ 3.058m (69.3%) respecto a lo
            reportado en 2022.''')
 
st.sidebar.markdown('- [Balanza comercial Servicios](#balanza-servicios)')
 
serv = pd.read_excel('BOP.xlsx',sheet_name='Servicios').loc[10:23,]
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
 
st.markdown('''Los servicios exportados estuvieron compuesto mayoritariamente por ventas de servicios tradicionales (68%),
            seguido de las ventas de servicios moderno (29%) en el que se destacan nuevamente los servicios de
            contact center, informáticay gestión empresarial.''')
 
st.markdown(''' Las compras de servicios registraron las siguientes contribuciones: 55% servicios tradicionale, 32% servicios modernos,
            13% otros servicios.Dentro de los servicios modernos, las compras más relevantes fueron uso de propiedad intelectual y las
            de informática.''')
 
st.warning('''El déficit  se redujo por menores importaciones de servicios de transporte de carga y por el
           incremento de las exportaciones por servicios de viajes gracias a un manor números de viajeros que arribaron al país.''',icon ='💡')
 
#Renta de los factores
 
st.subheader('Renta de los factores'+ ':moneybag:',anchor='renta-factores')
 
st.markdown('''Se estimó un balance deficitario en el rubro de la renta factorial por US\$17.209m. En comparación con 2021, el resultado deficitario
            fue superior en US\$ 8.486m, explicado principalmente por los mayores egresos de las utilidades vinculadas a la IED.''')
 
st.sidebar.markdown('- [Renta de los factores](#renta-factores)')
 
ingresos = pd.read_excel('BOP.xlsx', sheet_name= 'Ingresos').loc[10:23,]
egresos = pd.read_excel('BOP.xlsx',sheet_name='Egresos').loc[10:23,]
 
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
 
st.markdown('''Del total de egresos US\$23.218m, el 50.3% correspondio a la renta estimada para las empresas con
            IED, EL 26.3% a pagos de intereses asociados a créditos externos y el 23.2% a los pagos de dividendos e intereses
            asociados a inversiones extranjeras de cartera.''')
 
st.info(''' Se presentó una reducción en las utilidades de las firmas con IED, que estuvo compensada levemente por el aumento en los pagos
        de intereses externos. La disminución de las utilidades se dio de manera generalizada  y se explica por menores ganancias de las empresas dedicadas
        a  las actividades de minas y cantera, explotación petrolera, establecimientos financieros y servicios empresariales, comercio, restaurantes y
        hoteles. Por su parte,  los mayores pagos de intereses de préstamos externos ocurrió por un aumento generalizado en las
        tasas de intereses internacionales y en menor medida, en mayores saldo de deduda externa''',icon='🔎')
 
st.markdown('''Los ingresos por renta factorial se estimaron en US\$8.813m. El 46% de estos se dieron por rentas asociadas a IEDC, el 22%
            a asociados de activos de reservas internacionales, el 19 % a rendimientos asociados a inversión de cartera y el 12% asociada a los depósitos
            y otros activos en el exterior.''')
 
# Transferencias Corrientes
 
st.subheader('Transferencias Corrientes'+':arrows_counterclockwise:',anchor='transferencias-corrientes')
 
st.markdown('''**Las transferencias corrientes obtuvieron un balance superavitario de US\$12.910m y un incremento anual de 4.9%.**
           Los ingresos por remesas de trabajadores tuvieron un aumento anual del 7.0% y ascendieron a US\$10.91m. Su equivalencia del PIB fue de 2.8%. Del total
           de transferencias se destacaron los envios de USA y España. ''')
 
st.warning('''La tendencia alcista en el número de transferencias se explica tanto en el caso de USA como en el de España en menores tasas de desempleo y en un
           mayor flujo de migrantes colombianos hacia estos paises.''', icon='💡')
 
st.sidebar.markdown('- [Transferencias Corrientes](#transferencias-corrientes)')
 
transferencias = pd.read_excel('BOP.xlsx',sheet_name='Transferencias').loc[10:23,]
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
 
#Cuenta financiera
 
st.header(':blue[Cuenta Financiera]',anchor='cuenta-financiera')
 
st.markdown('''**La cuenta financiera (incluyendo activos de reserva) en 2022, registró entradas netas de capital
            por US\$ 8.880m (2.4% del PIB)**. Cifra inferior en US\$11.587m a lo observado en 2022. Estas entradas se
            explican por ingresos de capital extranjero (US\$22.952m), salidas de capital colombiano (US\$14.929m), pagos por conceptos de derivados
            financieros (US\$2.574m) y aumento de reservas internacionales por transacciones de la balanza de pagos
            (US\$1.718m)''')
 
st.sidebar.markdown('[Cuenta Financiera](#cuenta-financiera)')
 
financiera =pd.read_excel('BOP.xlsx',sheet_name='Cuenta Financiera').loc[10:23,]
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