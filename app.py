import streamlit as st
import random

st.set_page_config(page_title="Trivia de Farándula Peruana", page_icon="🎤", layout="centered")

# -----------------------------
# Banco de preguntas
# -----------------------------
QUESTIONS = [
    {
        "question": "¿Qué frase icónica popularizó Laura Bozzo en televisión?",
        "options": ["¡Que pase el desgraciado!", "¡Fuera de aquí!", "¡No me grites!", "¡Esto es el colmo!"],
        "answer": "¡Que pase el desgraciado!",
    },
    {
        "question": "¿Qué cantante peruana es conocida como 'La Tigresa del Oriente'?",
        "options": ["Judith Bustos", "Gisela Valcárcel", "Yola Polastri", "Monique Pardo"],
        "answer": "Judith Bustos",
    },
    {
        "question": "¿Quién fue conocida como la 'Señito' de la televisión peruana?",
        "options": ["Gisela Valcárcel", "Magaly Medina", "Maju Mantilla", "Rebeca Escribens"],
        "answer": "Gisela Valcárcel",
    },
    {
        "question": "¿Qué conductora es famosa por su programa de espectáculos y los 'ampays'?",
        "options": ["Magaly Medina", "Johanna San Miguel", "Tula Rodríguez", "Sheyla Rojas"],
        "answer": "Magaly Medina",
    },
    {
        "question": "¿Qué personaje infantil fue interpretado por Yola Polastri?",
        "options": ["La chica de la tele", "La reina de los niños", "La tía Yola", "La muñeca feliz"],
        "answer": "La tía Yola",
    },
    {
        "question": "¿Qué cantante peruano hizo famosa la frase 'No se llama amor'?",
        "options": ["Pedro Suárez-Vértiz", "Gian Marco", "Christian Meier", "Raúl Romero"],
        "answer": "Pedro Suárez-Vértiz",
    },
    {
        "question": "¿Qué exfutbolista y figura mediática estuvo casado con Melissa Klug?",
        "options": ["Jefferson Farfán", "Paolo Guerrero", "Roberto Martínez", "Juan Manuel Vargas"],
        "answer": "Jefferson Farfán",
    },
    {
        "question": "¿Qué conductor hizo famosa la frase 'Habacilar'?",
        "options": ["Raúl Romero", "Adolfo Aguilar", "Bruno Pinasco", "Carlos Galdós"],
        "answer": "Raúl Romero",
    },
    {
        "question": "¿Qué vedette fue protagonista de múltiples escándalos mediáticos en los 2000?",
        "options": ["Susy Díaz", "Maricielo Effio", "Tilsa Lozano", "Milett Figueroa"],
        "answer": "Susy Díaz",
    },
    {
        "question": "¿Qué frase se asocia popularmente con Susy Díaz?",
        "options": ["Vive la vida", "Me amo y no me importa", "Lo que pasa, pasa", "Todo por amor"],
        "answer": "Me amo y no me importa",
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

st.markdown("---")
st.caption("Aplicativo creado en Streamlit | Trivia Disney 👑")
