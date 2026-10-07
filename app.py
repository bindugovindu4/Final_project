import streamlit as st
import ollama
from rag_engine import (
    ask_ai,
    explain_topic,
    generate_quiz,
    generate_flashcards,
    create_summary,
    create_study_plan)
st.set_page_config(
    page_title="Intelligent Student Study Assistant",
    page_icon="🎓",
    layout="wide")
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;}
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: gray;
        margin-bottom: 30px;}
    .card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ddd;
        margin-bottom: 15px;}
    </style>
    """,
    unsafe_allow_html=True)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
st.markdown(
    '<div class="title">🎓 Intelligent Student Study Assistant</div>',
    unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-powered learning assistant for students</div>',
    unsafe_allow_html=True)
with st.sidebar:
    st.header("📚 Study Assistant")
    selected_page = st.radio(
        "Select Feature",
        [
            "🏠 Home",
            "💬 Ask AI",
            "📖 Explain Topic",
            "📝 Quiz Generator",
            "🧠 Flashcards",
            "📋 Study Summary",
            "📅 Study Planner",
            "📊 My Progress",
            "ℹ️ About"])
    st.divider()
    st.info(
        "Powered by Ollama + llama 3.2")
if selected_page == "🏠 Home":
    st.header("Welcome 👋")
    st.write(
        "Your personal AI-powered study assistant.")
    st.write(
        "You don't need to upload any notes or study materials. "
        "Simply enter a topic or ask a question.")
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            ### 💬 Ask AI
            Ask academic questions and get
            simple explanations.
            """)
    with col2:
        st.markdown(
            """
            ### 📝 Generate Quiz

            Generate MCQ questions for
            exam preparation.
            """)
    with col3:
        st.markdown(
            """
            ### 🧠 Flashcards

            Create flashcards for
            quick revision.
            """)
    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown(
            """
            ### 📖 Explain Topics
            Get detailed explanations
            of difficult concepts.
            """)
    with col5:
        st.markdown(
            """
            ### 📋 Summaries
            Generate quick revision
            notes automatically.
            """)
    with col6:
        st.markdown(
            """
            ### 📅 Study Planner
            Create personalized study
            schedules.
            """)
elif selected_page == "💬 Ask AI":
    st.header("💬 Ask AI")
    st.write(
        "Ask any academic or study-related question.")
    for message in st.session_state.chat_history:
        with st.chat_message(
            message["role"]):
            st.markdown(
                message["content"])
    question = st.chat_input(
        "Ask your question...")
    if question:
        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question})
        with st.chat_message("user"):
            st.write(question)
        with st.chat_message("assistant"):
            with st.spinner(
                "Thinking..."):
                answer = ask_ai(
                    question)
            st.markdown(answer)
        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": answer})
elif selected_page == "📖 Explain Topic":
    st.header("📖 Explain Any Topic")
    topic = st.text_input(
        "Enter topic",
        placeholder="Example: Normalization in DBMS")
    if st.button(
        "Explain Topic 🚀"):
        if topic.strip() == "":
            st.warning(
                "Please enter a topic.")
        else:
            with st.spinner(
                "Preparing explanation..."):
                answer = explain_topic(
                    topic)
            st.markdown(answer)
elif selected_page == "📝 Quiz Generator":
    st.header("📝 AI Quiz Generator")
    topic = st.text_input(
        "Enter subject/topic",
        placeholder="Example: Operating Systems")
    number = st.slider(
        "Number of questions",
        5,
        20,
        10)
    if st.button(
        "Generate Quiz 📝"):
        if topic.strip() == "":
            st.warning(
                "Please enter a topic.")
        else:
            with st.spinner(
                "Generating questions..."):
                quiz = generate_quiz(
                    topic,
                    number)
            st.markdown(quiz)
elif selected_page == "🧠 Flashcards":
    st.header("🧠 AI Flashcards")
    topic = st.text_input(
        "Enter topic",
        placeholder="Example: Computer Networks")
    if st.button(
        "Generate Flashcards 🧠"):
        if topic.strip() == "":
            st.warning(
                "Please enter a topic.")
        else:
            with st.spinner(
                "Creating flashcards..."):
                cards = generate_flashcards(
                    topic)
            st.markdown(cards)
elif selected_page == "📋 Study Summary":
    st.header("📋 Generate Study Summary")
    topic = st.text_input(
        "Enter topic",
        placeholder="Example: Database Management System")
    if st.button(
        "Generate Summary 📋"):
        if topic.strip() == "":
            st.warning(
                "Please enter a topic.")
        else:
            with st.spinner(
                "Creating summary..."):
                summary = create_summary(
                    topic)
            st.markdown(summary)
elif selected_page == "📅 Study Planner":
    st.header("📅 Personalized Study Planner")
    subject = st.text_input(
        "Enter subject",
        placeholder="Example: Python Programming")
    days = st.slider(
        "Number of study days",
        1,
        30,
        7)
    if st.button(
        "Create Study Plan 📅"):
        if subject.strip() == "":
            st.warning(
                "Please enter a subject.")
        else:
            with st.spinner(
                "Creating your study plan..."):
                plan = create_study_plan(
                    subject,
                    days)
            st.markdown(plan)
elif selected_page == "📊 My Progress":
    st.header("📊 My Study Progress")
    questions = len(
        st.session_state.chat_history)
    user_questions = len([
            x
            for x in st.session_state.chat_history
            if x["role"] == "user"])
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Questions Asked",
            user_questions)
    with col2:
        st.metric(
            "AI Responses",
            user_questions)
    with col3:
        st.metric(
            "Study Sessions",
            1 if user_questions > 0 else 0)
    st.progress(
        min(user_questions / 10, 1.0))
    st.write(
        "Your progress is based on your current session.")
elif selected_page == "ℹ️ About":
    st.header("ℹ️ About Project")
    st.markdown(
        """
        # 🎓 Intelligent Student Study Assistant
        This is an AI-powered student learning platform.
        ## Features
        ✅ Ask AI academic questions
        ✅ Explain difficult topics
        ✅ Generate MCQ quizzes
        ✅ Generate flashcards
        ✅ Generate study summaries
        ✅ Create personalized study plans
        ✅ Track basic study progress
        ## Technologies Used
        **Frontend**
        - Streamlit
        **Backend**
        - Python
        **AI**
        - Ollama
        - llama 3.2
        ## Project Objective
        The objective of this project is to provide students
        with an intelligent virtual study assistant that can
        help them understand concepts, prepare for exams,
        practice questions, and organize their study schedule.
        """)