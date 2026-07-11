from core.container import Container


class Example:
    pass


container = Container()

example = Example()

container.register("example", example)

print(container.exists("example"))

resolved = container.resolve("example")

print(example is resolved)

print(container.registered_services())

container.unregister("example")

print(container.exists("example"))