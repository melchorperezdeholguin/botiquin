Aquí tienes una versión mejorada y "arreglada" del código. No tenía errores de sintaxis, pero le he añadido:

1. **Configuración de página** (`st.set_page_config`) para que se vea bien en navegador.
2. **CSS ligero** para darle un estilo más limpio y espiritual.
3. **Estado de sesión** (`st.session_state`) para que los globos (`st.balloons()`) no se repitan en cada recarga.
4. **Texto del versículo y oración corta** para cada emoción (no solo la referencia).
5. **Botón "Limpiar"** para empezar de nuevo.
6. **Aviso importante**: recuerda que esta herramienta acompaña espiritualmente, pero no reemplaza ayuda profesional de salud mental (psicología/medicina), tal como sugieren las guías bíblicas consultadas.

```python
import streamlit as st

# ======================
# Configuración de la página
# ======================
st.set_page_config(
    page_title="🕊️ Botiquín Espiritual",
    page_icon="🕊️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ======================
# Estilos personalizados (CSS)
# ======================
st.markdown("""
    <style>
    .main {
        padding: 2rem 1rem;
    }
    .card {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-left: 6px solid #4CAF50;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .ref {
        font-weight: bold;
        color: #2e7d32;
        font-size: 1.1rem;
    }
    .verse-text {
        font-style: italic;
        color: #444;
        margin: 0.5rem 0;
    }
    .oracion {
        margin-top: 0.75rem;
        font-size: 0.95rem;
        color: #555;
    }
    .disclaimer {
        font-size: 0.8rem;
        color: #888;
        margin-top: 2.5rem;
        border-top: 1px solid #eee;
        padding-top: 1rem;
        text-align: center;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# ======================
# Título y subtítulo
# ======================
st.title("🕊️ Botiquín Espiritual")
st.subheader("¿Cómo te sientes hoy? La Palabra de Dios tiene una respuesta.")

# ======================
# Diccionario de emociones → versículo, texto y oración
# ======================
versiculos = {
    "😠 Molesto / Enojado": {
        "ref": "Juan 14:27",
        "texto": "»Les dejo la paz, les doy mi paz; pero no se la doy a ustedes como la da el mundo. No se angustien ni tengan miedo.«",
        "oracion": "Señor, entrego mi enojo en Tus manos y pide que Tu paz calme mi corazón."
    },
    "😔 Débil / Cansado": {
        "ref": "Isaías 40:31",
        "texto": "«Mas los que esperan en Jehová tendrán nuevas fuerzas; levantarán las alas como águilas; correrán, y no se cansarán; caminarán, y no se fatigarán.»",
        "oracion": "Dios, renueva mis fuerzas cuando me siento agotado y dame ánimo para seguir."
    },
    "😞 Solitario": {
        "ref": "Salmos 23",
        "texto": "«Jehová es mi pastor; nada me faltará. En lugares de delicados pastos me hará reposar; junto a aguas de descanso me pastoreará.»",
        "oracion": "Padre, gracias por caminar a mi lado aunque pase por valles oscuros; no estoy solo."
    },
    "😥 He pecado": {
        "ref": "Salmos 51",
        "texto": "«Misericordia de mí, oh Dios, según Tu misericordia; conforme a la multitud de Tus compasiones borra mis transgresiones.»",
        "oracion": "Señor, arrepiénteme, límpiame y restaura el gozo de Tu salvación en mí."
    },
    "😰 Preocupado / Ansioso": {
        "ref": "Filipenses 4:6-7",
        "texto": "«No se angustien por nada; más bien, oren; pídanle a Dios en toda ocasión y denle gracias. Y la paz de Dios, esa paz que nadie puede comprender, cuidará sus corazones y pensamientos en Cristo.»",
        "oracion": "Dios, entrego mis preocupaciones en oración y recibo Tu paz que guarda mi corazón."
    },
    "😢 Infeliz": {
        "ref": "Colosenses 3:12-17",
        "texto": "«Revístanse, entonces, como escogidos de Dios, santos y amados, de entrañas de misericordia, bondad, humildad, mansedumbre, paciencia...»",
        "oracion": "Señor, restaura mi gozo y enséñame a vivir agradecido en todas las circunstancias."
    },
    "⚠️ En peligro": {
        "ref": "Salmos 91",
        "texto": "«El que habita al abrigo del Altísimo morará bajo la sombra del Omnipotente. Diré de Jehová: Él es mi refugio y mi fortaleza, mi Dios, en quien confío.»",
        "oracion": "Padre, Tú eres mi refugio y mi escudo; confío en Tu protección sobre mi vida."
    },
    "😭 Deprimido": {
        "ref": "Salmos 27",
        "texto": "«Jehová es mi luz y mi salvación; ¿a quién temeré? Jehová es la fortaleza de mi vida; ¿de quién he de espantarme?»",
        "oracion": "Dios, acerca Tu luz a mi oscuridad y sostén mi espíritu cuando me siento abatido."
    },
    "🤔 Falta de fe": {
        "ref": "Éxodo 14",
        "texto": "«Jehová peleará por ustedes, y ustedes estarán quietos.»",
        "oracion": "Señor, aumenta mi fe y enséñame a confiar en Ti, incluso cuando no veo el camino."
    },
    "💪 Necesito valor": {
        "ref": "Josué 1:9",
        "texto": "«¿No te he mandado? Esfuérzate y sé valiente. No temas ni desmayes, que yo soy el Señor tu Dios, y estaré contigo por dondequiera que vayas.»",
        "oracion": "Dios, dame valor para avanzar sabiendo que Tú estás conmigo en cada paso."
    },
    "🧭 Necesito dirección": {
        "ref": "Salmos 73:21-26",
        "texto": "«Mas yo estoy siempre contigo; Tú me sostienes de mi mano derecha. Con Tu consejo me guiarás, y después me recibirás en gloria.»",
        "oracion": "Señor, guía mis pasos y sé mi dirección cuando no sé qué decidir."
    },
    "🕊️ Buscando paz": {
        "ref": "Mateo 11:28-30",
        "texto": "«Vengan a mí todos ustedes, los agotados de tanto trabajar, que yo los haré descansar. Lleven mi yugo sobre ustedes, y aprendan de mí, que soy manso y humilde de corazón, y hallarán descanso para su alma.»",
        "oracion": "Jesús, descanso en Ti y entrego mi carga; hallo paz para mi alma en Ti."
    },
}

# ======================
# Selector y botones
# ======================
sentimiento = st.selectbox(
    "Selecciona tu estado de ánimo:",
    options=list(versiculos.keys()),
    index=None,
    placeholder="Elige cómo te sientes..."
)

col1, col2 = st.columns([1, 1])
with col1:
    obtener = st.button("Obtener Versículo", type="primary", use_container_width=True)
with col2:
    limpiar = st.button("Limpiar", use_container_width=True)

# Botón limpiar: borra el estado y recarga
if limpiar:
    for key in ["mostrar", "animacion"]:
        st.session_state.pop(key, None)
    st.rerun()

# Botón obtener: guarda selección en sesión
if obtener and sentimiento:
    st.session_state["mostrar"] = sentimiento
    st.session_state["animacion"] = True

# Mostrar resultado si hay selección guardada
if "mostrar" in st.session_state:
    sentimiento_actual = st.session_state["mostrar"]
    data = versiculos[sentimiento_actual]

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.success(f"**{sentimiento_actual}**")
    st.markdown(f'<div class="ref">{data["ref"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<p class="verse-text">{data["texto"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="oracion"><strong>Oración corta:</strong> {data["oracion"]}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.info("Recuerda que Dios siempre está contigo. ¡Ánimo! 🙏")

    # Animación solo una vez por clic
    if st.session_state.get("animacion"):
        st.balloons()
        st.session_state["animacion"] = False

# ======================
# Descargo de responsabilidad
# ======================
st.markdown("""
<div class="disclaimer">
⚠️ <b>Aviso importante:</b> Este botiquín espiritual es una herramienta de acompañamiento y oración. No reemplaza el consejo médico, psicológico ni psiquiátrico. Si sientes tristeza persistente, ansiedad abrumadora, pensamientos de autolesión o estás en crisis, busca ayuda profesional hoy mismo y habla con una persona de confianza. Pedir ayuda es un acto de cuidado y valentía.
</div>
""", unsafe_allow_html=True)
```

### Principales cambios
| Cambio | ¿Por qué? |
|--------|-----------|
| `index=None` y `placeholder` | El usuario debe elegir activamente una emoción en lugar de que se preselecione la primera. |
| `st.session_state` | Evita que `st.balloons()` se dispare en cada interacción de Streamlit (recarga). |
| Texto del versículo + oración | No solo das la referencia, sino un fragmento del pasaje y una oración breve para aplicar. |
| CSS `.card` | Destaca visualmente el resultado y separa el contenido del resto de la app. |
| Botón "Limpiar" | Permite resetear la selección sin recargar la página manualmente. |
| Disclaimer | Nota ética importante: el apoyo espiritual no sustituye la ayuda profesional de salud mental. |

Puedes copiar y pegar este código directamente en tu archivo `.py` y ejecutarlo con `streamlit run nombre_archivo.py`.