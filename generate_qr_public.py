#!/usr/bin/env python3
import qrcode

# URL pública de GitHub Pages
url = "https://a242844jr-joel.github.io/restaurante-menu/"

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
img.save("menu_qr_public.png")

print(f"✓ Código QR público generado exitosamente!")
print(f"✓ URL: {url}")
print(f"✓ Imagen guardada como: menu_qr_public.png")
print(f"\n📱 Escanea este QR con tu móvil para acceder al menú desde cualquier lugar.")
print(f"🖨️  Imprime este QR y colócalo en las mesas de tu restaurante.")
