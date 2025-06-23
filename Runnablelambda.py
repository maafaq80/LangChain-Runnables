from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough
from dotenv import load_dotenv
import os 


load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

def word_count(text):
    # topic = input_dict.get('topic', '')
    return len(text.split())

model=ChatOpenAI(model="gpt-4o-mini",
                 openai_api_key=api_key)

prompt1=PromptTemplate(template="Generate a tweet about {topic}",
                       input_variable=['topic'])

parser=StrOutputParser()

joke_gen=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
    })

final_chain=RunnableSequence(joke_gen,parallel_chain)
result=final_chain.invoke({
    'topic':'cricket'
})

print(result)