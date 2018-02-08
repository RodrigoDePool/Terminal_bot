import subprocess
from time import sleep
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read




class BashTerminal:
    def __init__(self):
        # Open terminal process    
        self.process = subprocess.Popen(["/bin/bash"],stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE);

        # Set stdout (of the terminal) to non block reading 
        # set the O_NONBLOCK flag of p.stdout file descriptor:
        flags = fcntl(self.process.stdout, F_GETFL)              # get current p.stdout flags
        fcntl(self.process.stdout, F_SETFL, flags | O_NONBLOCK)  # set flag

    # Executes a Bash command in the terminal previously opened and return its stdout
    # in case of malformed command the terminal will close and a new one will be 
    # executed.
    def ex_command(self, command):
        try: 
            self.process.stdin.write(command+"\n");
            sleep(0.1);                         # Time for the terminal to write into pipe
            try:
                return self.process.stdout.read();    # We try to read, if empty throws an exception
            except:
                return "";
        except:                                 # syntax error => broken pipe => new terminal opened
            # Open new terminal
            self.process = subprocess.Popen(["/bin/bash"],stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE);
            # Non-blocking reading
            flags = fcntl(self.process.stdout, F_GETFL) # get current p.stdout flags
            fcntl(self.process.stdout, F_SETFL, flags | O_NONBLOCK)
            return "ERROR: COMANDO MAL FORMADO.\nAbriendo nueva terminal:"