import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        return f"Error fetching IP: {e}"

public_ip = get_public_ip()
print(f"Your public IP address is: {public_ip}")
a = input()
