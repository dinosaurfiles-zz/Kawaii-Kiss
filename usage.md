usage demo:

  > kiss.py -h
  + display help options

''
  > kiss.py -F
  + Display available video qualities

''  
  > kiss.py -f <1080,720,...>
  + check if video format is available
    * if 'no'
      * display available formats
      * exit program
    + if 'yes'
      * link video formats to links

| links    | format |
| -------- | -------- |
| link   | 1080      |
| link   | 720   |

* set filename()
  * get filename
  * strip + [vid format]
* proceed with download()
  * wget -c < link > -O < filename >
