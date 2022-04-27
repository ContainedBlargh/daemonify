#!/usr/bin/python3
from sys import argv
from os import geteuid, getcwd, system

def yes_or_no(prompt: str) -> bool:
    user_input = input(f"{prompt}\n\n\t(y/n) > ").lower()
    if user_input not in ["y", "n", "yes", "no"]:
        return False
    else:
        return user_input == "y"

def main(args):
    if len(args) < 2:
            print(f"Usage: {args[0]} <executable> <arguments>\nDaemonifies a program to run under systemd.")
            return
    if geteuid() != 0:
            print(f"You need to have root privileges to create systemd services!")
            return

    name = args[1]
    arguments = []
    arguments_str = ""
    if len(args) > 2:
        arguments = args[2:]
    if len(arguments) > 0:
        arguments_str = arguments.join(" ")
    arguments_str = " " + arguments_str
    restart = yes_or_no("Would you like the service to restart automatically?")
    restart_str = "always" if restart else "never"

    with open(f"/etc/systemd/system/{name}.service", "w") as fp:
        fp.write(
f"""
[Unit]
Description={name}

[Service]
ExecStart={getcwd()}/{name}{arguments_str}
Restart={restart_str}

[Install]
WantedBy=multi-user.target
"""
        )
    output = system(f"systemctl daemon-reload; systemctl enable {name}; systemctl status {name}")
    print(output)
    pass

main(argv)
