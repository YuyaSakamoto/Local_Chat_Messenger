import os
pid = os.fork()
# pidが０より大きい場合、親プロセス
if pid > 0:
    print("Fork above 0, PID:", os.getpid())
    print("Spawned child's PID:", pid)
# pidが0の場合、子プロセス
else:
    print("Fork is 0, this is a child PID:", os.getpid())
    print("Parent PID:", os.getppid())