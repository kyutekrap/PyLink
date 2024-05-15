from .cls.helper import Helper


class CreateStep:
    @staticmethod
    @Helper()
    def ExampleCustomMethod(name: str, params: dict, **kwargs) -> dict | None:
        """
        :param name: Name of Step (*Unique str recommended)
        :param params: Any type of dict. (*Conventional writing of keys with `$` recommended)
        :param kwargs: Available [Debug, Persist] as aforementioned
        :return: None, else Key-Value dict to save on Persist=True
        """
        list_of_tuples = list((a, b) for a, b in list(zip(*params.get("$values").values())))
        list_of_tuples = str(list_of_tuples)[1:-1]
        sql_stmt = f'INSERT INTO {params.get("$table")} {tuple(params.get("$values").keys())} VALUES {list_of_tuples}'
        # ** sql_stmt->prepare->execute **
        return {"affected_rows": 2}
