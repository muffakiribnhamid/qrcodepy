import qrcode
import pyshorteners

facebook = "https://www.facebook.com/itz.muffakir.9"
insta = "https://www.instagram.com/muffakir_hamid/"

s = pyshorteners.Shortener()
fb = s.tinyurl.short(facebook)
ig = s.tinyurl.short(insta)

sample_image = qrcode.make("My Links : \n facebook : {} \n Instagram : {}".format(fb,ig))
sample_image.save('bio.png')
