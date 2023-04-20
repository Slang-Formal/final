import re
import openai
import os
from dotenv import load_dotenv
load_dotenv()

def slang_word(informal):
    api_key = os.environ.get('openai')
    if not api_key:
        raise ValueError('OpenAI API key not set or is empty')
    openai.api_key = api_key
    model_engine = "text-davinci-003"
    prompt = "Can you tell me the words that are slang in the following sentence? I only want the words returned." + informal
    completion = openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=1024,n=1,stop=None,temperature=0.5,)
    response = completion.choices[0].text
    normal_string =re.sub("[^A-Z]", " ", response,0,re.IGNORECASE)
    final_list = normal_string.split()
    return(final_list)

