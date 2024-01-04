import json

filename = "animaux_leschats_debutant.json"

f = open(filename,"r")
data_json = f.read()
f.close()

questionnaire = json.loads(data_json)
print("Catégorie : ",questionnaire["categorie"])
print("Titre : ",questionnaire["titre"])
#print(type(questionnaire["questions"]))
#print(len(questionnaire["questions"]))
"""
for i in range(len(questionnaire["questions"])):
    print(questionnaire["questions"][i])
print(questionnaire["questions"][0]["titre"])
"""

"""
nb_questions = len(questionnaire["questions"])
total = 0
for i in range(nb_questions):
    print(questionnaire["questions"][i]["titre"])
    print()
    choix = questionnaire["questions"][i]["choix"]
    for j in range(len(questionnaire["questions"][i]["choix"])):
        print(str(j+1) + ") " + str(choix[j][0]))
        if choix[j][1]:
            #print(choix[j][1],j)
            bonne_reponse = j
    reponse = input("Votre réponse : ")
    if int(reponse)-1 == bonne_reponse:
        total += 1
    print()
print("Bonne reponse : ",total)
"""