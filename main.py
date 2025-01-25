from openai_integration.openai_api import get_openai_response

def main():
    prompt = "What are the latest trends in AI?"
    response = get_openai_response(prompt)
    print(f"OpenAI Response: {response}")

if __name__ == "__main__":
    main()
