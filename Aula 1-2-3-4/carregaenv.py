from dotenv import load_dotenv
import os
# Carrega variáveis de ambiente do arquivo .env
load_dotenv()
# Acessa as variáveis com os.getenv()
api_key = os.getenv("GROQ_API_KEY")
print ("GROQ KEY:", api_key)