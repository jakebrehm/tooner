An easier way to manage and launch sessions for multiple toons for [Toontown Rewritten](https://toontownrewritten.com).

# What does it do?

Currently, it allows you to communicate with Toontown Rewritten's login API in order to log in and start a session with very few lines of code.

```python
launcher = multitooner.ToontownLauncher(directory="...")
launcher.play(username="username", password="password")
```

If you're crazy, you can even combine these lines into one!

All you have to do is supply the directory of your Toontown Rewritten installation (where the TTREngine is stored) and your login information. On Windows, check your program files directories. On MacOS, this is in your Application Support directory. Eventually, I'd like to make this library automatically find the installation.

The best part is that you can do this to **play multiple toons at once**.

# Why does this exist?

Since I normally play on MacOS, there is no way for me to open multiple sessions of the Toontown Rewritten launcher without doing it from the terminal; this was really annoying to do every time I wanted to multitoon (which is a lot), so I set out to make this easier.

Ultimately, I was successful in making this functionality work the three major operating systems: Windows, MacOS, and, I assume, on Linux (I haven't been able to test this).

# Taking it further

I have a few project ideas that could use this functionality:
<!-- - Make a menu bar app for MacOS  -->
- Make a GUI to allow the user to store login information and start sessions for multiple toons
- Refactor the launcher module to allow for better communication with the GUI
- Send toast notifications for invasions
- If multitooning, tile windows automatically
However, they would be separate projects.

# Authors
- **Jake Brehm** - *Initial Work* - [Email](mailto:mail@jakebrehm.com) | [Github](http://github.com/jakebrehm) | [LinkedIn](http://linkedin.com/in/jacobbrehm)