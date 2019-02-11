import os

fini = False

while (fini == False) :

    commande = input()

    commande = commande.split(" ")

    if(commande[0] == '-i' or commande[0] == '--input-directory') :

        fichier = commande[1]

        fichier_ouvert = open(fichier, 'r')
        nom = fichier_ouvert.name
        nom = nom.replace(".md", "")
        fichier_html = open(nom+".html", 'a+')
        print(nom+".html")
        line_fichier_ouvert = fichier_ouvert.read().splitlines()

        for i in range(len(line_fichier_ouvert)) :

            line = line_fichier_ouvert[i]

            print(line)

            line = line.replace("*", "<em>")

            if (line.startswith("# ")) :
                print("1")
                line = line.replace("# ", "")
                fichier_html.write("<h1>" + line + "</h1>")

            if (line.startswith("## ")):
                print("2")
                line = line.replace("## ", "")
                fichier_html.write("<h2>" + line + "</h2>")

            if (line.startswith("### ")):
                print("3")
                line = line.replace("### ", "")
                fichier_html.write("<h3>" + line + "</h3>")

            if (line.startswith("http")):
                print("4")
                fichier_html.write("<a href=\""+line+"\">"+line+"</a>")

            if(line.startswith("- ")):
                print("5")
                line = line.replace("- ", "")
                fichier_html.write("<ul><li>"+line+"</li></ul>")

            fichier_html.write("<br>")

        fichier_html.close()

    elif (commande[0] == "-h"):

        print("-i --input-directory : Fichier à aller chercher pour convertir")
        print("-h : affichier l'aide concernant les commandes")

    else :

        print("cette commande n'existe pas")