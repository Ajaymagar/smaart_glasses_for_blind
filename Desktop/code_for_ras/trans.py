from textblob import TextBlob
input_str = input('\n enter the string:')
textblob_obj = TextBlob(input_str)
detectLanguage = textblob_obj.detect_language()
print('\n detected language',detectLanguage)



input_string = input('\n enter the text')

textblob_obj_2 = TextBlob(input_string)
arabic_op = textblob_obj_2.translate(to='ar')


print('\n ip string is converted into arabic_op:',arabic_op)


china_corona = textblob_obj_2.translate(to='zh-CN')
print('\n ip string is converted into china_corona:',china_corona)

french_op = textblob_obj_2.translate(to='fr')
print('\n ip string in french:',french_op)

greekop = textblob_obj_2.translate(to='el')
print('\n ip is converted to greek',greekop)

hindi_op = textblob_obj_2.translate(to='hi')
print('\n ip is converted into hindi',hindi_op)

