doc = []
while True:
    sentence = input()
    if len(sentence) == 0:
        break
    else:
        doc.extend(sentence.replace("\n", "").split())

print("_".join(doc))

