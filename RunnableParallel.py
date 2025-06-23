from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
import os 

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

model=ChatOpenAI(model="gpt-4o-mini",
                 openai_api_key=api_key)

prompt1=PromptTemplate(template="Generate a tweet about {topic}",
                       input_variable=['topic'])

prompt2=PromptTemplate(template="Generate a linkdein about{topic}",
                       input_variable=['topic'])

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkdein':RunnableSequence(prompt2,model,parser)
})

result=parallel_chain.invoke({'topic':'AI'})
print(result['tweet'])

print(result['linkdein'])