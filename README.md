
# arabic2latin

Convert Arabic and Persian (Farsi) characters to their English homophone.


## Installation

Install from PyPI:
```bash
pip install arabic2latin
```
Alternatively, install from source:
```bash
pip install git+https://github.com/rexa222/arabic2latin
```
## Usage/Examples

```python
from arabic2latin import arabic_to_latin

arabic_text = "السَّلَامُ عَلَيْكَ"
arabic_converted_text = arabic_to_latin(arabic_text)

persian_text = "سلام بر همگی"
persian_converted_text = arabic_to_latin(persian_text)

print("Arbic converted text: " + arabic_converted_text)
print("Persian converted text: " + persian_converted_text)
```
Output:
```text
Arbic converted text: alsaalaamo aalayka
Persian converted text: salam bar hamagy
```
## Debug Mode
If you came across a character that was not converted, you can find it using debug feature and report it as guided in the contributing section.
```text
converted_text = arabic_to_latin(arabic_text, debug=True)
```
Output:
```text
unknown character: ?
```




## Contributing

If you find a bug 🐛, please open a [bug report](https://github.com/rexa222/arabic2latin/issues/new?assignees=&labels=bug&template=bug_report.md&title=). If you have an idea for an improvement or new feature 🚀, please open a [feature request](https://github.com/rexa222/arabic2latin/issues/new?assignees=&labels=Feature+request&template=feature_request.md&title=).

