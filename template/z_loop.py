def open(expander, node):
    index_name, target_name = node.attrs["z-loop"].split(":")
    target = expander.env.find(target_name)

    expander.showTag(node, False)
    for item in target:
        expander.env.push({index_name: item})
        for child in node.children:
            expander.walk(child)
        expander.env.pop()
    return False


def close(expander, node):
    expander.showTag(node, True)
