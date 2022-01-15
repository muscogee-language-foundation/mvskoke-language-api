import os
from marshmallow import Schema, fields, post_load
import psycopg
from dotenv import load_dotenv

# load environment variables from .env
load_dotenv()
DB = os.getenv('DB')

# basic Search class
class SearchQuery:
    def __init__(self, query):
        self.query = query

def search(query: SearchQuery):
    response = 'Results for '+query.query + ':';
    response += query_db(query.query)+'';
    return response;


def query_db(term: str):
    # Connect to an existing database
    conn = psycopg.connect(conninfo=DB);

    with conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            results = [];

            # mvskoke
            cur.execute(
                'SELECT mvskoke, english FROM entries WHERE '
                    'mvskoke ILIKE %s '
                    'OR mvskoke ILIKE %s', 
                    (term+'%', '%'+term+'%')
            );
            results.extend(cur.fetchall());

            # english
            cur.execute(
                "SELECT mvskoke, english FROM entries WHERE "
                "ts @@ to_tsquery('english', %s)"
                "OR english ILIKE %s",
                (term, '%'+term+'%')
            );
            results.extend(cur.fetchall());

            resultStr = '';
            for item in results:
                resultStr+=str(item);
            return resultStr;


if __name__ == "__main__":
    query_db("mvt");