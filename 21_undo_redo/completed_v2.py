from dataclasses import dataclass, field


@dataclass
class Action:
    command: str
    text: str


@dataclass
class TextEditor:
    text: str = ""
    undos: list[Action] = field(default_factory=list)
    redos: list[Action] = field(default_factory=list)

    def insert(self, text: str) -> None:
        self.undos.append(Action("insert", text))
        self.text += text

    def delete(self, num_chars: int) -> None:
        self.undos.append(Action("delete", self.text[-num_chars:]))
        self.text = self.text[:-num_chars]

    def undo(self) -> None:
        if self.undos:
            action = self.undos.pop()
            self.redos.append(action)

            match action.command:
                case "insert":
                    self.text = self.text[:-len(action.text)]
                case "delete":
                    self.text += action.text
                case _:
                    raise Exception()

    def redo(self) -> None:
        if self.redos:
            action = self.redos.pop()
            self.undos.append(action)
            
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
