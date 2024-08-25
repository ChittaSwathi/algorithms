from collections import deque 

def gale_shapley_algorithm(men_pref, women_pref):
    
    """
    Initialize all men and women to free
    while there exist a free man m who still has a woman w to propose to 
    {
        w = m's highest ranked such woman to whom he has not yet proposed
        if w is free
        (m, w) become engaged
        else some pair (m', w) already exists
        if w prefers m to m'
            (m, w) become engaged
            m' becomes free
        else
            (m', w) remain engaged    
    }
    """
    free_men = [i for i in men_pref]
    men_proposal = {i:[] for i in men_pref}
    women_partner = {i:None for i in women_pref}

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
    
    return {i:j for j,i in women_partner.items()}
     

# Example usage:
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

result = gale_shapley_algorithm(men_pref, women_pref)
print(result)
