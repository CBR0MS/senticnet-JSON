# senticnet-JSON
Convert senticnet sentiment data into JSON format. 

When working on a [sentiment chrome extension](https://github.com/CBR0MS/nlpExtension), I needed a sentiment dictionary in JSON form, but SenticNet was only available in XML, txt, RDF and as a python dictionary. I wrote this little script to convert the python dictionary into a JSON file for use with javascript.  

## Usage 

To convert a senticnet python dictionary to JSON format, ensure `senticnet5.py` is in the same directory and run: ```python convert_senticnet_json.py```

If you'd like to output pretty printed JSON, run:
```python convert_senticnet_json.py -p```

### Deleting Values from Senticnet

The senticnet5 python dictionary has quite a few entries for each word or phrase in the list. As of SenticNet5, each word looks like this:
```python
senticnet['concept_name'] = [
                            'pleasantness_value',
                            'attention_value', 
                            'sensitivity_value',
                            'aptitude_value', 
                            'primary_mood', 
                            'secondary_mood', 
                            'polarity_label', 
                            'polarity_value', 
                            'semantics1', 
                            'semantics2', 
                            'semantics3', 
                            'semantics4', 
                            'semantics5'
                            ] 
```
And the JSON output looks like this:
```json
{
    "a_little": [
        "-0.99",
        "0",
        "0",
        "-0.70",
        "#sadness",
        "#disgust",
        "negative",
        "-0.84",
        "least",
        "little",
        "small_amount",
        "shortage",
        "scarce"
    ],
    ...
}
```
You may not need all of these entries for your project, so you can delete them to make a smaller JSON file. To do this, run
```python convert_senticnet_json.py -d ```
followed by the entries you wish to remove. For example, to remove `semantics1`, `semantics2`, and `aptitude_value`, run 
```python convert_senticnet_json.py -d 8 9 3``` This will yield a json file organized like: 
```json
{
    "a_little": [
        "-0.99",
        "0",
        "0",
        "#sadness",
        "#disgust",
        "negative",
        "-0.84",
        "small_amount",
        "shortage",
        "scarce"
    ],
    ...
}
```
To see a list of the possible entries to remove and their associated indices, run 
```python convert_senticnet_json.py --values```

With nothing except for `polarity_value` senticnet goes from 28,197 KB to just 4,712 KB- not exactly a small file but certainly much reduced from the 28 MB inital size. 

### Help 
See all possible commands with ```python convert_senticnet_json.py --help```

## Compadibility 
`convert_senticnet_json.py` has been tested and words with SenticNet5 and SenticNet4, which are the only two versions to include a `.py` file in the publicly-available download. To use SenticNet4, include `senticnet4.py` in the directory and in `convert_senticnet_json.py` simply change 
```python
from senticnet5 import *
```
to 
```python
from senticnet4 import *
```
to get the senticnet4 dictionary. 