from collections import defaultdict

# O(m * n); m = total number of strings, n = average number of character in a single string
def group_anagram(strs):
    # key = count of alphabets in each str (eg: 1e, 1a, 1t)
    # value = list of anagrams that matches the key

    res = defaultdict(list)  # map charCount to list of Anagrams

    for s in strs:
        count = [0] * 26  # a ... z
        for c in s:
            # a = 0, b = 1, .. z = 25
            # ord = ascii value
            count[ord(c) - ord("a")] += 1
            # a = 80 -> 0, 80 - 80
            # b = 81 -> 1, 81 - 80

        # append the string into the dict where key is charcount
        # tuple to make it immutable
        res[tuple(count)].append(s)

    return res.values()


print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
