from solutions1.solution import strict

@strict
def add (a: int, b: int) -> int:
    return a + b

@strict
def divide(a: float, b: float) -> float:
    return a / b

@strict
def sentence(name: str, execited: bool) -> str:
    return f"Hi, {name}{'!' if execited else '-'}"


@strict
def echo(x):
    return x
