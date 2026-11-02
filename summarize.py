import os 
from openai import OpenAI
from dotenv import load_dotenv
from scrapper import fetch_website_contents
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv()         



prompt = ChatPromptTemplate.from_template(
    "Give a short, friendly summary of this website:\n\n{website}"
)

# ② the same model from Class 1, wrapped for LangChain
model = ChatOpenAI(model="openai/gpt-oss-120b", temperature=0.3,api_key=os.getenv("GROQ_API_KEY"),
                            base_url="https://api.groq.com/openai/v1")

# ③ the package-opener: hands back plain text
parser = StrOutputParser()

# ④ snap them together  (| means "then")
chain = prompt | model | parser


def summarize(url):
    # ⑤ run it; the dict fills the {website} blank by name
    return chain.invoke({"website": fetch_website_contents(url)})


if __name__ == "__main__":
    print(summarize("https://reference.langchain.com/python/langchain-community/tools/wikipedia/tool"))




"""
#This implementation happened first 
system_prompt = "Give a short, friendly summary of this website"
client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                            base_url="https://api.groq.com/openai/v1")


def summarize(url):
    website = fetch_website_contents(url)
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role":"system", "content": system_prompt},
            {"role":"user",   "content": f"Summarize this website:\n\n{website}"},
        ],
    )
    return response.choices[0].message.content 

if __name__ == "__main__":
    print(summarize("https://reference.langchain.com/python/langchain-community/tools/wikipedia/tool"))
"""