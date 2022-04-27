# daemonify
Daemonifies a program to run under systemd.

This is done by simply adding an entry to the systemd's system folder.
The entry is populated with the settings that you provide.

I wrote this script to save me some boilerplate on a server once, then I realized that I missed it on other machines. 
Hence, why I've started this repo.

## Requirements

You must have python3 installed.
You must have root privileges to access systemd. 

## Usage

```
Usage: python main.py <executable> <arguments>
```

Run the `main.py`-script using python3 (if you prefer, save it some where on your `path` as `daemonify` and run it by that name) with the following arguments:

- `<executable>` The path to your executable.

- `<arguments>` Any arguments that you want to pass along to your executable. You don't have to provide any.

The program then asks you whether you would like the daemon to restart automatically.

And then you're done.

## Note

You could perform the same task in a simple shell script or by hand, but I find that it's nice to have a little utility I can call.
