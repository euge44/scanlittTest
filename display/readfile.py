def display_clusters(data):
    clusters={}

    #enlève l'espace de citation count
    for donne in data:
        donne['Citation_count'] = donne['Citation count']
    print(data)

    #tri des données selon le nombre de citation
    data_tries = sorted(data, key=lambda doc: float(doc['Citation count']), reverse=True)
    print("========")
    print(data_tries)

    #tri par catégorie de cluster
    for donne in data_tries:
        cluster=donne['Cluster']
        if cluster not in clusters:
            clusters[cluster]=[]
        clusters[cluster].append(donne)
    return clusters





