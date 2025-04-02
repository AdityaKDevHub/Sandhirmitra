consonants = ("क", "ख", "ग", "घ", "ङ",
              "च", "छ", "ज", "झ", "ञ",
              "ट", "थ", "ड", "ढ", "ण",
              "त", "थ", "द", "ध", "न",
              "प", "फ", "ब", "भ", "म",
              "य", "र", "ल", "व",
              "श", "ष", "स", "ह")

consonants2 = ("क", "ख", "ग", "घ",
               "च", "छ", "ज", "झ",
               "ट", "थ", "ड", "ढ",
               "त", "थ", "द", "ध",
               "प", "फ", "ब", "भ",
               "य", "र", "ल", "व",
               "श", "ष", "स", "ह")

consonants3 = ("ग", "घ", "ङ",
               "ज", "झ", "ञ",
               "ड", "ढ", "ण",
               "द", "ध", "न",
               "ब", "भ", "म",
               "य", "र", "ल", "व",
			   "श", "ष", "स", "ह")

consonants3 = ("ग", "घ", "ङ",
               "ज", "झ", "ञ",
               "ड", "ढ", "ण",
               "द", "ध", "न",
               "ब", "भ", "म",
               "य", "र", "ल", "व", "ह")

matra = ("ा", "ि", "ी", "ू", "ू", "ृ", "ॄ", "े", "ै", "ो", "ौ")
annunasik = ("ञ", "म", "ङ", "ण", "न")
ichmatra = ("ि", "ी", "ु", "ू", "ृ", "ॄ", "ै", "ै", "ो", "ौ")

def Swar_Sandhi(term1, term2, end, start):
	if (end in consonants) or (end == "ा"):
		if start in ("अ", "आ"):
			return term1 + "ा" + term2[1:]
		elif start in ("इ", "ई"):
			return term1 + "े" + term2[1:]
		elif start in ("उ", "ऊ"):
			return term1 + "ो" + term2[1:]
		elif start in ("ॠ", "\u090B"):
			return term1 + "र्" + term2[1:]
		elif start in ("ऌ"):
			return term1 + "ल्" + term2[1:]
		elif start in ("ए", "ऐ"):
			return term1[:-1] + "ै" + term2[1:]
		elif start in ("ओ", "औ"):
			return term1[:-1] + "ौ" + term2[1:]

	elif end in ("ि", "ी"):
		if start in ("इ", "ई"):
			return term1 + "ी" + term2[1:]
		elif start in ("अ", "आ", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-1] + ("्य", "्या", "्यु", "्यू", "्यृ", "्यॄ", "्ये", "्यै", "्यो", "्यौ")[val] + term2[1:]

	elif end in ("ु", "ू"):
		if start in ("उ", "ऊ"):
			return term1 + "ू" + term2[1:]
		elif start in ("अ", "आ", "इ", "ई", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-1] + ("्व", "्वा", "्वि", "्वी", "्वृ", "्वॄ", "्वे", "्वै", "्वो", "्वौ")[val] + term2[1:]

	elif end in ("ृ", "ॄ"):
		if start in ("ॠ", "\u090B"):
			return term1 + "ॄ" + term2[1:]
		elif start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-1] + ("्र", "्रा", "्रि", "्री", "्रु", "्रू", "्रे", "्रै", "्रो", "्रौ")[val] + term2[1:]

	elif end == "ऌ":
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return ("ल", "ला", "लि", "ली", "लु", "लू", "लृ", "लॄ", "ले", "लै", "लो", "लौ")[val] + term2[1:]

	elif end == "े":
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-1] + ("य", "या", "यि", "यी", "यु", "यू", "यृ", "यॄ", "ये", "यै", "यो", "यौ")[val] + term2[1:]

	elif end == "ै":
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-1] + ("ाय", "ाया", "ायि", "ायी", "ायु", "ायू", "ायृ", "ायॄ", "ाये", "ायै", "ायो", "ायौ")[val] + term2[1:]

	elif end == "ो":
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-1] + ("व", "वा", "वि", "वी", "वु", "वू", "वृ", "वॄ", "वे", "वै", "वो", "वौ")[val] + term2[1:]

	elif end == "ौ":
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-1] + ("ाव", "ावा", "ावि", "ावी", "ावु", "ावू", "ावृ", "ावॄ", "ावे", "ावै", "ावो", "ावौ")[val] + term2[1:]

def Vyanjan_Sandhi(term1, term2, end, start):
	penultimate = term1[-2]

	if penultimate == "क":
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-2] + ("ग", "गा", "गि", "गी", "गु", "गू", "गृ", "गॄ", "गे", "गै", "गो", "गौ")[val] + term2[1:]
		elif start in consonants2:
			return term1[:-2] + "ग्" + term2
		elif start in annunasik:
			return term1[:-2] + "ङ्" + term2

	elif penultimate == "च":
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-2] + ("ज", "जा", "जि", "जी", "जु", "जू", "जृ", "जॄ", "जे", "जै", "जो", "जौ")[val] + term2[1:]
		elif start in consonants2:
			return term1[:-2] + "ज्" + term2
		elif start in annunasik:
			return term1[:-2] + "ञ्" + term2

	elif penultimate == "ट":
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-2] + ("ड", "डा", "डि", "डी", "डु", "डू", "डृ", "डॄ", "डे", "डै", "डो", "डौ")[val] + term2[1:]
		elif start in consonants2:
			return term1[:-2] + "ड्" + term2
		elif start in annunasik:
			return term1[:-2] + "ण्" + term2

	elif penultimate == "त":
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-2] + ("द", "दा", "दि", "दी", "दु", "दू", "दृ", "दॄ", "दे", "दै", "दो", "दौ")[val] + term2[1:]
		elif start in consonants2:
			return term1[:-2] + "द्" + term2
		elif start in annunasik:
			return term1[:-2] + "न्" + term2

	elif penultimate == "प":
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-2] + ("ब", "बा", "बि", "बी", "बु", "बू", "बृ", "बॄ", "बे", "बै", "बो", "बौ")[val] + term2[1:]
		elif start in consonants2:
			return term1[:-2] + "ब्" + term2
		elif start in annunasik:
			return term1[:-2] + "म्" + term2

def Visarg_Sandhi(term1, term2, end, start):
	penultimate = term1[-2]

	if (penultimate in consonants) and (start == "अ"):
		return term1[:-1] + "ोऽ" + term2[1:]
	elif (penultimate in consonants) and (start in consonants3):
		return term1[:-1] + "ो" + term2

	elif penultimate in ichmatra:
		if start in ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ"):
			val = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ").index(start)
			return term1[:-1] + ("र", "रा", "रि", "री", "रु", "रू", "रृ", "रॄ" "रे", "रै", "रो", "रौ")[val] + term2[1:]
	
	elif (penultimate in consonants) or (penultimate in matra):
		if start in consonants3:
			return term1[:-1] + "र्" + term2
		elif start in ("च", "छ", "श"):
			return term1[:-1] + "श्" + term2
		elif start in ("त", "थ", "स"):
			return term1[:-1] + "स्" + term2
		elif start in ("ट", "ठ", "ष"):
			return term1[:-1] + "ष्" + term2
		elif term1 in ("नमः", "पुरः"):
			return term1[:-1] + "स्" + term2

	elif (penultimate in consonants) and (start in ("आ", "इ", "ई", "उ", "ऊ", "ॠ", "\u090B", "ए", "ऐ", "ओ", "औ")):
		return term1[:-1] + term2
	elif (penultimate == "आ") and (start in consonants3):
		return term1[:-1] + term2

def main():
	term1, term2 = input("प्रथमं पदं देहि (Enter first term): "), input("द्वितीयं पदं देहि (Enter second term): ")
	end, start = term1[-1], term2[0]
	result = None

	if (end in consonants) or (end in matra):
		result = Swar_Sandhi(term1, term2, end, start)
	elif end == "्":
		result = Vyanjan_Sandhi(term1, term2, end, start)
	elif (end == "ः") or (end == ":"):
		result = Visarg_Sandhi(term1, term2, end, start)

	if not result:
		print("\n\nअनयोः पदयोः संधि: नास्ति वा पदयोः त्रुटी भवतः वा अधुना यावत् सन्धिः न योजितः वा।\n(Either there's no 'Sandhi' in the terms, or either of the terms is incorrect or the resulting 'Sandhi' is not implemented yet.\n\n")
		return

	print(f"{term1} + {term2} = {result}\n\n")

if __name__ == "__main__":
	print("संधिर्मित्र\nMade by ADITYA VN KADIYALA\n")
	while True:
		main()
