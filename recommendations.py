from math import sqrt
critics = {'Lisa': {'Lady': 2.5, 'Snake': 3.5, 'Luck':3.0, 'Superman': 3.5,
'Dupree': 2.5, 'Night': 3.0},
'Gene': {'Lady': 3.0, 'Snake': 3.5, 'Luck':1.5, 'Superman': 5.0, 'Night': 3.0,
    'Dupree': 3.5},
'Michael': {'Lady': 2.5, 'Snake': 3.0, 'Superman': 3.5, 'Night': 4.0},
'Claudia': {'Snake': 3.5, 'Luck': 3.0, 'Night': 4.5, 'Superman': 4.0, 'Dupree':
    2.5},
'Mick': {'Lady': 3.0, 'Snake': 4.0, 'Luck': 2.0, 'Superman': 3.0, 'Night': 3.0,
    'Dupree': 2.0},
'Jack': {'Lady': 3.0, 'Snake': 4.0, 'Night': 3.0, 'Superman': 5.0, 'Dupree':
    3.5,},
'Toby': {'Snake': 4.5, 'Dupree': 1.0, 'Superman': 4.0}}

def sim_pearson(prefs, p1, p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1

    n = len(si)

    # no common
    if n == 0: return 1
    
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    sum1sq = sum([pow(prefs[p1][it],2) for it in si])
    sum2sq = sum([pow(prefs[p2][it],2) for it in si])

    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1sq - pow(sum1,2)/n) * (sum2sq-pow(sum2,2)/n))
    if den == 0: return 0
    
    r = num/den
    return r

def sim_distance(pref, person1, person2):
    flag = 0
    for item in pref[person1]:
        if item in pref[person2]:
            flag = 1

    if (flag == 0):
        print pref[person1]
        print pref[person2]
        return 0

    sum_of_sq = sum([pow(pref[person1][item] - pref[person2][item],2) for item
        in pref[person1] if item in pref[person2]])
    return 1 / (1 + sqrt(sum_of_sq))

def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs,person, other), other) for other in prefs if
            other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    sumSims = {}
    for other in prefs:
        if (other == person) : continue
        sim = similarity(prefs, other, person)
        for item in prefs[other]:
            if item in prefs[person] : continue
            totals.setdefault(item, 0)
            totals[item] += sim * prefs[other][item]
            sumSims.setdefault(item, 0)
            sumSims[item] += sim

    recommendations = [(totals[item] / sumSims[item], item) for item in totals]
    recommendations.sort()
    recommendations.reverse()
    return recommendations

def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            result[item][person] = prefs[person][item]

    return result



def main():
    print sim_distance(critics, 'Lisa', 'Gene')
    print sim_pearson(critics, 'Lisa', 'Gene')
    print topMatches(critics, 'Toby', n=3)
    print getRecommendations(critics, 'Toby')
    print getRecommendations(critics, 'Toby', sim_distance)
    movies = transformPrefs(critics)
    print topMatches(movies, 'Superman')

if __name__ == "__main__":
    main()

