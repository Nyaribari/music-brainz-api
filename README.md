*MUSIC BRAINZ API*

The goal of this exercise is to write a web service with the following specs:
- You need to work with the MusicBrainz API.
(https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2).

- Given an artist MusicBrainz Id (e.g. 65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab), the service
returns a list of release-groups of type Album and the number of releases in each release-group. (A release is something you can buy as media, such as a CD or a vinyl record, while a release group embraces the overall concept of an album).

- The service should give the possibility to paginate results. It should support 'offset' and
'limit'. The default limit is 50 and it can be increased up to 150.

- The service should return a JSON object.
- You can implement this prototype using a programming language of your choice, as long as it is free and available on GNU/Linux.

- Paying attention to concurrency and scalability issues will be valued.
- Installing notes and instructions on how to run your code is required.
- Be careful with the API request limits of MusicBrainz.


**SOLUTION**

**The code is in the musicbrainz_api_func.py** 

First, make sure you have **requests** installed with **pip install requests and python 3.6+ (I used python 3.9)**

The function is run as a python file. 

In terminal **run python musicbrainz_api_func.py** or  if you using an IDE run it.

In the terminal you will prompted with inputs and you will be asked to enter the values.

Enter limit value:(enter int value of your choice)

Enter offset value:(enter int value of your choice)

Enter artist id:(enter the artist id)

**The limit is for pagination, from the required 50 to 150, more or less.**