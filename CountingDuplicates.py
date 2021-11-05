def duplicate_count(text):
    newlist = []
    # characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    # print(len(["i" for i in characters if text.lower().count(i) > 1]))

    # for i in "abcdefghijklmnopqrstuvwxyz":
    #     if text.count(i) > 1:
    #         newlist.append(i)

    # for i in text.lower():
    #     if text.lower().count(i) > 1:
    #         newlist.append(i)
    print(
        len(list(dict.fromkeys([i for i in text.lower() if text.lower().count(i) > 1])))
    )

    # for i, j in enumerate(text):
    #     if j in text[i - 1 : i + 1]:
    #         newlist.append(j)

    # newlist = list(dict.fromkeys(newlist))
    # print(text)
    # print(newlist)
    # print(len(newlist))


duplicate_count("abcde")  # 0 no characters repeats more than once
duplicate_count("aabbcde")  # 2 'a' and 'b'
duplicate_count("aabBcde")  # 2 'a' occurs twice and 'b' twice (`b` and `B`)
duplicate_count("indivisibility")  # 1 'i' occurs six times
duplicate_count("Indivisibilities")  # 2 'i' occurs seven times and 's' occurs twice
duplicate_count("aA11")  # 2 'a' and '1'
duplicate_count("ABBA")  # 2 'A' and 'B' each occur twice
