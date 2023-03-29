# What is this?
 This repo allows you to download endnote files from .bib format of files, using google scholar.

# How to use?

## 1. Prepare the python environment

```
pip install -r requirements.txt
````

## 2. Run with the bib file (can be the .txt or .bib etc...)

```
python main.py --file <yourBibFile>
```

You can check the downloaded file in the `refs` folder under the path that you execute the code.

## 3. (Optional) Ignore references by adding
```
--ignore <your file>
```
The file should have the format as: (every line is a paper title)
```
<title1> # you should replace <> as well
<title2>
...
```
or you can export the file from endnote by using the style we provided `export notes.ens`


# Proxy for China area
Export the IP and port of your proxy server in the terminal window which you use to run the code. For example:

在用于运行代码的终端窗口中导出代理服务器的 IP 和端口。例如：

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

通常情况下IP就为`http://127.0.0.1`，端口需要查看你的代理软件的设置，clash默认为`7890`。