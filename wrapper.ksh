import subprocess
import time
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")



message = """

 Demo setup: We've created a RHEL server instance on AWS for demonstration purposes.


 Access method: The RHEL server is accessed using a User Interface provided by the open-source software Cockpit and AWS security policies.


 Command conversion: Natural language instructions are converted into Linux commands with the help of ChatGPT API, using just 20 lines of code.


 Customization: You can create and train your own model to achieve similar output tailored to your specific needs.


"""

print(message)

time.sleep(20)

clear_screen()

instructions = [
"Show me the current directory.",
"List all files and folders in the current directory.",
"List all files and folders but only the hidden ones.",
"Show the contents of a file called readme.txt.",
"how many dml files are available  under the /home/admin/dml folder. display the count and file names",
"search for a keyword policy under the /home/admin/dml folder. display matching occurence",
"list all files updated in the last 12 hrs in the current folder and its subdirectories",
"Show the disk usage of the current directory.",
"Show the available disk space on the system.",
"show the top 10 files consuming most space",
"display current date and time.",
"list all the log files under /home/admin/log folder. also display error remarks encountred in the log files",
"Show the detailed information about the system's hardware.",
"Show the kernel version and system information.",
]



def execute_software(instruction):
    try:
        output = subprocess.check_output(["python", "software.py", instruction], text=True)
        print(f"Output:\n{output}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}\n{e.output}")


for index, instruction in enumerate(instructions, start=1):
    print(f"Executing instruction {index}): {instruction}")
    print("\n")
    execute_software(instruction)
    time.sleep(5)
    clear_screen()




