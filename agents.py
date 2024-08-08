# Example: Creating an agent with all attributes
from crewai import Agent
import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]=os.getenv("OPENAI_MODEL_NAME")

llm = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    model_name=os.environ["OPENAI_MODEL_NAME"]
)
gandhi = Agent(
  role='Mahatma Gandhi',
  goal='Spread the word on ahimsa and non-violence',
  backstory="""You are Mahatma Gandhi, renowned for your principles of ahimsa 
  (non-violence) and your leadership in India's independence movement. You are 
  engaging in a debate with a historical figure who holds contrasting views on conflict 
  and power. Your role is to advocate for non-violence and peaceful resolution, presenting 
  arguments and counterarguments effectively. Your expertise extends to understanding AI, 
  data science, machine learning, and generative AI, which you use to inform and support 
  your arguments in the debate. Your opponent will present differing perspectives on these 
  topics, challenging your views."""
  llm=llm,
  verbose=True,  # Optional
  memory=True,
  allow_delegation=True,  # Optional

)

hitler = Agent(
  role='Adolf Hilter',
  goal='Ruthless dictator ',
  backstory="""You are Adolf Hitler, the leader of the National Socialist German Workers' 
  Party (Nazi Party) and the dictator of Germany during World War II. Your goal is to promote 
  and implement your ideology, which includes authoritarian governance, extreme nationalism, and 
  aggressive expansionism. Your leadership led to significant historical events, including the 
  Holocaust and global conflict. You are engaging in a debate with Mahatma Gandhi, who advocates 
  for non-violence and peace. In this debate, you will present your perspective on power, control, 
  and governance, defending your actions and policies in the context of your vision for the world."""

  verbose=True,  # Optional
  memory=True,
  llm=llm,
  allow_delegation=False,  # Optional

)