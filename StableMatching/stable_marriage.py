from collections import deque 

def gale_shapley_algorithm(men_pref, women_pref):
    
    free_men = [i for i in men_pref]
    men_proposal = {i:[] for i in men_pref}
    women_partner = {i:None for i in women_pref}
    print(men_proposal, women_partner)

    while free_men:
        man = free_men.pop(0)
        for woman in men_pref[man]:
            if woman not in men_proposal[man]:
                curr_partner = women_partner[woman]
                women_choices = women_pref[woman]
                if not curr_partner:
                    women_partner[woman] = man
                    break
                else:
                    if women_choices.index(man) < women_choices.index(curr_partner):
                        free_men.append(curr_partner)
                        women_partner[woman] = man
                        break
    
    return {i:j for j,i in women_partner.items() if i}
     

# Equal men to women count:
men_pref = {
    'a': ['A', 'B', 'C', 'D'],
    'b': ['A', 'C', 'B', 'D'],
    'c': ['B', 'C', 'A', 'D'],
    'd': ['A', 'B', 'D', 'C']
}

women_pref = {
    'A': ['d', 'c', 'a', 'b'],
    'B': ['a', 'd', 'b', 'c'],
    'C': ['d', 'b', 'c', 'a'],
    'D': ['b', 'c', 'a', 'd']
}


# more men, less women
men_pref1 = {
    'a': ['A', 'B', 'C', 'D'],
    'b': ['A', 'C', 'B', 'D'],
    'c': ['B', 'C', 'A', 'D'],
    'd': ['A', 'B', 'D', 'C'],
    'e': ['D', 'B', 'D', 'C']
}

women_pref1 = {
    'A': ['d', 'c', 'a', 'b','e'],
    'B': ['a', 'd', 'e', 'b', 'c'],
    'C': ['d', 'e', 'b', 'c', 'a'],
    'D': ['e', 'b', 'c', 'a', 'd']
}

# less men, more women
men_pref2 = {
    'a': ['A', 'B', 'C', 'D'],
    'b': ['D', 'C', 'B', 'E'],
    'c': ['B', 'C', 'E', 'D'],
    'd': ['E', 'B', 'D', 'C'],
}

women_pref2 = {
    'A': ['d', 'c', 'a', 'b'],
    'B': ['a', 'd', 'b', 'c'],
    'C': ['d', 'b', 'c', 'a'],
    'D': ['b', 'c', 'a', 'd'],
    'E': ['c', 'd', 'b', 'a'],
    'F': ['c', 'd', 'b', 'a'],
    'G': ['a', 'd', 'b', 'c'],
    'H': ['a', 'b', 'c', 'd'],
    'I': ['d', 'b', 'c', 'a'],
}

result = gale_shapley_algorithm(men_pref, women_pref)
result1 = gale_shapley_algorithm(men_pref1, women_pref1)
result2 = gale_shapley_algorithm(men_pref2, women_pref2)
print('Equal men and women', result,'\nMore men less women',result1, '\nLess men more women', result2)
