from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough,RunnableParallel,RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

model=ChatOpenAI(model="gpt-4o-mini" , openai_api_key=api_key)

parser=StrOutputParser()

prompt1=PromptTemplate(template="write a joke on {joke}",
                       input_variables=['joke'])

prompt2=PromptTemplate(template="Explain the joke {joke}",
                       input_variables=['joke'])

joke_gen_chain=RunnableSequence(prompt1,model,parser)


parallel_chain={
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
}

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
result=final_chain.invoke({
    'joke':'cricket'
})

print(result)