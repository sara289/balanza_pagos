import streamlit as st

st.sidebar.header('Análisis Balanza de Pagos'+'⚖️')
st.sidebar.image('logo banrep.png')

st.title('¿Qué es la balanza de pagos? :scales:')
st.markdown('''Es una herramienta comúnmente utilizada por los analistas económicos para examinar los ingresos y gastos de un país con el resto del mundo.
En esta se registran tanto los flujos de bienes y servicios como de capitales. La balanza está compuesta por dos cuentas: la **cuenta corriente** y la **cuenta financiera** ''')


st.header('📌'+'Cuenta Corriente', anchor='cuenta-corriente')


st.markdown('''Esta cuenta contabiliza el intercambio de bienes, servicios y rentas de un país con el resto del mundo y se obtiene una vez se suman los siguientes componentes:
- **Bienes y servicios**: Es la diferencia entre las exportaciones y las importaciones asociadas al comercio exterior de bienes (carbón, flores, medicamentos, etc) y servicios
             (transporte, turismo, seguros, etc).
- **Ingreso Primario**: Se le conoce también como **_renta de los factores_**, es la diferencia entre los ingresos y los egresos asociados principalmente a rendimientos y utilidades
            de la inversión directa y de cartera, así como los intereses generados por préstamos.
- **Ingreso Secundario**: Es la resta entre los ingresos asociados a transferencias corrientes, que en su mayoría corresponden a remesas de los trabajadores''')


st.sidebar.markdown("[Cuenta Corriente](#cuenta-corriente)")


st.warning(''' **Importante: :bulb:**
Una vez agregados todos los componentes si los egresos superan a los ingresos se dice que hay un **déficit** en cuenta corriente. El caso contrario se conoce como **superávit** corriente''')  


st.header("📌"+ "Cuenta Financiera" ,anchor='cuenta-financiera')
 
st.markdown('''Refleja si un país está siendo prestamista para el resto del mundo o si por el contrario el resto del mundo es prestamista del país local. Si una economía registra
            déficit corriente, esta cuenta contabiliza cuáles fueron las fuentes de financiamiento externo, en caso contrario (superávit) permite visualizar la capacidad de prestar
            o invertir recursos en el resto de los países. Obtiene al agregar los siguientes componentes:
- **Inversión Directa:** Diferencia entre los flujos inversión directa en el exterior y los flujos de inversión extranjera directa (IED)
- **Inversión de Cartera:** En este componente se registran los flujos de inversiones que se realizaron en bonos o acciones tanto de extranjeros en el país local, como de nacionales
            en otros países. Es conocida también como **_inversión de portafolio_**.
- **Otra inversión:** En este componente se agregan inversiones diferentes a las anteriormente mencionadas. El saldo se obtiene al restar los flujos de inversiones en el exterior y en el país.  
- **Variación en las reservas internacionales:** Es la resta entre los ingresos por concepto de transacciones asociadas a los activos de reserva (rendimiento portafolio, compra de divisas, entre
            otros) y por concepto de egresos (venta de divisas, entre otros).
''')
 
st.sidebar.markdown("[Cuenta Financiera](#cuenta-financiera)")


st.header('📌'+'Errores y Omisiones',anchor='errores-y-omisiones')


st.markdown('''Dada la complejidad para calcular con exactitud la diferencia entre los ingresos y los gastos de un país, en la cuenta de errores y omisiones se registran todas aquellas
            transacciones que por su naturaleza diversa y compleja no se contabilizan previamente. Esta cuenta ayuda a balancear los ingresos y los gastos, a la vez que solventa discrepancias
            posibles en otras cuentas.''')


st.sidebar.markdown("[Errores y Omisiones](#errores-y-omisiones)")

st.header('❗¿Por qué es importante la balanza de pagos?',anchor='importancia')

st.sidebar.markdown("[Importancia](#importancia)")

st.markdown('''✔ Es un indicador de la salud económica de un país. Refleja el nivel de comercio internacional
            y los flujos de capital, suministrando una visión integral de su situación económica
            y su necesidad de financiación.

✔ Proporciona información esencial para la formulación de política monetaria. Permite identificar desequilibrios
            económicos y adoptar medidas de ajuste.
                              
✔  Influencia los tipos de cambio e incide sobre los niveles de inflación.
            
✔  Mide la competitividad de un país y su capacidad para generar ingresos a través del comercio internacional.
            
✔  Permite identificar relaciones de interdependencia bien sea de importaciones o de commodities sobre las exportaciones. ''')