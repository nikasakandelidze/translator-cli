# Terminal Translator program
I bumped upon the problem of overhead when trying to translate some words i couldn't understand from English to my native language Georgian. I am creating this app to avoid this overhead associated with it.
cli-translator is a command line interface program which uses some web HTTP api-s under the hood to translate words from SOURCE to TARGET languages.
At the moment it only supports from English ---> Georgian translation, but the code is written in a way to be able to easily  add as many language features as possible and wanted.

# Current Features
- Translate words from english to georgian snap fast
- Auto correct misspelled words and find correct translations. Like: if you issue command `translated grotasque` app will display message Spelling of "grotasque" is not correct. Autocorrecting it to "groteqsue" 

# Usage
Currently the most useful way i found myself using thi cli is by using it for "One shot translation".
Example:
- python path/to/main.py grotesque 
and it returns several contextual results in georgian.
Since its pain in the XXX to every time locate to the main.py in the hirerchy of your computers folders i on my pc ( MAC ) created an alias in shell profile to map custom translate command to it.

Example:
- For python3 and zshell(MAC) `echo "alias translate=python3 path/to/src/main.py" >> ~/.zshrc`
- For python3 and bash(Ubuntu) `echo "alias translate=python3 path/to/src/main.py" >> ~/.bashrc`
- For python and zshell(MAC) `echo "alias translate=python path/to/src/main.py" >> ~/.zshrc`
- For python and bash(Ubuntu) `echo "alias translate=python path/to/src/main.py" >> ~/.bashrc`
After executing one of the commands restart the terminal session( close and reopen it ) and now you can use translator simply in a next way:
- translate WORD_IN_ENGLISH

# Technical details
Application uses clearly seperated layers and modules following mostly clean architecture.

