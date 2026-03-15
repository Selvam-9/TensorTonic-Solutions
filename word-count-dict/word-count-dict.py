def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    sent = []
    output = sent
    cnt = dict()
    for i in sentences:
        for l in i:
            sent.append(l)
    for i in sent:
        if i not in cnt:
            cnt.update({i:1})
        elif i in cnt:
            cnt.update({i:cnt[i]+1})
    return cnt
    pass