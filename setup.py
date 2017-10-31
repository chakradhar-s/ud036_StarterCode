from setuptools import setup

#I have taken reference from https://chriswarrick.com/listings/entry_points_project/setup.py.html for this piece of code
setup(name='movie trailer website',
      version='0.0.2',
      packages=['movie_trailer'],
      entry_points={
          'console_scripts': [
              'movie_trailer = movie_trailer.entertainment_center:main'
          ]
          },
      )
