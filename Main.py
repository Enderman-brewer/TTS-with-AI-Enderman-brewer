print("______________________________________________")
print("| Concept By Enderman-brewer")
print("| ...powered by Bard, the AI with a spark of genius.")
print("------------------------------------------------")
# Settings (frequently touched first)
delay_after_speech = 5
log_file = "word_log.txt"
chatgpt_api_key = 0
google_ai_api_key = "your_google_ai_api_key"
voice_index = 0
speech_rate = 175
volume = 1.0
noise_cancellation = True
confidence_threshold = 0.5
show_recognized_text = True
partial_results = False
log_verbosity = 1
api_retries = 3
api_timeout = 10
quit_command = "quit"
output_device = None

# Functions
def log_words(words):
    with open(log_file, "a") as file:
        file.write(words + "\n")

def get_chatgpt_response(text):
    # ... replace with actual ChatGPT API call and response format handling

def get_google_ai_response(text):
    # ... replace with actual Google AI API call and response format handling

def listen_and_speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Speak now:")
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                log_words(text)
                engine.say(text)
                engine.runAndWait()

                time.sleep(delay_after_speech)

                # Prioritize ChatGPT response
                if chatgpt_api_key != 0:
                    try:
                        chatgpt_response = get_chatgpt_response(text)
                        if chatgpt_response:
                            engine.say(chatgpt_response)
                            engine.runAndWait()
                            break
                    except Exception as e:
                        print(f"Error connecting to ChatGPT: {e}")

                # Fallback to Google AI if ChatGPT unavailable or didn't respond
                if google_ai_api_key and not chatgpt_response:
                    try:
                        google_ai_response = get_google_ai_response(text)
                        if google_ai_response:
                            engine.say(google_ai_response)
                            engine.runAndWait()
                    except Exception as e:
                        print(f"Error connecting to Google AI: {e}")

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            if text.lower() == quit_command:
                break

# TTS initialization
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[voice_index].id)
engine.setProperty('rate', speech_rate)
engine.setProperty('volume', volume)
if output_device:
    engine.setProperty('device', output_device)

# Start the real-time loop
threading.Thread(target=listen_and_speak).start()

