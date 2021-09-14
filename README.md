Motivational-Meme-Generator

Meme Generator is a multimedia application to dynamically generate memes, which includes an image with an overlaid quote. It is a dynamic data - rich application. It is primarily focused on data engineer and full - stack roles in Python development.

This application does the following:

Interacts with a variety of complex filetypes.
Load quotes from a variety of filetypes (CSV, Docx, PDF, Text files)
Load, manipulate and save images
Accept dynamic user input through a command-line tool and a web serive.
Libraries

requests
python - docx
pandas
pillow
flask
PDF file handling

The app uses the subprocess module for the purpose of converting data from PDF to Txt format. Firstly, pdftotext needs to be installed on Mac or Windows. For this xpdf should be downloaded using here. For Mac, run brew install pkg-config poppler python and then pip install pdftotext

Project Interface

The project should be in the correct virtual environment before running it. Pass the command source env/bin/activate. This will activate the environment.

There are two ways of running this project:

Running on the command line - python3 meme.py. For getting more information you could run python meme.py --help which will provide further explanation.

(env) (base) Garys-MacBook-Air:Motivational-Meme-Generator gary$ python3 meme.py --help
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

Generate meme....

optional arguments:
 -h, --help       show this help message and exit
--path PATH      Path for the image file
--body BODY      Quote for the image
--author AUTHOR  Author of the quote
Example of how to use generate meme via - meme.py (CLI)

(env) (base) Garys-MacBook-Air:Motivational-Meme-Generator gary$ python3 meme.py --body "Cute dog" --author  "Gary"
Image saved to ./tmp/tmp-1614979852.763993.png.
./tmp/tmp-1614979852.763993.png
Through this way, the meme will be generated in tmp directory. The parameters are optional. If no parameter is passed then a random meme will be generated.

Running the project in the app - python3 app.py and go to the link

(env) (base) Garys-MacBook-Air:Motivational-Meme-Generator gary$ python3 app.py
* Serving Flask app "app" (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
The app will use QuoteEngine module and Meme Generator module which will generate the meme with a random quote. It will use requests package to fetch an image which the user submits.

Modules description

The structure of the project:

The QuoteEngine module is responsible for ingesting various file types which contain the quotes. It contains many classes and showcases inheritance, abstract classes, classmethods, strategy objects.

The MemeEngine module is responsible for the resizing, cropping and drawing text on the images for the memes.

Dependencies can be installed by running pip install -r requirements.txt
For the Web app - some default memes and images will be made. The user also has the option to create his/her own meme by specifying the image url, quote and author. Enjoy!!
For the CLI - the meme created will be stored in static directory.
