def my_coding(text,tbl1,tbl2):
    tcode=''
    for ch in text:
        tcode += tbl2[tbl1.find(ch)]
    return tcode

codetable_from = input()
codetable_to = input()
line_for_coding = input()
line_for_decoding = input()
print(my_coding(line_for_coding,codetable_from,codetable_to))
print(my_coding(line_for_decoding,codetable_to,codetable_from))
    