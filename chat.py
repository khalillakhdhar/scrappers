import requests
from bs4 import BeautifulSoup

# Étape 1 : Envoyer une requête HTTP pour obtenir le contenu de la page
url = 'https://medium.com/tag/technology/latest'
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Étape 2 : Utiliser BeautifulSoup pour analyser le contenu HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Étape 3 : Extraire les titres des articles et les auteurs
    articles = soup.find_all('div', class_='postArticle')
    
    # Liste pour stocker les résultats
    article_list = []

    for article in articles:
        # Extraire le titre
        title = article.find('h3')
        if title:
            title_text = title.get_text(strip=True)
        else:
            title_text = "Titre non disponible"

        # Extraire le nom de l'auteur
        author = article.find('a', class_='ds-link')
        if author:
            author_name = author.get_text(strip=True)
        else:
            author_name = "Auteur non disponible"
        
        # Ajouter le titre et l'auteur à la liste
        article_list.append((title_text, author_name))

    # Étape 4 : Afficher les résultats
    for idx, (title, author) in enumerate(article_list, 1):
        print(f"Article {idx}: {title} - Auteur: {author}")
else:
    print(f"Erreur {response.status_code} lors de la récupération de la page.")
