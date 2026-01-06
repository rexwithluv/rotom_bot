import tomllib


class Configuration:
    def __init__(self, filename: str):
        self._data: dict[str, any] = self._load_data(filename)

    def _load_data(self, filename: str) -> dict[str, any]:
        try:
            with open(filename, "rb") as f:
                return tomllib.load(f)
        except Exception as e:
            print(f"ERROR: {e}")

    @property
    def bot_token(self) -> str:
        return self._data["bot_token"]

    @property
    def chat_id(self) -> str:
        return self._data["chat_id"]

    @property
    def job_interval(self) -> float:
        return float(self._data["job_interval"])
