# Text Adventure - Descent of the Cullodens
## Chapter 3 - I’d Kill You If I Had My Gun!

This game makes use of the [Adventurelib](https://adventurelib.readthedocs.io/en/stable/) Python library.

Source: [PDF](https://drive.google.com/file/d/1flH5tXNHh-ks1RYCTHMwxx8EgXRroGiM/view)

Link: [Escape This Podcast (S04E03)](http://www.escapethispodcast.com/e/descent-of-the-cullodens-chapter-3-id-kill-you-if-i-had-my-gun-ft-triple-jeopardy-lee-amy-and-alistair/)


## To play

```
python3 ./run.py
```

## For debugging

You can also run in debug mode to get actual error messages when something goes wrong:

```
python3 ./run.py --debug
```

## Using Docker

This project also includes a Dockerfile. Use run it using Docker, use the following commands:

```
docker build -t escape-room .
docker run -it escape-room
```