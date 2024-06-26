import requests

# Sua API Key do D-ID
API_KEY = 'YOUR_API_KEY'
API_URL = 'https://api.d-id.com/animate'

# Parâmetros para a animação
payload = {
    'script': 'Hello! This is a test animation.',
    'image_url': 'https://example.com/path_to_image.jpg'
}

# Cabeçalhos de autorização
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Envie a solicitação para a API
response = requests.post(API_URL, json=payload, headers=headers)

# Verifique a resposta
if response.status_code == 200:
    print('Animação criada com sucesso!')
    animation_url = response.json().get('result_url')
    print(f'URL da animação: {animation_url}')
else:
    print(f'Erro: {response.status_code}')
    print(response.text)
