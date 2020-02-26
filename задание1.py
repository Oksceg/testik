ad_dict = {
"раз": "первый",
"два": "второй"
}
some_dict = {}
some_dict["ноль"] = "нулевой"
some_dict.update(ad_dict) #1
dctn = {}
elems = ["never", "gonna", "give", "you", "up", "never", "gonna", "let", "you", "down"]
for elem in elems:
   if elem in dctn:
       dctn[elem] += 1
   else:
       dctn[elem] = 1
keys = list(dctn.keys())
values = list(dctn.values()) #2
text = "Тихо  было  в  храме,  и красноватым светом мерцала лампада и распятия. И что-то там в чем-то."
text = text.split(".")
freq = {}
for line in text:
    words = line.split()
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
print(freq)
keys = list(freq.keys())
values = list(freq.values())
fin_freq = {}
if "в" in keys:
    fin_freq.update(freq)
