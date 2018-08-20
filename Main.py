class TreeNode:
    def __init__(self, key="", val="", left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent

    def __repr__(self):
        return f'k: {self.key}, v: {self.val}'


items = {
	"0":"the",
	"10":"chased",
	"110":"dog",
	"1110":"mouse",
	"1111": "cat",
}

root = TreeNode("root")


def get_TreeNode(tree_node, key, value):
    current_node = tree_node
    for i, v in enumerate(key):
        partial_key = key[0:i + 1]
        if v == "0":
            if current_node.right is None:
                current_node.right = TreeNode(key=partial_key, parent=current_node)
            current_node = current_node.right
        else:
            if current_node.left is None:
                current_node.left = TreeNode(key=partial_key, parent=current_node)
            current_node = current_node.left
    current_node.val = value
    current_node.key = key
    return current_node


for key, value in items.items():
    get_TreeNode(root, key, value)


def print_parent_list(parents):
    parents = parents[::-1]
    sj = []
    for item in parents:
        if item.val == "":
            sj.append(f'"{item.key}"')
        else:
            sj.append(f'"{item.key}:{item.val}"')
    print(' -> '.join(sj))


def get_parent_list(current):
    parents = [current]
    parent = current
    while parent.parent is not None:
        parents.append(parent.parent)
        parent = parent.parent
    return parents


ranks = {999: []}


def append_to_ranks(ranks, current):
    if current.key == "root":
        return
    if current.left is None and current.right is None:
        ranks[999].append(f'"{current.key}:{current.val}"')
    else:
        if len(current.key) not in ranks:
            ranks[len(current.key)] = []
        ranks[len(current.key)].append(f'"{current.key}"')


stack = [root]
while stack:
    current = stack.pop()
    append_to_ranks(ranks, current)

    if current.val != "":
        parents = get_parent_list(current)
        print_parent_list(parents)

    if current.right is not None:
        stack.append(current.right)

    if current.left is not None:
        stack.append(current.left)

for value in sorted(ranks.keys()):
    print('{rank = same; ' + "; ".join(ranks[value]) + '}')
