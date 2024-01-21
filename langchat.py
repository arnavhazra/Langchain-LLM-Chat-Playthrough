import os
import json
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain
import dotenv
import json
from langchain import LLMChain, ChatPromptTemplate, RouterOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.llms import ChatOpenAI

memory = ConversationBufferMemory()

llm = ChatOpenAI(temperature=0.9)
dotenv.load_dotenv()

# Access the environment variable
open_api_key = os.environ.get("OPEN_API_KEY")

# Initialize the ChatOpenAI
llm = ChatOpenAI(temperature=0.9)

prompt_infos = [
    {
        "name": "college_scheduler",
        "description": "Good for helping with college scheduling and time optimization",
        "prompt_template": "You are a master scheduler.\n\nHere is a question:\n{input}"
    },
    {
        "name": "college_career_counselor",
        "description": "Good for providing college career counseling",
        "prompt_template": "You are a college career counselor.\n\nHere is a question:\n{input}"
    },
    {
        "name": "financial_advisor",
        "description": "Good for answering questions about college finances",
        "prompt_template": "You are a financial advisor.\n\nHere is a question:\n{input}"
    },
    {
        "name": "academic_advisor",
        "description": "Good for providing college academic advising",
        "prompt_template": "You are an academic advisor.\n\nHere is a question:\n{input}"
    }
]

destination_chains = {}
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = ChatPromptTemplate.from_template(template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain

router_template = r"""
Given a raw text input, determine the relevant assistants and call them to add their unique domain-specific perspective to the input.
Return a JSON object formatted to look like:
{{
  "destinations": [string, ...],
  "next_inputs": string
}}
<< CANDIDATE PROMPTS >>
{destinations}
<< INPUT >>
{{input}}
"""

destinations_str = "\n".join([f"{p['name']}: {p['description']}" for p in prompt_infos])
router_prompt = PromptTemplate(template=router_template.format(destinations=destinations_str), input_variables=["input"])
router_chain = LLMChain(llm=llm, prompt=router_prompt, memory=ConversationBufferMemory())

def run_chains(input_text):
    router_result_text = router_chain.run(input_text)
    try:
        router_result = json.loads(router_result_text)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON output")

    destinations = router_result.get("destinations", [])
    responses = []

    for destination in destinations:
        if destination in destination_chains:
            response = destination_chains[destination].run(input_text)
            responses.append(response)

    compiled_response = " ".join(responses)
    return compiled_response

st.title("Multi-Assistant Chatbot")

user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    response = run_chains(user_input)
    st.write(response)