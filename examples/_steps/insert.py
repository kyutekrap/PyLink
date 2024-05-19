from Link import register_step


@register_step()
def Insert(name: str, params: dict, **kwargs) -> dict | None:
    list_of_tuples = list((a, b) for a, b in list(zip(*params.get("$values").values())))
    list_of_tuples = str(list_of_tuples)[1:-1]
    sql_stmt = f'INSERT INTO {params.get("$table")} {tuple(params.get("$values").keys())} VALUES {list_of_tuples}'
    # ** sql_stmt->prepare->execute **
    return {"affected_rows": 2}
