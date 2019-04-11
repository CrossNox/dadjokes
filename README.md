# Dadjokes
[icanhazdadjoke](https://icanhazdadjoke.com/) API wrapper, to programatically cheer your code up.

# Installation
```bash
pip install dadjokes
```

# Usage

## Example
```python
from dadjoke import Dadjokes
dadjoke = Dadjoke()
print(dadjoke.joke)
```

The previous snippet will print a random joke.  

`Dadjoke` objects can be built from an id as well. You can get those calling the `.id` property of a `Dadjoke`. If you are using this in a **Slack** app, you might find the `.as_slack` property useful.

### cli
Please check available options with:  
```bash
dadjokes -h
```