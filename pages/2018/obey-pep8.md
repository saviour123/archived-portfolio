title: Make Your Code PEP8 Complaint
tags: [python, pep8]
date: 2018-12-27
published: True
subtitle: If you are in the python world, it's quite important to make your code PEP8 complaint!


Quick Tip For Pythonistas - This is short a short post.

To check if your code is pep8 compliant.
In the root of your folder.
    
    $ pip install pylint

    $ find . -iname "*.py" | xargs pylint


Many text editors also support on the fly linting. My favourite is [VSCODE](https://code.visualstudio.com/download) with the python plugin. You can get auto formating of your code by setting up [autopep8](https://donjayamanne.github.io/pythonVSCodeDocs/docs/formatting/) on your vscode. 