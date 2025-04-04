import openai
def generate_technical_questions(tech_stack):
    prompt = f"""
    You are an AI recruiter for a technology company. Generate 3-5 technical interview questions for each skill in the following tech stack:
    {', '.join(tech_stack)}
    
    Example:
    - Python: What are Python decorators? Explain with an example.
    - Django: How does Django handle database migrations?
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]
