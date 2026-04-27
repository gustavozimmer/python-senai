import numpy as np
vetor = np.array([
    [3, 4, 5],
    [5, 4, 3],
    [5, 5, 5]])
medias = vetor.mean(axis=1) 
indice_melhor = np.argmax(medias)
maior_media = medias[indice_melhor]
print(f"O restaurante {indice_melhor + 1} possui a melhor média: {maior_media}")