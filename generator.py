import qrcode

print("=" * 50)
print("         QR CODE GENERATOR")
print("=" * 50)

data = input("Enter text or URL: ")

filename = input("Enter file name: ")

img = qrcode.make(data)

img.save(f"{filename}.png")

print(f"\nQR Code saved as {filename}.png")
