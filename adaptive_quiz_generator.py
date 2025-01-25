def generate_quiz(topic):
    """
    Generate a personalized quiz based on the topic.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Create a quiz with 5 multiple-choice questions on {topic}.",
        max_tokens=200
    )
    return response.choices[0].text.strip()

topic = "Machine Learning"
quiz = generate_quiz(topic)
print("Generated Quiz:\n", quiz)
