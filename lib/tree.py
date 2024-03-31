class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, id):
        return self._depth_first_search(self.root, id)

    def _depth_first_search(self, node, id):
        if node['id'] == id:
            return node

        for child in node['children']:
            result = self._depth_first_search(child, id)
            if result:
                return result

        return None

    def _breadth_first_search(self, id):
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            if node['id'] == id:
                return node

            for child in node['children']:
                queue.append(child)

        return None

# Test the depth-first search
root = {
    'tag_name': 'div',
    'id': 'root',
    'text_content': 'Root Element',
    'children': [
        {
            'tag_name': 'h1',
            'id': 'heading',
            'text_content': 'Title',
            'children': []
        },
        {
            'tag_name': 'p',
            'id': 'paragraph',
            'text_content': 'Lorem ipsum dolor sit amet',
            'children': []
        }
    ]
}

tree = Tree(root)
print(tree.get_element_by_id('heading'))  # Output: {'tag_name': 'h1', 'id': 'heading', 'text_content': 'Title', 'children': []}

# Test the breadth-first search
print(tree._breadth_first_search('paragraph'))  # Output: {'tag_name': 'p', 'id': 'paragraph', 'text_content': 'Lorem ipsum dolor sit amet', 'children': []}
