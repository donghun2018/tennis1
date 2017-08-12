# tennis1


## Requirement 1.0

- Goal
  - tournament matching program
  - preliminary league splitting

- input
  - text. csv. name. school. seed.
  - [name1],[name2],[school],[level],[seed]
  
- output
  - text. csv. per [league_name]
  - {[name1],[name2],[school]}
  - league split result
  
## Future Suggestions

- Add.


### input_parser.py
- param: entry csv file
- Parse the inputs and put it into a dictionary form

### prelim_league_placement.py
- param: N (number of teams per league)
- Divide the entries into leagues of size N
- Make sure to divide up the schools, and match higher seeds with lower seeds
- The top K teams are able to enter the tournament phase
