class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class Autocomplete:
    def __init__(self):
        self.root = Trie()

    def insert(self, key: str):
        trie_node = self.root
        for character in key:
            if character not in trie_node.children.keys():
                trie_node.children[character] = Trie()
            trie_node = trie_node.children[character]
        trie_node.end = True

    def get_last_node(self, key: str) -> Trie:
        trie_node = self.root
        for character in key:
            if character not in trie_node.children.keys():
                return None
            trie_node = trie_node.children[character]
        return trie_node

    def autocomplete(self, to_complete: str) -> list:
        trie_node = self.get_last_node(to_complete)
        if trie_node is None:
            return []

        stack = [(to_complete, trie_node)]
        suggestions = []
        while len(stack) > 0:
            stack_item = stack.pop()
            if stack_item[1].end:
                suggestions.append(stack_item[0])
            for key, child in stack_item[1].children.items():
                stack.append((stack_item[0] + key, child))

        return suggestions

if __name__ == "__main__":
    words = ["hola", "hey", "Salud", "Saludo"]
    autocomplete = Autocomplete()
    for word in words:
        autocomplete.insert(word)
    print(autocomplete.autocomplete("h"))
    print(autocomplete.autocomplete("Salud"))
    print(autocomplete.autocomplete("non"))
