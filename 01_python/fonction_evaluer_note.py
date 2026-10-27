def evaluer_note(note):
    if note >= 16:
        return 'excellent'
    elif note >= 10:
        return 'admis'
    else:
        return 'refus'
decision = evaluer_note(9)
print('decision:', decision)
        
    

        
    