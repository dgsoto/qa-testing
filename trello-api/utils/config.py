from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

API_KEY = os.getenv('TRELLO_API_KEY')
TOKEN = os.getenv('TRELLO_TOKEN')
BASE_URL = 'https://api.trello.com/1'

# Verificar que las variables estén configuradas correctamente
assert API_KEY, "TRELLO_API_KEY no está configurado"
assert TOKEN, "TRELLO_TOKEN no está configurado"
