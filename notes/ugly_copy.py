"""
Contains get_beauty_score function
"""
from collections import defaultdict
import re


def get_beauty_score(text):
    """
    Calculates beauty score for input text, only counts letters
    26 for most frequent letter, 25 for next frequent, etc.
    :return: Beauty score
    :rtype: int
    """
    text = text.lower()
    text = re.sub("[^a-z]", "", text)
    count_dict = defaultdict(int)
    for character in text:
        count_dict[character] += 1
    counts = sorted([v for k, v in count_dict.items()], reverse=True)
    scores = range(26, 0, -1)
    return sum([i * j for i, j in zip(counts, scores)])
