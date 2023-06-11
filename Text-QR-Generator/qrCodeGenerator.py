import segno

print("Insert anything here.\n")
inserted_value = input("Insert : ")
qrcode = segno.make_qr(inserted_value)
qrcode.save("output.png", scale=10)
