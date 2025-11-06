count_freq_and_top_n = [
    ["a","b","a","c","b","a"],
    ["bb","aa","bb","aa","cc"],
]

def count_freg(tokens: list[str]) -> dict[str, int]:
    from collections import Counter

    
    return dict(Counter(tokens)) # считаем частоты элементов 

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    my_list = list(freq.items())

    def sort_po_alfavity(key_v):
        return key_v[0]
    my_list.sort(key=sort_po_alfavity)

    def sort_po_num(key_v):
        return key_v[1]
    my_list.sort(key=sort_po_num, reverse=True)

    return my_list[:n]


for tokens in count_freq_and_top_n:
    freq_dict = count_freg(tokens) 
    print(f"Частоты: {freq_dict}")
    print(f"Топ: {top_n(freq_dict)}")  
    