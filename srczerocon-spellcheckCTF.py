import socket
import sys
from spellchecker import SpellChecker

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('bookworm.threatsims.com', 8008)
print('starting up on %s port %s' % server_address)
sock.connect(server_address)

spell = SpellChecker()
substring = "Word: "
OriginalWord = ""
NewWord=""
look = "_"
data = str(sock.recv(4096), 'utf-8')
counter = 0
while data:
    
    if counter == 1000:
    	print(data)
    	data = (str(sock.recv(2050), 'utf-8'))
    cuf = (data.split())
    
    for list_index in range(0, len(cuf)):
    	list_item = cuf[list_index]
    	if '_' in list_item:
    		OriginalWord= str(list_item)
    		print(OriginalWord)
    		NewWord = spell.correction(OriginalWord)
    		print(NewWord)
    		xx = OriginalWord.find(look)
    		missing = (NewWord[xx])
    		print (missing)
    #print(cuf[5])
    		sock.send(missing.encode())
    		print("count: "+ str(counter))
    		counter= counter+1
    		
    
    #print(data)
    data = (str(sock.recv(2050), 'utf-8'))
    print (data)
    print("\n\n")


sock.close()
exit()
