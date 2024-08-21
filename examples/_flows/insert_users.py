from PyLink import *


@Flow(Debug=True)
def InsertUsers():
    Step.Insert({
        "table": "people",
        "values": {
            "name": ["Kate Park", "Peter Parker"],
            "number": ["1234567899", "1234567899"]
        }
    })
    Debugger.log(GetStep("Insert")["affected_rows"])
    Step.Insert({
        "table": "schools",
        "values": {
            "name": ["MIT", "CIT"],
            "location": ["E Jefferson St", "N Jefferson St"]
        }
    })
    Debugger.log(GetStep("Insert")["affected_rows"])
