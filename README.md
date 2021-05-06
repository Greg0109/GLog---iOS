# GLog - Logging system for iOS

This is GLog, a new logging system for iOS that allows you to debug your code in an easy and comfortable way. Just place the files where needed, start the logger with the computer ip, log your code and start the server on the computer side and done.

## Built With

- Python
- Objective-C

## Getting Started

First ensure you have python installed on your PC and that the logging system is setup on the iOS side

## Prequisites

Python installed on the machine
Terminal or similar to launch and see the server data

## Install

Download a copy of the repository

## Usage

In your project, import your files properly and set it up like so

```#import "GLog.h"```

```GLog *log = [[GLog alloc] initWithIP:@"place-computer-ip-or-hostname-here"];```

```[log sendLog:@"Your logs"];```

If you are using this with an iOS tweak, you also need to add it to the makefile

```TweakName_FILES = Tweak.x GLog.m```

In your pc, just start the server in terminal like so

```python3 GLogServer.py```

## Authors

👤 Gregorio Rábago Sainz

- GitHub: [@Greg0109](https://github.com/greg0109)
- Twitter: [@Greg_0109](https://twitter.com/greg_0109)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/greg0109/glog/issues).

## Show your support

Give a ⭐️ if you like this project!
