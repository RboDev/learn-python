from dataclasses import dataclass, field


@dataclass
class Action:
    command: str
    text: str


@dataclass
class TextEditor:
    text: str = ""
    actions: list[Action] = field(default_factory=list)
    index = -1

    def insert(self, text: str) -> None:
        self.actions.append(Action("insert", text))
        self.index += 1
        self.text += text

    def delete(self, num_chars: int) -> None:
        self.actions.append(Action("delete", self.text[-num_chars:]))
        self.index += 1
        self.text = self.text[:-num_chars]

    def undo(self) -> None:
        if self.index >= 0:
            action = self.actions[self.index]
            match action.command:
                case "insert":
                    self.text = self.text[:-len(action.text)]
                case "delete":
                    self.text += action.text
                case _:
                    raise Exception()
            self.index -= 1

    def redo(self) -> None:
        if self.index < len(self.actions) - 1:
            self.index += 1
            action = self.actions[self.index]
            match action.command:
                case "insert":
                    self.text += action.text
                case "delete":
                    self.text = self.text[:-len(action.text)]
                case _:
                    raise Exception()

    def print_text(self) -> None:
        print(self.text)


def main() -> None:
    # Test the text editor
    editor = TextEditor()

    # Since there is no text, these commands should do nothing
    editor.undo()
    editor.redo()

    editor.insert("Hello")
    editor.insert(" World!")
    editor.print_text()  # Output: Hello World!

    editor.delete(6)
    editor.print_text()  # Output: Hello

    editor.undo()
    editor.print_text()  # Output: Hello World!

    editor.redo()
    editor.print_text()  # Output: Hello

    editor.insert("!!!")
    editor.print_text()  # Output: Hello!!!

    editor.undo()
    editor.undo()
    editor.print_text()  # Output: Hello World!


if __name__ == "__main__":
    main()
