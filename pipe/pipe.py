import os
# os.pipe(): 2つのファイル記述子（read only, write only）をタプルで返す
# r: read only , w: write only
r, w = os.pipe()
pid = os.fork()

if pid > 0:
    # This is a parent process
    print("Parent PID:", os.getpid())
    print("Child PID:", pid)
    # parent process is write only
    os.close(r)
    # Spawn message from parent process
    message = 'Message from parent with pid {}'.format(os.getpid())
    # Show the spawned message
    print("Parent, sending out the message - {}".format(message, os.getpid()))
    # encode the spawned message to write a pipe
    os.write(w, message.encode('utf_8'))

else:
    # This is a child process
    print("Parent PID:", os.getppid())
    print("Fork is 0,Child PID:", os.getpid())
    # child process is read only
    os.close(w)
    # open a read only file descriptor
    f = os.fdopen(r)
    # show a read message from pipe
    print("Incoming string:", f.read())