"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1,2,3]],
            "answer": [1, 3, 6],
        },
        {
            "input": [[1,1,1,1,1]],
            "answer": [1, 2, 3, 4, 5],
        },
        {
            "input": [[1, 0, 0]],
            "answer": [1, 1, 1],
        },
        {
            "input": [[]],
            "answer": [],
        }
    ],
    "Extra": [
        {
            "input": [[6,3,7,9,0,545,46,7,34]],
            "answer": [6, 9, 16, 25, 25, 570, 616, 623, 657],
        },
    ]
}
