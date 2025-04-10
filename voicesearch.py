import speech_recognition as sr
import wikipedia as wi

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("give your question")
    audio=recognizer.listen(source)

try:
    question=recognizer.recognize_google(audio)
    print(f"you said {question}")

    summary= wi.summary(question)
    print(f"wikipedia Suammry \n{summary}")
    print(summary)

    filename = "output.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(summary)
        print(summary)

except Exception as e:
    print("error",str(e))
