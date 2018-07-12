# CardCastParser
Simple parser for CardCast. It gets rid of most pointless data that is stored in CardCast API and saves them to separate JSON files.

## Usage
    cardcastdump.py [option] [ARG]...

    Options:

      -i             Dump decks to JSON files by ID
 
      -f             Dump decks to JSON files from text file (multiple IDs in file, new id in new line)


 Examples:
 
 `cardcastdump.py -i ID1 ID2 ID3 ID4`
 
` cardcastdump.py -f file1.txt file2.txt`
 
 ### Licencing
  The one and only WTFPL.
