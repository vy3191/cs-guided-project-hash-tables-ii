# In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.
# The spy, if it exists:
#     Does not trust anyone else.
#     Is trusted by everyone else (he's good at his job).
#     Works alone; there are no other spies in the city-state.
# You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.
# If the spy exists and can be found, return their identifier. Otherwise, return -1.
def uncover_spy(n, trust):
    # cover the edge case here
    if len(trust) == 1:
        return trust[0][1]
    # have trust dict
    trust_dict = {}
    # loop through the trust list
    # store the peopple in the dict
    # first person in inner-list as key
    # second person in the inner-list as value
    for persons in trust:
        if persons[0] not in trust_dict:
            trust_dict[persons[0]] = [persons[1]]
        else:
            trust_dict[persons[0]].append(persons[1])
    
    # print(trust_dict) 
    # have set to avoid the duplicates
    spy_person_set = set()  
    for value in trust_dict.values():
        spy_person_set.add(value[0])     
    # print(spy_person_set)  
    if len(spy_person_set) == 1:
        return spy_person_set.pop()     
    #default return
    return -1   
  
print(uncover_spy(2, [[1, 2]])) # 2
print(uncover_spy(3, [[1, 3], [2, 3]])) # 2
print(uncover_spy(3, [[1, 3], [2, 3], [3, 1]])) # 3
print(uncover_spy(4, [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]])) # 3
print(uncover_spy(3, [[1, 2], [2, 3]])) # -1
