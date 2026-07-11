from core.container import Container


class Example:
    pass


container = Container()

example = Example()

container.register("example", example)

resolved = container.resolve("example")

print(example is resolved)