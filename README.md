# Visualisation of a BIB file into a Hierarchical Edge Bundling

The script parses a BIB file generated automatically by Mendeley and generates a JSON file. The visualisation is done with [D3](https://d3js.org/) into an HTML file (we limit the visualisation to the authors with several publications to limit the number of authors to display).

Run the 'process_data.py' file to create the JSON file and update the HTML file

```
python process_data.py
```

The dynamic result of this visualisation is available [here](https://rfalque.github.io/pages/bibvis.html).

:heavy_exclamation_mark: In order to be interpreted the JSON file has to be processed by a server (or emulated locally).
