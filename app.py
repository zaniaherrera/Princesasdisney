import streamlit as st
import random

st.set_page_config(page_title="Trivia de Farándula Peruana", page_icon="🎤", layout="centered")

# -----------------------------
# Banco de preguntas
# -----------------------------
QUESTIONS = [
    {
        "question": "¿Qué famosa frase hizo viral Magaly Medina en sus programas de espectáculos?",
        "options": ["Ampay", "No me importa", "Eso fue fuerte", "Qué vergüenza"],
        "answer": "Ampay",
    },
    {
        "question": "¿Quién es conocida como la 'Urraca' de la televisión peruana?",
        "options": ["Magaly Medina", "Gisela Valcárcel", "Tula Rodríguez", "Janet Barboza"],
        "answer": "Magaly Medina",
    },
    {
        "question": "¿Qué conductor hizo famosa la frase 'Mami, qué rica estás'?",
        "options": ["Carlos Cacho", "Raúl Romero", "Andrés Hurtado", "Renzo Schuller"],
        "answer": "Carlos Cacho",
    },
    {
        "question": "¿Qué personaje televisivo es conocido como 'Chibolín'?",
        "options": ["Andrés Hurtado", "Raúl Romero", "Adolfo Aguilar", "Mathías Brivio"],
        "answer": "Andrés Hurtado",
    },
    {
        "question": "¿Qué modelo fue protagonista del famoso caso del 'Loco Vargas'?",
        "options": ["Tilsa Lozano", "Milett Figueroa", "Sheyla Rojas", "Melissa Loza"],
        "answer": "Tilsa Lozano",
    },
    {
        "question": "¿Qué conductor lideró el programa juvenil 'Habacilar'?",
        "options": ["Raúl Romero", "Bruno Pinasco", "Adolfo Aguilar", "Gian Piero Díaz"],
        "answer": "Raúl Romero",
    },
    {
        "question": "¿Qué exvedette fue famosa por llevar su número al Congreso tatuado?",
        "options": ["Susy Díaz", "Monique Pardo", "Gisela Valcárcel", "Mariella Zanetti"],
        "answer": "Susy Díaz",
    },
    {
        "question": "¿Qué presentadora era conocida como 'La Señito'?",
        "options": ["Gisela Valcárcel", "Mónica Zevallos", "Karen Schwarz", "Jessica Newton"],
        "answer": "Gisela Valcárcel",
    },
    {
        "question": "¿Qué personaje infantil hizo famosa Yola Polastri?",
        "options": ["La tía Yola", "La reina mágica", "La muñeca feliz", "La chica dulce"],
        "answer": "La tía Yola",
    },
    {
        "question": "¿Qué frase se volvió icónica de Laura Bozzo?",
        "options": ["¡Que pase el desgraciado!", "¡Fuera todos!", "¡No puede ser!", "¡Silencio!"],
        "answer": "¡Que pase el desgraciado!",
    },
]


# -----------------------------
# Estado inicial
# -----------------------------
if "started" not in st.session_state:
    st.session_state.started = False

if "question_order" not in st.session_state:
    st.session_state.question_order = random.sample(QUESTIONS, len(QUESTIONS))

if "shuffled_options" not in st.session_state:
    shuffled = []
    for q in st.session_state.question_order:
        opts = q["options"][:]
        random.shuffle(opts)
        shuffled.append(opts)
    st.session_state.shuffled_options = shuffled

if "submitted" not in st.session_state:
    st.session_state.submitted = False


# -----------------------------
# Función reiniciar
# -----------------------------
def restart_game():
    st.session_state.question_order = random.sample(QUESTIONS, len(QUESTIONS))

    shuffled = []
    for q in st.session_state.question_order:
        opts = q["options"][:]
        random.shuffle(opts)
        shuffled.append(opts)

    st.session_state.shuffled_options = shuffled
    st.session_state.submitted = False

    # limpiar respuestas previas
    for i in range(len(QUESTIONS)):
        key = f"q_{i}"
        if key in st.session_state:
            del st.session_state[key]


# -----------------------------
# UI principal
# -----------------------------
st.title("🎤 Trivia de Farándula Peruana")
st.markdown("### ¿Cuánto sabes de los momentos más icónicos de la farándula en Perú?")
st.write("Responde las 10 preguntas. Las alternativas cambian de orden en cada partida 👀")

if st.button("🔄 Nueva partida"):
    restart_game()
    st.rerun()

st.divider()

for i, q in enumerate(st.session_state.question_order):
    st.subheader(f"Pregunta {i + 1}")
    st.radio(
        q["question"],
        st.session_state.shuffled_options[i],
        key=f"q_{i}",
        index=None,
    )
    st.write("")


if st.button("✅ Finalizar Trivia"):
    st.session_state.submitted = True


if st.session_state.submitted:
    score = 0

    st.divider()
    st.header("📊 Resultados")

    for i, q in enumerate(st.session_state.question_order):
        user_answer = st.session_state.get(f"q_{i}")
        correct_answer = q["answer"]

        if user_answer == correct_answer:
            score += 1
            st.success(f"Pregunta {i + 1}: Correcto ✅")
        else:
            st.error(
                f"Pregunta {i + 1}: Incorrecto ❌ | Respuesta correcta: {correct_answer}"
            )

    st.markdown(f"## Puntaje final: **{score}/10**")

    if score == 10:
        st.balloons()
        st.snow()
        st.success("🎉 ¡PERFECTO! ¡Acertaste todo! Eres una leyenda de la farándula peruana 👑")
        st.markdown(
            """
            <div style='text-align:center; font-size:28px; padding:20px;'>
                ✨🏆 FAMA TOTAL 🏆✨<br>
                ¡Nivel experto desbloqueado!
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif score >= 7:
        st.info("👏 Muy bien, casi eres reportero de espectáculos.")
    elif score >= 4:
        st.warning("😄 Vas bien, pero necesitas más chismecito televisivo.")
    else:
        st.warning("📺 Hora de ver más farándula peruana y volver a intentarlo.")
