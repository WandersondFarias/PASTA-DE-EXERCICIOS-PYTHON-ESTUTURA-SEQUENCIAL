import qrcode

# Defina os detalhes do seu Wi-Fi
ssid = "wanderson"  # Nome da sua rede Wi-Fi
password = "wf251174"  # Senha da sua rede Wi-Fi
security_type = "WPA"  # Tipo de segurança (WEP, WPA, WPA2)

# Formate os dados no padrão de Wi-Fi para QR Code
wifi_data = f"WIFI:T:{security_type};S:{ssid};P:{password};;"

# Crie o QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(wifi_data)
qr.make(fit=True)

# Gere a imagem do QR Code
img = qr.make_image(fill='black', back_color='white')

# Salve a imagem do QR Code
img.save("wifi_qrcode.png")

print("QR Code gerado e salvo como wifi_qrcode.png")
