#Q. Write a program to fill in a letter template given below with name and date.
name = 'Roy'
date = '08/4/2025'

letter = '''
  Dear Name,\n
  You are selected!\n
  <|Date|>
        '''

print(letter.replace("Name",name).replace("<|Date|>",date))