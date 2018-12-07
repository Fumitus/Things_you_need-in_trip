import webbrowser, sys, pyperclip

sys.argv #['trip.py', 'place', 'hotel', 'name']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['trip.py', 'place', 'hotel', 'name'] -> 'place hotel name'
    word = ' '.join(sys.argv[1:])
else:
    word = pyperclip.paste()
# https://translate.google.com/#en/lt/<WORD>
webbrowser.open('https://www.google.com/maps/place/' + word)
webbrowser.open('https://www.google.com/search?q=' + word + ' things to do')
webbrowser.open('https://www.google.com/search?q=' + word + ' hotel')
webbrowser.open('https://www.google.com/search?q=' + word + ' flight')
