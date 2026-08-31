class Person:
    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.get_full_name(),
        }