# Langchain Chatbot and Playthrough Notebook

This repository contains a Jupyter notebook and a multi-assistant chatbot that leverages Langchain's LLM pipelining capabilties. The Jupyter notebook demonstrates the use of Langchain's various prompt templates and chat models, while the chatbot is designed to handle multiple domains, including college scheduling, career counseling, financial advice, and academic advising.

## Files

- `jupyter_notebook.ipynb`: A Jupyter notebook showcasing the use of Langchain's prompt templates and chat models.
- `chatbot.py`: The multi-assistant chatbot code that integrates Langchain's ChatOpenAI and various prompts to provide answers to user queries.

## Usage

To explore the capabilities of Langchain and the functionality of the multi-assistant chatbot, follow these steps:

1. Clone the repository:
  

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebook to see examples of Langchain's prompt templates and chat models in action.

4. Run the chatbot using the following command:
   ```
   python langchat.py
   ```

## Features

- **Jupyter Notebook**: The notebook provides examples of using PromptTemplate, ChatPromptTemplate, and various other Langchain features.
- **Multi-Assistant Chatbot**: The chatbot can handle queries related to college scheduling, career counseling, financial advice, and academic advising.


## Multi-Assistant Chatbot Features

- **Multi-Domain Assistance**: The chatbot can handle queries related to college scheduling, career counseling, financial advice, and academic advising.
- **Langchain Integration**: The chatbot uses Langchain's ChatOpenAI and various prompts to provide answers to user queries.
- **Conversation Buffer Memory**: The chatbot uses ConversationBufferMemory to store and retrieve previous conversations, allowing for more personalized and context-aware responses.


## Jupyter Notebook Usage

## Installation

To run the notebook, you will need to install LangChain and its dependencies. You can do this using pip:

```
pip install langchain
```

## Usage

To use LangChain in your own projects, you can import the relevant classes from the `langchain` package. For example:

```python
from langchain import PromptTemplate
```

## Examples

The notebook includes examples of using the following LangChain classes:

- PromptTemplate
- StringPromptTemplate
- FunctionExplainerPromptTemplate
- FeastPromptTemplate
- FewShotPromptTemplate
- ChatPromptTemplate
- ChatMessagePromptTemplate
- MessagesPlaceholder

