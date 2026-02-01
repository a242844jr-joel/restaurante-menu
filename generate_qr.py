#!/usr/bin/env python3
import qrcode
import socket

# Obtener la IP local
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# URL del servidor local
url = f"http://{local_ip}:8000"

# Crear código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crear imagen
img = qr.make_image(fill_color="black", back_color="white")
img.save("menu_qr.png")

print(f"✓ Código QR generado exitosamente!")
print(f"✓ URL: {url}")
print(f"✓ Imagen guardada como: menu_qr.png")
print(f"\nEscanea el código QR con tu móvil para acceder al menú.")
