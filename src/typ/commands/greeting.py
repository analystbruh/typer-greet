import typer
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def greet(
    name: Annotated[str, typer.Argument(help='Name of who to greet.')]
):
    print(f'hi {name}')