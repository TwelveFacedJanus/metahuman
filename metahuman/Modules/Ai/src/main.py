from pydantic import BaseModel
import tensorflow

type Result[T] = list(T)
type Void = None

class Images(BaseModel):
    front: str = ""
    back: str = ""
    left: str = ""
    right: str = ""
    

    def load_images(self: object) -> None:
        self.images: List[str] = []
        with open(self.front, 'rb') as file:
            self.images.append(file.readlines())
        with open(self.back, 'rb') as file:
            self.images.append(file.readlines())
        with open(self.left, 'rb') as file:
            self.images.append(file.readlines())
        with open(self.right, 'rb') as file:
            self.images.append(file.readlines())
def main() -> Void:
    pass

if __name__ == "__main__":
    main()