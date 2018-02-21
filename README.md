<a target="_top" href="http://www.flamingtext.com/" ><img src="https://blog.flamingtext.com/blog/2018/02/21/flamingtext_com_1519200076_290247836.png" border="0" alt="Logo Design by FlamingText.com" title="Logo Design by FlamingText.com"></a>

# GIG : GitIgnore Generator [WIP]
Generate language/framework specific `.gitignore` from the comfort of your terminal. This is a work in **progress**.

## What is it?
A simple CLI tool to generate `.gitignore` files for your projects. It can generate `.gitignore` files specific to more than 100 languages or frameworks.

## Why use this?
Have you ever forgotten to add a `.gitignore` file while creating a new repository on github and then you have write a new `.gitignore` from scratch. Well this tool saves you the trouble of going through that.
So if you spend a lot of time on your terminal and are a bit forgetfull you might find this tool useful.

## Usage
Just `cd` into your project repository and type `gig --lang <language-or-framework>`
For e.g to generate a gitignore for a haskell project type `gig --lang Haskell`

## See it in action
![GIG in action](https://github.com/palash25/GIG/blob/master/assets/gig.gif)

## Requirements
**Python 3**
**Click**

## System Wide Installation
`$ git clone <this-repo>`
`$ cd GIG`
`$ pip install --editable .` (Use the editable flag if you want to hack on it make changes otherwise don't)

## Installation using virtualenv (Recommended)
An installing using virtualenv is always reccomended so that there are no conflicts with other modules and packages

Fisrt you need to install virtualenv, if you don't already have one. Install it using the following command:
`$ python3 -m pip3 install --user virtualenv`

Then you need to create a virtual environment. To create a virtual environment, go to your project’s directory and run virtualenv using the following command:
`$ python3 -m virtualenv env`

Before you can start installing or using packages in your virtualenv you’ll need to activate it. Run the following command to activate virtualenv:
`$ source env/bin/activate` 

Now, to install the required packages follow the instructions as mentioned under the section **System-wide installation**.

## Contributing
This is just the MVP and it still needs a lot of work. Once it is done it will be open for contributions.

## ToDo
- [ ] Add checks for pre-existing `.gitignore` files and uninitialized repo.
- [ ] Add warning messages for the user.
- [ ] Add docstrings and man page.
- [ ] PEP8ify the code.
- [ ] Refactoring and cleanup.
