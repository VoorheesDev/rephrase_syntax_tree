# The syntax tree paraphrase

## What does this service do?
<p align="justify">
The main idea is to create new texts by rephrasing the 
existing ones in order to make them unique, for example,
for search engines (the text has to differ from others
but the meaning remains).<br>
</p>

The project was implemented using [Django](https://www.djangoproject.com/) framework and [nltk.tree](https://www.nltk.org/howto/tree.html) package.

### An algorithm of paraphrasing:<br>
+ In text find all noun phrases 
(NP), consisting of several NPs, separated by tags: "," (comma)
or "CC" (coordinating conjunction, e.g. "and").
+ Generate variants of permutations of these inner NP trees. 

## Installation

### Clone the repo
```bash
git clone https://github.com/VoorheesDev/rephrase_syntax_tree.git
cd rephrase_syntax_tree
```

### Create a virtual environment and install requirements
+ For <b>Linux</b>:
```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r ./requirements/base.txt
```

+ For <b>Windows</b>:
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r .\requirements\base.txt
```

## Usage
To start the server simply run:
```bash
python ./backend/manage.py runserver
```

## Available endpoints

+ <b>POST</b> [/api/v1/rephrase/](http://127.0.0.1:8000/api/v1/rephrase/) - create new unique rephrased trees <br>
    Query parameters:
    * <b>tree</b> (required) - a syntax tree to paraphrase unique trees from.<br>
      For example: `(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS restaurants))))))))`
      is a syntax tree for sentence "*The charming Gothic Quarter, or Barri Gòtic, has narrow medieval streets filled with trendy bars, clubs and Catalan restaurants.*" 
    * <b>limit</b> (optional, default: 20) - the maximum number of generated trees in response
