# tripTo

Simple script added to Windows menu for easy access by one button

![image](https://user-images.githubusercontent.com/42386993/49665655-35209e00-fa5e-11e8-8f60-897b724ea3e6.png)

## Just push Windows button and type tripTo + place you prefer to visit
## Location can be entered from clipboard as well. 
In this case it is enough to type tripTo and hit enter

Default browser will open new windows with usefull info. In my case it opens:

```
webbrowser.open('https://www.google.com/maps/place/' + word) - shows place on map
webbrowser.open('https://www.google.com/search?q=' + word + ' things to do') - finds things to do
webbrowser.open('https://www.google.com/search?q=' + word + ' hotel') - finds hotels
webbrowser.open('https://www.google.com/search?q=' + word + ' flight') - finds flights
```

## How to install

You need to copy tripTo.py and tripTo.bat files to your PC.
Add this location to your System Variables-> Path

![environment variables](https://user-images.githubusercontent.com/42386993/49666586-343d3b80-fa61-11e8-92e3-a0a4a38a351a.JPG)

You need to modify tripTo.bat file by adding to it location you stored tripTo.py and tripTo.bat
```py
@py.exe C:\\...\\MyPythonScripts\\tripTo.py %*
```
## How to modify code

Just open tripTo.py and modify/add lines

```py
webbrowser.open('https://www.google.com/maps/place/' + word)
webbrowser.open('https://www.google.com/search?q=' + word + ' things to do')
webbrowser.open('https://www.google.com/search?q=' + word + ' hotel')
webbrowser.open('https://www.google.com/search?q=' + word + ' flight')
```

