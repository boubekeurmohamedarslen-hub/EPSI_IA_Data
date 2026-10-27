
def moyenne_admis(notes):
    admis = []
    for note in notes:
        if note >= 10:
                admis.append(note)
    return(admis)
print(moyenne_admis([8, 12, 16, 6]))
        
    