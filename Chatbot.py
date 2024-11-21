import nltk
#nltk.download("punkt_tab")
#nltk.download("wordnet")
from nltk import WordNetLemmatizer
from nltk import word_tokenize

purpose="customer support"
conversation_type="Simple QnA"
dataset=[
    {"input":"Hello","response":"Hi"},
    {"input":"What is your name","response":"My name is Chatbot"},
    {"input":"How are you","response":"I am fine what about you?"},
    {"input":"What are you","response":"I am chatbot for customer Support designed for an Internship task"},
    {"input":"what type of services you offer","response":"I am a Simple QnA for basic Questions"},
    {"input":"I am having issues with a product","response":"I am sorry to hear that please provide me with more details"}

]
try:
    lematizer=WordNetLemmatizer()
    tokenizeddataset=[]
    for entry in dataset:
        inputtokens=word_tokenize(entry["input"])
        responsetokens=word_tokenize(entry["response"])
        lematizedinput=[lematizer.lemmatize(token) for token in inputtokens]
        lematizedresponse=[lematizer.lemmatize(token)for token in responsetokens]
        tokenizeddataset.append({"input":lematizedinput,"response":lematizedresponse})
    def generate_response(userinput):
        userinput_tokens = word_tokenize(userinput)
        lemmatized_userinput = [lematizer.lemmatize(token) for token in userinput_tokens]
        for entry in tokenizeddataset:
            if lemmatized_userinput == entry["input"]:
                return " ".join(entry["response"])
        return "Sorry, I did not understand that"
    def chatbot():
        a=True
        while(a==True):
            userinput=input("User:")
            response=generate_response(userinput)
            print("Chatbot: ",response)
    def main():
        chatbot()
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("\nBye")

