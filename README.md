# Mvskoke Language API

This is a Python + Flask app that interacts with a Postgres 12 database.

http://api.muscogeelanguage.org/

## Usage

Search will return results from the database in English or Mvskoke.

`/search?query=[term]`  

i.e:  
`/search?query=friend`  
or   
`/search?query=mv`

## Roadmap 
- Ranking
- Normalizations for Mvskoke
