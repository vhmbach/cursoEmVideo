import requests

# configurações do firewall
firewall_url = 'https://seu-firewall.com' # substitua com o URL do seu firewall
username = 'seu-username' # substitua com seu nome de usuário
password = 'sua-senha' # substitua com sua senha

# faz login no firewall
login_url = f"{firewall_url}/api/v1/access_token"
response = requests.post(login_url, json={"username": username, "password": password})
response.raise_for_status()
access_token = response.json()["access_token"]

# cria o backup
backup_url = f"{firewall_url}/diag_backup.php"
headers = {"Authorization": f"Bearer {access_token}"}
params = {"nopackages": "yes", "donotbackuprrd": "yes", "download": "download"}
response = requests.post(backup_url, headers=headers, params=params)

# salva o backup em um arquivo
backup_file = 'pfSense_backup.xml' # substitua com o nome que desejar
with open(backup_file, 'wb') as f:
    f.write(response.content)

print(f"Backup salvo em {backup_file}")
