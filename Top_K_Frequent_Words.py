import heapq
from collections import Counter

def top_k_frequent_words(words, k):
    word_count = Counter(words)
    heap = [(-count, word) for word, count in word_count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]

# Test the function
words = ["i", "love", "leetcode", "i", "love", "coding"]
print(top_k_frequent_words(words, 2))



import heapq
from collections import Counter

def top_k_frequent_words(words, k):
    word_count = Counter(words)
    heap = [(-count, word) for word, count in word_count.items()]
    heapq.heapify(heap)
    
    # Sort the heap
    sorted_heap = sorted(heap)
    
    return [heapq.heappop(sorted_heap)[1] for _ in range(k)]

# Test the function
words = ["the", "day", "is", "sunny", "the", "the", "sunny", "is", "is"]
k = 4
print(top_k_frequent_words(words, k))  # Output: ['day', 'sunny', 'is', 'the']