def open(expander, node):
    expander.showTag(node, False)
    expander.output(str(node.attrs["z-num"]))


def close(expander, node):
    expander.showTag(node, True)
