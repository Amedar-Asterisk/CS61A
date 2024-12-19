from cats import minimum_mewtations, furry_fixes, autocorrect, lines_from_file

all_words = lines_from_file("data/words.txt")
common_words = lines_from_file("data/common_words.txt")
print(len(common_words))
minimum_mewtations.call_count = 0
autocorrect("woll", common_words, minimum_mewtations, 4)
minimum_mewtations.call_count
minimum_mewtations.call_count = 0
print(minimum_mewtations.call_count)
autocorrect("woll", common_words, minimum_mewtations, 4)  # identical to the first call
minimum_mewtations.call_count
print(minimum_mewtations.call_count)
