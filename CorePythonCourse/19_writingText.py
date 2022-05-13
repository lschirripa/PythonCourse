# in text mode, write and read option returns number of characters written or readed, not bytes. (all this in repl)

f = open('test.txt',mode='wt', encoding='utf-8')

f.write('this is a test!! :) \n')
f.write('before this test must be an endline \n')
f.write('and before this too')

f.close()