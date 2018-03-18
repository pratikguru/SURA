import os, subprocess, time

//Replace address bar with correct object file location.
//Python GUI to engine listening protocol.

talk_to_me = subprocess.Popen("/home/prateek/Desktop/mate2k17/yadda.o", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

def put(command):
    print('you:\n\t'+command)
    talk_to_me.stdin.write(command +'\n')

def getData():
    talk_to_me.stdin.write('isready\n')
    print('nengine: ')
    while True:
        text = talk_to_me.stdout.readline().strip() 
        if text == 'readyok':
            break
        if text !=' ':
            print ('\t' + text)


put('1')
getData()
