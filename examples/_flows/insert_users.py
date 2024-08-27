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
    Decision(GetStep("Insert")["affected_rows"], {
        "CreateIds": "> 0",
        System.Die: "== 0"
    })
    RecursiveFlow({
        "update": 0,
        "epoch": 2
    }).CreateIds(1)
    Debugger.log(GetFlow("CreateIds"))


@Flow(Debug=True, Thread=False, Wait=False)
def CreateIds(x: int) -> int:
    RecursiveStep({
        "update": 0,
        "epoch": 10,
        "if": "< 100000"
    }).GenerateId(x)
    Decision(GetStep("GenerateId"), {
        System.Die: "== 0"
    })
    Step.Insert({
        "table": "ids",
        "values": {
            "id": [x],
            "number": [GetStep("GenerateId")]
        }
    })
    return x + 1
