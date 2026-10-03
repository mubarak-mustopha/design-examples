def open(expander, node):
    value = expander.env.find(node.attrs["z-var"])

    expander.showTag(node, False)
    expander.output(str(value))


def close(expander, node):
    expander.showTag(node, True)
