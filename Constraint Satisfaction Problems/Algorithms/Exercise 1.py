# Você deve planejar a irrigação de uma plantação por 5 dias consecutivos.
# A irrigação total não pode ultrapassar 20 mm.
#
# Previsão do Tempo:
# ● Dia 1: Sem chuva (irrigar 10 mm, 5 mm, ou 2 mm)
# ● Dia 2: Chuva leve (0 a 4 mm de chuva prevista - irrigar 5 mm ou 2 mm)
# ● Dia 3: Chuva moderada (5 a 9 mm de chuva prevista - irrigar 2 mm ou 0 mm)
# ● Dia 4: Sem chuva (irrigar 10 mm, 5 mm, ou 2 mm)
# ● Dia 5: Chuva intensa (10 mm ou mais de chuva prevista - irrigar 0 mm)
#
# Encontre uma combinação válida.

# Irrigation planning
options = [
    [10, 5, 2],  # day 1
    [5, 2],      # day 2
    [2, 0],      # day 3
    [10, 5, 2],  # day 4
    [0]          # day 5
]

# max irrigation at the end of the 5 days
max_irrigation = 20

def backtrack(day, currentIrrigation, currentSum):
    if day == len(options): # all days have been processed
        if currentSum <= max_irrigation: 
            return currentIrrigation.copy() # that's the solution
        else:
            return None # to much irrigation
    
    for amount in options[day]:
        if currentSum + amount > max_irrigation: # if too much irrigation
            continue # skip this amount
        
        currentIrrigation.append(amount) #if not too much irrigation, add it to the current irrigation
        
        # then recurse to the next day
        result = backtrack(day + 1, currentIrrigation, currentSum + amount)
        
        # if there's a solution, return it
        if result is not None:
            return result
        
        # if not, remove the last amount added
        currentIrrigation.pop()
        
    # if no solution was found, return None
    return None

solution = backtrack(0, [], 0)

if solution is not None:
    print("mm de irrigacao por dia:", solution)
    print("Irrigacao total:", sum(solution), "mm")
else:
    print("Nenhuma solução encontrada.")