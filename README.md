# RankedPairs
A Ranked Pairs Python Module

```console
pip install rankedpairs
```

This module contains a lightweight implementation of the Ranked Pairs method for determining the winner of a ranked choice election. In future releases, this package will be extended with other methods. 

Further documentation exists though python's built in ```help()``` function. In summary, this module can parse votes represented as mappings between a candidate and a preference and determine the winner of an election. There is an ```Election``` class to more easily store and parse data, but the core functions exist separately and can be invoked on candidates and votes. 
