An easier way to manage and launch sessions for multiple toons for [Toontown Rewritten](https://toontownrewritten.com).

# What does it do?

Currently, it allows you to communicate with Toontown Rewritten's login API in order to log in and start a session with very few lines of code.

```
launcher = multitooner.ToontownLauncher(directory="TTREngine.exe")
launcher.play(username="username", password="password)
```

If you're crazy, you can even combine these lines into one!

The best part is that you can do this to **play multiple toons at once**.

# Why does this exist?

Since I normally play on MacOS, there is no way for me to open multiple sessions of the Toontown Rewritten launcher without doing it from the terminal; this was really annoying to do every time I wanted to multitoon (which is a lot), so I set out to make this easier.

Unfortunately, I couldn't find a way to start the Toontown Rewritten engine (*TTREngine.exe* on Windows) on MacOS, so I had to give up on that dream for now. I was, however, successful in making this functionality work on Windows and, I assume, on Linux.

# Future plans for this project

- Make a GUI to allow the user to store login information and start sessions for multiple toons
- Send toast notifications for invasions
- If multitooning, tile windows automatically
- Find a way to make the login functionality work correctly on Mac

# Authors
- **Jake Brehm** - *Initial Work* - [Email](mailto:mail@jakebrehm.com) | [Github](http://github.com/jakebrehm) | [LinkedIn](http://linkedin.com/in/jacobbrehm)