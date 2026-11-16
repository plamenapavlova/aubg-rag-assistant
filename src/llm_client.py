from openai import OpenAI
from src import config

client = OpenAI(api_key = config.OPENAI_API_KEY, timeout = config.LLM_MAX_WAITING_TIME)

def generate_response(instructions, prompt):
    response =client.responses.create(
        model = config.LLM_MODEL,
        reasoning ={"effort": "low"},
        max_output_tokens = config.LLM_MAX_OUTPUT_TOKENS,
        instructions = instructions,
        input = prompt
    )

    return response.output_text

if __name__ == "__main__":
    print(generate_response("Answer in one sentence", "Say hello to an AUBG student"))



