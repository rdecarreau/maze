# maze

Uses a single-pass filtering algorithm to find all possible paths through a maze and removes dead-ends. The idea is that the output dictionary of nodes can be fed to a search algorithm to select a path.

## Runtime

My best estimates right now are O((rows*columns) * log(branches)) but that is really preliminary.

## Generators

I didn't have to work out the generators because I used some cool ones already available:

* Multipath: https://keesiemeijer.github.io/maze-generator
* Other: http://www.mazegenerator.net/
