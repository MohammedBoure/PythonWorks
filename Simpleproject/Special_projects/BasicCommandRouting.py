import subprocess

#desired_directory = r"C:\pythonProject\pythonProject"

def execute_command_in_cmd(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, errors = process.communicate()
        if process.returncode != 0:
            return(f"errors : {errors.decode('latin1')}")
        else:
            return(f"message1 : \n{output.decode('latin1')}")
    except Exception as e:
        return (f"-------{e}")
