from Link import *


class InsertUsers:
    def __init__(self):
        self.my_flow()

    @register_flow(Debug=True)
    def my_flow(self):
        CreateFlow([
            CreateStep.Insert({
                "table": "people",
                "values": {
                    "name": ["Kate Park", "Peter Parker"],
                    "number": ["1234567899", "1234567899"]
                }
            }),
            Debugger.log(GetStep("Insert")["affected_rows"]),
            Decision({
                System.Die: GetStep("Insert")["affected_rows"] == 0
            })
        ])
        self.my_other_flow()

    @register_flow()
    def my_other_flow(self):
        CreateFlow([
            CreateStep.Insert({
                "table": "schools",
                "values": {
                    "name": ["MIT", "CIT"],
                    "location": ["E Jefferson St", "N Jefferson St"]
                }
            })
        ])
