from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

@app.route('/generate-content', methods=['POST'])
def generate_content():
    """
    Generate dynamic content using OpenAI's GPT model.
    """
    try:
        user_input = request.json.get("user_input", "")
        if not user_input:
            return jsonify({"error": "Invalid input"}), 400
        
        response = openai.Completion.create(
            engine="text-davinci-003",  # Replace with the appropriate model
            prompt=f"Write about {user_input} in detail.",
            max_tokens=100
        )
        
        return jsonify({
            "generated_content": response.choices[0].text.strip()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
