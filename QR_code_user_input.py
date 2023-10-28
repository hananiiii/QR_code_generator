import qrcode

url = input("Enter the URL you want to generate a QR code for: ")
#https://www.youtube.com/watch?v=vTVmQxTzz2k
features = qrcode.QRCode(version=1, box_size=40, border=3)
features.add_data(url)
features.make(fit=True)
generate_image = features.make_image(fill_color="black", back_color="white")

file_name = input("Enter the file name : ")
#QR_Code_example.png
generate_image.save(file_name)

print(f"QR code saved as {file_name}")
