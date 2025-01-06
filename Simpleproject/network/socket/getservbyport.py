from socket import getservbyport

# Open a file for writing
with open("servport.txt", 'w') as file:
    for i in range(100):
        try:
            # Get the service name for port i
            service = getservbyport(i)
            # Write the service name and port number to the file
            file.write(f"{service} : {i}\n")
        except Exception as e:
            pass  # Ignore errors in case there is no service for the port
