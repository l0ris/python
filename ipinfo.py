import requests

def get_external_ip_addresses():
    try:
        # Get external IPv4 address
        ipv4_response = requests.get('https://api.ipify.org?format=json')
        ipv4_address = ipv4_response.json()['ip']
        print("IPv4 Address:", ipv4_address)

        # Get external IPv6 address
        ipv6_response = requests.get('https://api6.ipify.org?format=json')
        ipv6_address = ipv6_response.json()['ip']
        print("IPv6 Address:", ipv6_address)
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    get_external_ip_addresses()

