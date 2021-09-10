<div align="center">

  <img src="https://github.com/jakebrehm/tooner/blob/master/img/logo.png" alt="Tooner Logo"/>

  <br>
  <br>

  <h1>An easier way to launch sessions and track invasions for Toontown Rewritten.</h1>

  <br>

  <img src="https://img.shields.io/github/last-commit/jakebrehm/tooner?style=for-the-badge&color=yellow" alt="Last Commit"></img>
  <img src="https://img.shields.io/github/commit-activity/w/jakebrehm/tooner?style=for-the-badge&color=yellow" alt="Commit Activity"></img>
  <img src="https://img.shields.io/github/license/jakebrehm/tooner?style=for-the-badge&color=yellow" alt="MIT License"></img>
  <br>
  <img src="https://img.shields.io/badge/Made%20With-Python%203.7-violet.svg?style=for-the-badge&logo=Python" alt="Made with Python 3.7"></img>

</div>

<br>

## What does it do?

Currently, **tooner** allows you to communicate with Toontown Rewritten's login API in order to log in and start a session with very few lines of code.

```python
launcher = tooner.ToontownLauncher(directory="...")
launcher.play(username="username", password="password")
```

If you're crazy, you can even combine these lines into one!

All you have to do is supply the directory of your Toontown Rewritten installation (where the TTREngine is stored) and your login information. On Windows, check your program files directories. On MacOS, this is in your Application Support directory. Eventually, I'd like to make this library automatically find the installation.

The best part is that you can do this to **play multiple toons at once**.

You are also able to **get the latest invasion information**.

```python
tracker = tooner.InvasionTracker()
invasions = tracker.invasions
```

Unfortunately, *latest* does not mean *freshest* in this case, as fresh information is pushed to the Toontown Rewritten Invasion API noticeably infrequently.

## Why does this exist?

Since I normally play on MacOS, there is no way for me to open multiple sessions of the Toontown Rewritten launcher without doing it from the terminal; this was really annoying to do every time I wanted to multitoon (which is a lot), so I set out to make this easier.

Ultimately, I was successful in making this functionality work the three major operating systems: Windows, MacOS, and, I assume, on Linux (I haven't been able to test this).

## How do I get it?

It's easiest to simply install the package via pip using the following command:

```
pip install tooner
```

Otherwise, you can close this repository using the command

```
git clone https://github.com/jakebrehm/tooner.git
```

and then you can do whatever you want with it!

## Future improvements

My two main concerns and top priorities for this package are the following:

- **Automatically finding the directory,** or at least try. I imagine users should still be able to supply their own directory if they know the program is installed in a non-default location. This would further (and possibly significantly) simplify the usage of the package, and would allow for a one-line launcher.
- **Adding support for ToonGuard**. The only problem is writing it in such a way that makes sense while keeping in mind *tooner*'s two-line launcher paradigm, as it would require the user to enter a code *after* having run the script.
- **Make invasion functions**. Instead of having to make a class and keep track of it, some basic functions to encapsulate the class would be useful and easy to implement.

## Projects using **tooner**

The following projects are using **tooner**:
1. [MultiTooner](https://github.com/jakebrehm/multitooner) by [Jake Brehm](https://github.com/jakebrehm)

## Authors

- **Jake Brehm** - *Initial Work* - [Email](mailto:mail@jakebrehm.com) | [Github](http://github.com/jakebrehm) | [LinkedIn](http://linkedin.com/in/jacobbrehm)