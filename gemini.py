import config
import google.generativeai as genai

genai.configure(api_key=config.gemini_api_key)

# map of chat_id to gemini client
clients = {}

def get_client(chat_id):
	if chat_id not in clients:
		clients[chat_id] = genai.GenerativeModel('gemini-pro')
	return clients[chat_id]

def generate_new_model(chat_id):
	if chat_id in clients:
		del clients[chat_id]
	return get_client(chat_id)

def response(chat_id, prompt):
	return get_client(chat_id).generate_content(prompt)