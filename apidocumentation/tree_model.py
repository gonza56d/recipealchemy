
class ApiDocumentationNode:

    name = ''
    description = ''
    url = ''
    inner_nodes = []

    def __init__(self, name, description, url, inner_nodes):
        self.name = name
        self.description = description
        self.url = url
        self.inner_nodes = inner_nodes


class ApiDocumentationTreeModel:

    resources = [
        ApiDocumentationNode('Ingredients', 'Learn how to handle our ingredients resource.', '/api/ingredients/', []),
        ApiDocumentationNode('Recipes', 'Learn how to handle our recipes resource.', '/api/recipes/', []),
        ApiDocumentationNode('Users', 'Learn how to handle our users and authentication credentials.', '/api/users/', [])
    ]
