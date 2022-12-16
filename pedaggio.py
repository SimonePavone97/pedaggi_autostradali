
pedaggi=[]
percorsi=[]

with open ("pedaggi.txt", "r") as file:
    for line in file:
        # x=(file.readline())
        pedaggi.append(line.strip().split(";"))
file.close

with open ("percorsi.txt", "r") as file:
    for line in file:
        # x=(file.readline())
        percorsi.append({
            "partenza" : line.strip().split(";")[0],
            "arrivo": line.strip().split(";")[1]      
                  })
file.close

lun_percorsi=len(percorsi)
lun_pedaggi=len(pedaggi)
citta=""   
costo=0.00
n_caselli=0
tratta=[]
partenza=""

for item in percorsi:
    partenza=item["partenza"]
    arrivo=item["arrivo"]
    i=0
    while i<lun_pedaggi:
        if pedaggi[i][0] in [partenza,citta]:
            if arrivo == pedaggi[i][1]:
                costo+=float(pedaggi[i][2])
                n_caselli+=1
                item["costo"]=round(costo,2)
                item["num_caselli"]=n_caselli
                citta=""   
                costo=0.00
                n_caselli=0
                i=lun_pedaggi
            else:
                costo+=float(pedaggi[i][2])
                n_caselli+=1
                citta=pedaggi[i][1]
                partenza=""
                i=0
        else:
            i+=1

for item in percorsi:
    if "costo" in item.keys():
        print("La tratta", item["partenza"], "a", item["arrivo"], "passa", item["num_caselli"], "e costa", item["costo"])
    else: 
        print("La tratta", item["partenza"], "a", item["arrivo"], "non esiste")

cost_min=percorsi[0]
i=0
while i<lun_percorsi:
    if "costo" in percorsi[i].keys():
        if percorsi[i]["costo"] < cost_min["costo"]:
            cost_min=percorsi[i]
            i=0
        else: i+=1
    else: i+=1
    

print("-"*40)
print("La tratta", cost_min["partenza"], "a", cost_min["arrivo"], "è la più economica")