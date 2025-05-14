# Cinco amigos - Ana, Bruno, Carlos, Diana e Eduardo - estão sentados em uma mesa redonda. Eles
# precisam se sentar de forma que:
#
# 1. Ana não pode estar ao lado de Bruno nem de Carlos.
# 2. Diana não pode estar ao lado de Eduardo.
# 3. Carlos não pode estar ao lado de Eduardo.
#
# Encontre uma configuração válida onde todos os amigos estejam sentados na mesa de forma que essas
# restrições sejam respeitadas.

people = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']

def is_valid(arrangement):
    def sitting_close(a, b): # check who are neighbors
        indexA = arrangement.index(a)
        indexB = arrangement.index(b)
        return(indexA + 1) % len(arrangement) == indexB or (indexA - 1) % len(arrangement) == indexB
    
    # check for all restrictions
    if(sitting_close('Ana', 'Bruno') or sitting_close('Ana', 'Carlos')):
        return False
    
    if(sitting_close('Diana', 'Eduardo')):
        return False
    
    if(sitting_close('Carlos', 'Eduardo')):
        return False
    
    return True

def backtrack(arrangement, used):
    # if seat is full
    if len(arrangement) == len(people): # if all people are seated
        if is_valid(arrangement): # and  arrangement is valid
            return arrangement # that's the solution
        else:
            return None # if not, no solution found
    
    for person in people:
        if person not in used:
            arrangement.append(person) # add person to arrangement
            used.add(person) # mark seat as used
            
            result = backtrack(arrangement, used) # recurse to the next seat
            
            if result is not None: # if there's a solution, return it
                return result
            
            arrangement.pop() # if not, remove last person added
            used.remove(person) # and unmark seat as used
    return None

solution = backtrack([], set())

if solution is not None:
    print("Arranjo valido:", solution)  
else:
    print("Nenhuma solucao encontrada.")