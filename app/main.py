def greet(name: str = "broken") -> str:
    return f"Hello from {name}"


if __name__ == "__main__":
    print(greet())
