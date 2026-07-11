from core.container import Container


class Example:
    pass


container = Container()

example = Example()

container.register(Example, example)

print(container.exists(Example))

resolved = container.resolve(Example)

print(example is resolved)

print(container.registered_services())

container.unregister(Example)

print(container.exists(Example))