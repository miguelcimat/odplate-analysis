def require(condition: bool, message: str, exc_type=ValueError) -> None:
    if not condition:
        raise exc_type(message)
