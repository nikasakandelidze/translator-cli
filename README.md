# Terminal Translator program
I bumped upon the problem of overhead when trying to translate some words i couldn't understand from English to my native language Georgian. I am creating this app to avoid this overhead associated with it.
cli-translator is a command line interface program which uses some web HTTP api-s under the hood to translate words from SOURCE to TARGET languages.
At the moment it only supports from English ---> Georgian translation, but the code is written in a way to be able to easily  add as many language features as possible and wanted.

# Current Features
- Translate words from english to georgian snap fast
- Auto correct misspelled words and find correct translations:
	-  if you issue command `translate grotasque` app will display message: " Spelling of 'grotasque' is not correct. Autocorrecting it to 'groteqsue'. 

# Usage
Usage of the application is two step process:
- Setup
- Run
### Setup
To install all the dependencies run: `pip install -r requirements.txt`
### Run
Currently the most useful way i found myself using thi cli is by using it for "One shot translation".
Example:
- python path/to/main.py grotesque 
and it returns several contextual results in georgian.

Since its pain in the XXX to every time locate to the main.py in the hirerchy of your computers folders i on my pc ( MAC ) created an alias in shell profile to map custom translate command to it:
- For python3 and zshell(MAC) `echo "alias translate=python3 path/to/src/main.py" >> ~/.zshrc`
- For python3 and bash(Ubuntu) `echo "alias translate=python3 path/to/src/main.py" >> ~/.bashrc`
- For python and zshell(MAC) `echo "alias translate=python path/to/src/main.py" >> ~/.zshrc`
- For python and bash(Ubuntu) `echo "alias translate=python path/to/src/main.py" >> ~/.bashrc`
After executing one of the commands restart the terminal session( close and reopen it ) and now you can use translator simply in a next way:
- translate WORD_IN_ENGLISH

# Technical details
Application uses clearly seperated layers and modules following mostly clean architecture.

### Architecture
![Architecture diagram](./assets/architecture.jpeg)

Architecture used in this app is described pretty fully in the diagram. Basic idea is that there is core package/module which doesn't have any dependency on any concrete implementation module or library except core python.
There are thee main parts/modules of the program at the moments: Core, Adapters, Presenter
- Core module encapsulates business logic of the application, without any dependencies on implementation details like web, http, concrete data storage, etc.
  Core module depends on abstract adapters and presenters ( simply like abstract classes/interfaces in typed languages ).
  This way, when core business logic is not dependant on specific implementations of different parts of the program we can easily updates code.
-  Adapters encapsulate logic associated with some third party libraries and implementation details. 
   For example, Adapter module encapsulates we have translation adapter, which has one specific implementation web_translation_adapter, this implementation translated using the web, 
   later we might add another implementation of translation_adapter which will use local db or something else.
- Presenter is module with responsibility to interact with user layer, showing data to them and fetching data from them as inputs to the system. At the moment we have speecific implementation of presenter called CliPresenter, which uses
command line interface to interact with user. 
  Since core business logic isn't dependant upon specific implementation of presenter we can later switch cli presenter layer to REST web presenter and return and fetch data from users using HTTP.
