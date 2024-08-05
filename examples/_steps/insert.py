from Link import register_step
from typing import TypedDict, Dict


class InsertProps(TypedDict):
    table: str
    values: Dict[str, str]


class CRUD:
    @staticmethod
    @register_step(Debug=True)
    def Insert(params: InsertProps) -> dict | None:
        list_of_tuples = list((a, b) for a, b in list(zip(*params.get("values").values())))
        list_of_tuples = str(list_of_tuples)[1:-1]
        sql_stmt = f'INSERT INTO {params.get("table")} {tuple(params.get("values").keys())} VALUES {list_of_tuples}'
        # ** sql_stmt->prepare->execute **
        return {"affected_rows": 2}
