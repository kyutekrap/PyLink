from Link import CreateFlow, CreateStep, Debugger, GetStep, Decision


code = CreateFlow("Flow", [
        CreateStep.ExampleCustomMethod("Step1", {
            "$table": "people",
            "$values": {
                "name": ["Kate Park", "Peter Parker"],
                "number": ["1234567899", "1234567899"]
            }
        }, Persist=True, Debug=True),
        Debugger.log(GetStep("Step1", "affected_rows")),
        Decision({
            "End": GetStep("Step1", "affected_rows") == 0
        }),
        CreateStep.ExampleCustomMethod("Step1-1", {
            "$table": "schools",
            "$values": {
                "name": ["MIT", "CIT"],
                "location": ["E Jefferson St", "N Jefferson St"]
            }
        }, Debug=True)
    ])


print(code)
