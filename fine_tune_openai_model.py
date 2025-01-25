import openai

openai.api_key = "sk-5k98H4I4kx3m234Lf1VfJ8wETc5RrTu5KlW"

# Example fine-tuning
fine_tune_response = openai.FineTune.create(
    training_file="p0ll0b",  # Replace with uploaded file ID
    model="gpt-o1:gpt-aikoinfinity"
)
print("Fine-tune ID:", fine_tune_response['proj_Kj0ipvvIXekQYDDOLpQpOtea'])

# Monitoring fine-tune status
status = openai.FineTune.retrieve(id=fine_tune_response['proj_Kj0ipvvIXekQYDDOLpQpOtea'])
print("Fine-tune Status:", status['status'])
