# What is this?
 This repo allows you to download endnote files from .bib format of files, using google scholar.

# How to use?

1. Prepare the python environment

```
pip install -r requirements.txt
````

2. Run with the bib file (can be the .txt or .bib etc...)

```
python main.py --file <yourBibFile>
```

You can check the downloaded file in the `refs` folder under the path that you execute the code.


# Proxy for China area
Export the IP and port of your proxy server in the terminal window which you use to run the code. For example:

## windows
```
set https_proxy=http://127.0.0.1:<port>
set http_proxy=http://127.0.0.1:<port>
```

## mac and linux
```
export https_proxy=http://127.0.0.1:<port>
export http_proxy=http://127.0.0.1:<port>
```
