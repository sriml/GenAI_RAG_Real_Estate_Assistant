from langchain.prompts import PromptTemplate
from langchain.chains.qa_with_sources.stuff_prompt import template

custom_template = "You are a helpful assistant for my research." + template

prompt = PromptTemplate(template=custom_template, input_variables=["summaries", "question"])

example_prompt = PromptTemplate(template="Content:{page_content}\nSource:{source}", input_variables=["page_content", "source"])

