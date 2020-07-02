def getScore(text):
    text = text.lower()
    text = re.sub("[^a-z]", "", text)
    d = defaultdict(int)
    for c in text:
        d[c]+=1
    counts = sorted([v for k,v in d.items()],reverse=True)
    scores = range(26,0,-1)
    return sum([i*j for i,j in zip(counts,scores)])



