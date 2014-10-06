Zabbix Map Generator 
====================

Contrary to its name this code doesn't generate a map, but, it will move every object it contails (selements) so that it is disposed on a grid (defined in Settings.py) sorted Alphabetically.

How to use :
-----------
- Create a Map in Zabbix and add any thing you want on it.
- Export the map as XML and save it as Map.xml
- run the main script `zabbix_map_generator.py` : it will generate a `map_parsed.xml` that you can reimport (checking every check box in the import wizard so that it updates current map.
