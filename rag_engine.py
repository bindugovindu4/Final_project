import ollama
MODEL = "llama3.2:3b"
def generate_response(prompt):
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt}])
        return response["message"]["content"]
    except Exception as e:
        return f"""
Error connecting to Ollama.
Please make sure Ollama is running and the model
'{MODEL}' is installed.
Error:
{str(e)}
"""
def ask_ai(question):
    prompt = f"""
You are an intelligent student study assistant.
Answer the student's question clearly and accurately.
Student Question:
{question}
Instructions:
- Explain in simple language.
- Give examples where useful.
- Use headings and bullet points.
- If the topic is technical, explain step-by-step.
- Keep the answer suitable for a college student.
"""
    return generate_response(prompt)
def explain_topic(topic):
    prompt = f"""
Explain the following academic topic to all students.
Topic:
{topic}
Give the answer using this structure:
1. Definition
2. Main concepts
3. How it works
4. Example
5. Advantages
6. Disadvantages
7. Important points for exams
8. Short summary
Use simple language.
"""
    return generate_response(prompt)
def generate_quiz(topic, number):
    prompt = f"""
Create {number} multiple-choice questions for a college student.
Topic:
{topic}
For each question provide:
Question:
A)
B)
C)
D)
Correct Answer:
Explanation:
Make the questions educational and suitable for exam preparation.
"""
    return generate_response(prompt)
def generate_flashcards(topic):

    prompt = f"""
Create 10 useful study flashcards for the following topic:
{topic}
Use this format:
FLASHCARD 1
Question:
Answer:
FLASHCARD 2
Question:
Answer:
Continue until FLASHCARD 10.
Keep answers short and easy to remember.
"""
    return generate_response(prompt)
def create_summary(topic):
    prompt = f"""
Create a clear study summary for:
{topic}
Include:
- Introduction
- Important concepts
- Key definitions
- Important formulas if applicable
- Examples
- Advantages
- Disadvantages
- Exam points
- Quick revision notes
Make it concise and easy to study.
"""
    return generate_response(prompt)
def create_study_plan(subject, days):
    prompt = f"""
Create a {days}-day study plan for the subject:
{subject}
For each day provide:
Day number:
Topics:
Study time:
Practice activity:
Revision activity:
Make the plan realistic for a college student.
"""
    return generate_response(prompt)