from typing import List, Tuple
from pypinyin import lazy_pinyin

expansions_text: List[str] = ["expansions.txt", "expansions-zh.txt"]

for eps_txt in expansions_text:

    print("Start to sort", eps_txt)

    expansions_list: List[Tuple[str, str]] = []

    with open(eps_txt, "r", encoding="utf-8") as f:
        expansions_list = [
            (line.strip(), "".join(lazy_pinyin(line, style=2)).upper())
            for line in f.readlines()
        ]

    expansions_list.sort(key=lambda x: x[1])

    with open(eps_txt, "w", encoding="utf-8") as f:
        f.write("\n".join([line[0] for line in expansions_list]))

    print("Done")

print(" - All Done - ")
