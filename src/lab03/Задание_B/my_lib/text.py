def count_freg(tokens: list[str]) -> dict[str, int]:
    from collections import Counter

    
    return dict(Counter(tokens)) # считаем частоты элементов 



def tokenize(text: str) -> list[str]:
    import re
    

    p = r'\w+(?:-\w+)*'
    tokens = re.findall(p, text) # проверяем совпадения в нашей строке и возвращаем их список
    return tokens

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    my_list = list(freq.items())

    def sort_po_alfavity(key_v):
        return key_v[0]
    my_list.sort(key=sort_po_alfavity)

    def sort_po_num(key_v):
        return key_v[1]
    my_list.sort(key=sort_po_num, reverse=True)

    return my_list[:5]

