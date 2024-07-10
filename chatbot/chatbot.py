import openai
import json

openai.api_key = ''

def getResponse(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 150
    )
    return response.choices[0].text.strip()
    
def loadData(fileName):
    with open(fileName) as file:
        data = json.load(file)
    return data

def chatbot(data):
    print("Hii! I'm your friendly chatbot. Ask me anything about your timetable.")
    while True:
        query = input("You: ")
        if query.lower == ["exit", "quit"]:
            print("Bye! Have a great day.")
            break

if __name__ == '__main__':
    data = loadData("data.json")

    chatbot(data) 