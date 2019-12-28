How it works:

Given a  term, definition and a search term, decide on its "score", which determines the order of the elements displayed.

Step 1:

Search term(s) for search term, and separate all terms out that contain the search term

Step 2:

For each of these, add an entry to the scores like so:

term: score

where score is 50 minus the number of letters outside the search term. For example:

search term = pre
term = pre-lude
score = 4

search term = pre
term = sa-pre-si
score = 4

OR

50 - pad_n

Step 3:

Search all definitions for search term and separate all terms and definitions out that contain the search term

Step 4:

Separate the words that contain the search term out

Step 5:

For each term, add an entry to the scores like so:

term: score

where score is (20 minus the average number of letters around the word (as described in Step 2)) plus (2 times the occurences of the search term in the definition)

OR

(20 - avg(pad_n)) + (2 x i_occ)

Step 6:

From scores, find out the rank of each term

Step 7:

Pack the info up into a JSON string:

"{"term": "Prelude", "definition": "...", "rank": 1}"
