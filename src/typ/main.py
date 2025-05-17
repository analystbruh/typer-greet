import typer
from typing_extensions import Annotated
from typing import Optional
from importlib import metadata
from .commands import greeting

__version__ = metadata.version('typ')

def version(value):
    if value:
        print(f'Typ version: {__version__}')
        raise typer.Exit()

app = typer.Typer()

@app.callback()
def main(
    version: Annotated[
        Optional[bool],
        typer.Option('--version', callback=version, help="Show app version." )
    ] = None
):
    pass

app.add_typer(greeting.app)

# if __name__ == '__main__':
#     app()