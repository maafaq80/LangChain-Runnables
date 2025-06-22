from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv
import os 

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

model=ChatOpenAI(model="gpt-4o-mini",
                 openai_api_key=api_key)

prompt=PromptTemplate(
    template="write a joke for the {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()

chain=RunnableSequence(prompt,model,parser)
result=chain.invoke({
    'topic':'AI'
})

print(result)

