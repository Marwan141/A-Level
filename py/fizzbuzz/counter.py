stri = "BRXFD QQRWO RVHDK RPLQJ SLJHR Q.LIB RXUKR PLQJS LJHRO GRHVO RWFRP HEDFN ,WKHQ ZKDWB RXKDY HORVW LVDSL JHRQ."
count = 0

letter = input("Input the letter: ")
for i in stri:
    if i == letter:
        count += 1

print(count)