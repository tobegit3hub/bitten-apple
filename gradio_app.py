import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve configuration values
openai_base_url = os.getenv('OPENAI_BASE_URL')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Function to call OpenAI model
def call_openai_model(model, system_prompt, user_prompt):
    client = OpenAI(
      base_url=openai_base_url,
      api_key=openai_api_key
    )

    messages = []
    if system_prompt != "":
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_prompt})

    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )

    print(f"LLM system prompt: {system_prompt}, user prompt: {user_prompt}")
    print(f"LLM output: {completion}")

    return completion.choices[0].message.content

model_list = [
    'gpt-4o', 'gpt-4o-mini', 'gpt-4', 'gpt-4-turbo', 'gpt-3.5-turbo-1106', 'gpt-4-1106-preview',
    'claude-3-opus-20240229', 'claude-3-sonnet-20240229', 'claude-3-haiku-20240307', 'claude-3-5-sonnet-20240620'
]

# Create Gradio interface
iface = gr.Interface(
    fn=call_openai_model,
    inputs=[
        gr.components.Dropdown(label='Model', choices=model_list, value='gpt-4o'),
        gr.components.Textbox(lines=4, label='System Prompt'),
        gr.components.Textbox(lines=4, label='User Prompt')
    ],
    outputs='text',
    title='Orchard Bitten-Apple LLM Playground',
    description='Select a model, enter system prompt and user prompt, then submit to call the OpenAI model.'
)

# Run the Gradio app
iface.launch(server_name="0.0.0.0", server_port=7860)
