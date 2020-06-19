An easier way to manage and launch sessions for [Toontown Rewritten](https://toontownrewritten.com).

# What does it do?

Currently, **tooner** allows you to communicate with Toontown Rewritten's login API in order to log in and start a session with very few lines of code.

```python
launcher = tooner.ToontownLauncher(directory="...")
launcher.play(username="username", password="password")
```

If you're crazy, you can even combine these lines into one!

All you have to do is supply the directory of your Toontown Rewritten installation (where the TTREngine is stored) and your login information. On Windows, check your program files directories. On MacOS, this is in your Application Support directory. Eventually, I'd like to make this library automatically find the installation.

The best part is that you can do this to **play multiple toons at once**.

# Why does this exist?

Since I normally play on MacOS, there is no way for me to open multiple sessions of the Toontown Rewritten launcher without doing it from the terminal; this was really annoying to do every time I wanted to multitoon (which is a lot), so I set out to make this easier.

Ultimately, I was successful in making this functionality work the three major operating systems: Windows, MacOS, and, I assume, on Linux (I haven't been able to test this).

# How do I get it?

It's easiest to simply install the package via pip using the following command:

```
pip install tooner
```

Otherwise, you can close this repository using the command

```
git clone https://github.com/jakebrehm/tooner.git
```

and then you can do whatever you want with it!

# Future improvements

The most pressing major improvement that could be made is **adding support for ToonGuard**. The only problem is writing it in such a way that makes sense while keeping in mind *tooner*'s two-line launcher paradigm, as it would require the user to enter a code *after* having run the script.

# Projects using **tooner**

The following projects are using **tooner**:
1. [MultiTooner](https://github.com/jakebrehm/multitooner) by [Jake Brehm](https://github.com/jakebrehm)

# Authors

- **Jake Brehm** - *Initial Work* - [Email](mailto:mail@jakebrehm.com) | [Github](http://github.com/jakebrehm) | [LinkedIn](http://linkedin.com/in/jacobbrehm)