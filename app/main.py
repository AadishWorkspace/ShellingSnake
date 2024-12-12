import sys
import os
import subprocess

def file_search(command: str, directories: list[str]) -> str:
    cmd_path = None
    for directory in directories:
        if os.path.exists(os.path.join(directory, command)):
            cmd_path = os.path.join(directory, command)
            break
    return cmd_path



def main():
    valid_commands = ['exit', 'echo', 'type', 'pwd']
    path = os.environ.get("PATH")

    directories = path.split(os.pathsep)

    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        user_input = input()

        individual_commands = user_input.split(' ')

        if individual_commands[0] in valid_commands:
            if individual_commands[0] == 'exit':
                return 0
            elif individual_commands[0] == 'echo':
                print(' '.join(individual_commands[1:]))
            elif individual_commands[0] == 'type':
                if len(individual_commands) < 2:
                    print('type: missing argument')
                    continue
                cmd_path = file_search(individual_commands[1], directories)
                if individual_commands[1] in valid_commands:
                     print(f'{individual_commands[1]} is a shell builtin')
                elif cmd_path:
                    print(f'{individual_commands[1]} is {cmd_path}')
                else:
                    print(f'{individual_commands[1]}: not found')
            elif individual_commands[0] == 'pwd':
                print(os.getcwd())

        else:
            cmd_path = file_search(individual_commands[0], directories)
            if cmd_path:
                subprocess.run([cmd_path] + individual_commands[1:])

            else:
                print(f'{user_input}: command not found')


if __name__ == "__main__":
    main()
