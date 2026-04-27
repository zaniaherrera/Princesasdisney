import streamlit as st
import random

st.set_page_config(
    page_title="Trivia de Princesas Disney",
    page_icon="👑",
    layout="centered"
)

# Banco de preguntas
QUESTIONS = [
    {
        "question": "¿Cómo se llama la princesa de la película 'La Sirenita'?",
        "options": ["Ariel", "Bella", "Jazmín", "Rapunzel"],
        "answer": "Ariel"
    },
    {
        "question": "¿Qué princesa tiene como mejor amigo a un tigre llamado Rajah?",
        "options": ["Mulán", "Jazmín", "Cenicienta", "Blancanieves"],
        "answer": "Jazmín"
    },
    {
        "question": "¿Qué princesa pierde un zapato de cristal?",
        "options": ["Aurora", "Cenicienta", "Tiana", "Moana"],
        "answer": "Cenicienta"
    },
    {
        "question": "¿Qué princesa tiene el cabello mágico y muy largo?",
        "options": ["Rapunzel", "Elsa", "Mérida", "Pocahontas"],
        "answer": "Rapunzel"
    },
    {
        "question": "¿Qué princesa besa a un sapo?",
        "options": ["Tiana", "Bella", "Mulán", "Anna"],
        "answer": "Tiana"
    }
]


def initialize_game():
    """Inicializa o reinicia el juego con opciones aleatorias."""
    randomized_questions = []

    for q in QUESTIONS:
        shuffled_options = q["options"][:]
        random.shuffle(shuffled_options)

        randomized_questions.append({
            "question": q["question"],
            "options": shuffled_options,
            "answer": q["answer"]
        })

    st.session_state.questions = randomized_questions
    st.session_state.submitted = False


if "questions" not in st.session_state:
    initialize_game()

st.title("👑 Trivia de Princesas Disney")
st.markdown("### Responde las 5 preguntas y descubre si eres un verdadero fan Disney ✨")

with st.form("quiz_form"):
    user_answers = []

    for idx, q in enumerate(st.session_state.questions, start=1):
        answer = st.radio(
            f"{idx}. {q['question']}",
            q["options"],
            key=f"q_{idx}"
        )
        user_answers.append(answer)

    submitted = st.form_submit_button("Enviar respuestas")

if submitted:
    score = 0

    st.divider()
    st.subheader("📋 Resultados")

    for i, q in enumerate(st.session_state.questions):
        correct = user_answers[i] == q["answer"]

        if correct:
            score += 1
            st.success(f"Pregunta {i+1}: ¡Correcto! ✅")
        else:
            st.error(
                f"Pregunta {i+1}: Incorrecto ❌ | Respuesta correcta: {q['answer']}"
            )

    st.markdown(f"## Puntaje final: **{score}/5**")

    if score == 5:
        st.balloons()
        st.success("🎉 ¡FELICIDADES! ¡Acertaste todas las preguntas! Eres realeza Disney 👑✨")
        st.markdown("### 🌟 Premio especial desbloqueado 🌟")
        st.markdown("## 🏆 ¡Princesa experta certificada! 🏆")
    elif score >= 3:
        st.info("✨ ¡Muy bien! Conoces bastante sobre las princesas Disney.")
    else:
        st.warning("💫 Sigue practicando, aún puedes convertirte en experto Disney.")

    if st.button("🔄 Jugar nuevamente"):
        initialize_game()
        st.rerun()

st.markdown("---")
st.caption("Aplicativo creado en Streamlit | Trivia Disney 👑")
