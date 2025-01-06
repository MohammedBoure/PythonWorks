import subprocess

def run_python_file(file_name):
    try:
        subprocess.Popen(['python', file_name])
    except Exception as e:
        pass
run_python_file('main.py')
run_python_file('hiden_icon.py')
 
