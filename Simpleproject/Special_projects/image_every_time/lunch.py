import subprocess

def run(file_name):
    try:
        subprocess.Popen(['python', file_name])
    except:
        pass

run('test4.py')

