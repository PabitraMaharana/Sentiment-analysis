import tkinter as tk
from tkinter import scrolledtext, END
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Created By: Pabitra Maharana
#Email:maharanapabitra156@gmail.com

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    sentiment = "positive" if sentiment_scores['compound'] > 0 else "negative" if sentiment_scores['compound'] < 0 else "neutral"
    return sentiment

def send_message(event=None):
    user_input = input_entry.get().strip()
    print(f"User Input: {user_input}")
    if not user_input:
        return
    input_text.config(state=tk.NORMAL)
    input_text.insert(tk.END, f"You: {user_input}\n\n", "user")
    input_text.config(state=tk.DISABLED)
    if user_input.lower() == 'exit':
        print("Exiting...")
        root.destroy()
    elif user_input.lower() == '\i':
        print("Displaying Information...")
        input_text.config(state=tk.NORMAL)
        input_text.insert(tk.END, "Chatbot: \n->Created By: Pabitra Maharana\n->About: I perform sentiment analysis using the VADER (Valence Aware Dictionary and Sentiment Reasoner) sentiment analysis tool from the NLTK (Natural Language Toolkit) library.\n", "chatbot") 
        input_text.see(END)
        input_text.config(state=tk.DISABLED)
    elif user_input.lower() == '\h':
        print("Displaying Help...")
        input_text.config(state=tk.NORMAL)
        input_text.insert(tk.END, "Chatbot: Type the sentence in the below input bar and press Enter Key or Send Button to analyse the sentiment of the sentence \nClick Clear Chat to clear the screen\n\n", "chatbot") 
        input_text.see(END)
        input_text.config(state=tk.DISABLED)
    else:
        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}")
        input_text.config(state=tk.NORMAL)
        input_text.insert(tk.END, f"Chatbot: The sentiment of your input is {sentiment}.\n\n", "chatbot")
        input_text.see(END)
        input_text.config(state=tk.DISABLED)
    input_entry.delete(0, tk.END)

def new_chat():
    print("Starting a New Chat...")
    input_text.config(state=tk.NORMAL)
    input_text.delete(1.0, tk.END)
    input_text.insert(tk.END, "Chatbot: Hello! I'm here to analyze the sentiment of your messages.\nUse: \n-> \i for More Information \n-> \h for How to Use.\n\n", "chatbot")
    input_text.config(state=tk.DISABLED)

def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_colors()

def update_colors():
    if dark_mode:
        root.configure(bg="#333")
        input_text.config(bg="#222", fg="white", insertbackground="white")
        input_text.configure(cursor="arrow white")  
        input_entry.config(bg="#222", fg="white")
        send_button.config(bg="#444", fg="white")
        new_chat_button.config(bg="#444", fg="white")
    else:
        root.configure(bg="white")
        input_text.config(bg="white", fg="black", insertbackground="black")
        input_text.configure(cursor="arrow black")  
        input_entry.config(bg="white", fg="black")
        send_button.config(bg="#eee", fg="black")
        new_chat_button.config(bg="#eee", fg="black")

dark_mode = False

root = tk.Tk()
root.title("Chat Sentiment Reader")
root.geometry("400x600")

mode_button = tk.Button(root, text="Dark-White Change", command=toggle_mode)
mode_button.pack()

input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50, state=tk.DISABLED,font=("Helvetica", 12))
input_text.pack(padx=10, pady=10)
input_text.tag_configure("user", foreground="blue", justify="right")
input_text.tag_configure("chatbot", foreground="green")
input_text.configure(borderwidth=2, relief="solid")

entry_frame = tk.Frame(root)
entry_frame.pack()

send_button = tk.Button(entry_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10)

input_entry = tk.Entry(entry_frame, width=40, font=("Helvetica", 12))
input_entry.pack(side=tk.LEFT, padx=10, pady=(10, 10))
input_entry.bind("<Return>", send_message)

new_chat_button = tk.Button(root, text="Clear Chat", command=new_chat)
new_chat_button.pack()

new_chat() 
update_colors()
root.mainloop()

