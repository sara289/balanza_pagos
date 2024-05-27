import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
st.sidebar.header('Análisis Balanza de Pagos'+'⚖️')
st.header('Algunas conclusiones 📊')
st.sidebar.image('logo banrep.png')
 
st.divider()
 
st.markdown('''➡️ El déficit para 2014 y 2015 se profundizo producto de una caída de los precios del petróleo que redujo
            considerablemente los niveles de exportación.''')
 
st.info('''Según el portal [**El economista**](https://www.eleconomista.es/materias-primas/noticias/6463592/02/15/Los-verdaderos-responsables-del-desplome-del-petroleo-durante-2014-el-fracking-no-esta-solo.html#:~:text=El%20precio%20del%20petr%C3%B3leo%20se,la%20ca%C3%ADda%20alcanza%20el%2060%25.)
         los precios del petróleo se desplomaron en 2014 alrededor de un 47% producto de un exceso de oferta por el auge del *fracking*
         y una intensa competencia entre **USA, Irak, Cánada, Brasil e Irán.**''',icon='🔎')
 
st.markdown('''La caída global en los precios de este commoditie no solo profundizó el déficit de la balanza comecial, si no que también
            lo hizo con la cuenta de renta factorial.
           
Con esto se puede concluir que en efecto **la economía colombiana depende altamente de sector minero-energético**, ya que su canasta exportadora
reside principalmente sobre el petróleo y carbón. Adicionalmente, es importante señalar que existe una gran concentración de capitales con destino
a inversión en este sector, lo que aumenta la vulnerabilidad externa ante volatilidad en precios.''')
 
st.warning('''Considerando lo anterior, los recientes anuncios del presidente Gustavo Petro sobre la decisión de [**no firmar más contratos de exploración de
           pozos petróleros**](https://www.infobae.com/colombia/2023/12/01/colombia-ya-dejo-de-firmar-contratos-de-exploracion-de-carbon-petroleo-y-gas-gustavo-petro-reitera-el-tema-en-la-cop28/)
           y la creciente conciencia ambiental de las grandes naciones sobre el uso de combustibles fósiles, Colombia debe avanzar rápidamente en la
           diversificación de su canasta exportadora para evitar escenarios profundos de déficit que puedan conducir a situaciones de insolvencia. ''', icon='⚠️')
st.divider()
 
st.markdown('''➡️ Como se pudo observar en el análisis, para 2023 el déficit en la balanza de servicios se redujo ampliamente gracias a una destaca participación
            de las exportaciones de servicios de viajes.''')
 
st.warning('''Dado lo anterior, el gobierno colombiano en trabajo mancomunado con organizaciones como COTELCO (Asociación Hotelera y Turística de Colombia)
           deben continuar creando estrategias que fomenten en turismo y permitan posesionar a Colombia como uno de los principales destinos turisiticos del mundo.
           Esto permitiría reducir el déficit en cuenta corriente e impulsar el desarrollo.''', icon='⚠️')
st.divider()
 
st.markdown('''➡️ El ingreso secundario en el período de análisis obtuvo siempre un balance superávitario, principalmente por un número signficativo
            de remesas enviadas por migrantes colombianos.''')
 
remesas = pd.read_excel('BOP.xlsx',sheet_name='Remesas').loc[6:,]
 
remesas.columns = ['Ingresos por remesas','Año']

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(8, 4))
sns.barplot(x='Año',y='Ingresos por remesas',data=remesas, color='darkgoldenrod')
 
plt.title('Ingresos por remesas', weight='bold')
plt.xlabel('Años')
plt.ylabel('Millones USD')
plt.xticks(rotation=90)
 
st.pyplot()
 
st.info(''' La gráfica muestra un comportamiento ascendente con leves reducciones en 2009 y 2020.
        Dado la gran cantidad de colombianos residentes en Estados Unidos, la caída considerable de este rubro en 2009,
        se puede explicar por la crisis financiera en 2008 que tensionó la economía mundial y en especial la estadounidense.
 
Luego, para 2020 se presenta una disminución no muy pronunciada en el número de divisas recibidas, este comportamiento
        evidentemente se dió por las medidas de confinamiento impuestas por los gobiernos para combatir el covid-19.
 
De acuerdo con los postulados de [Lucas & Stark (1985)](https://www.jstor.org/stable/1833062) y a la luz de un análisis netamente descriptivo se puede decir que
           las remesas recibidas en Colombia se mueven por motivaciones altruistas en lugar de interés propio. ''', icon='💡')
st.divider()
 
st.markdown(''' ➡️ La profundización del déficit en cuenta corriente para 2021 se dió por una gran ampliación del desbalance en la cuenta de bienes. Este
            comportamiento se explica evidentemente por la compra de las vacunas anticovid por parte del gobierno. Las diferentes medidas adoptadas por el gobierno
            para salvaguardar la vida y proteger el ingreso de las familias colombianas excedieron la capacidad del gobierno y aumentaron los niveles de endeudamiento.
           
En general, Colombia se posesiona como una nación deudarora frente al resto del mundo y debe organizar sus finanzas rigurosamente para evitar escenarios de insolvencia. ''')
