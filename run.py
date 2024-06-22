import subprocess

import click

from config import settings


@click.command()
@click.option(
    "-h", "--host", show_default=True, help=f"Host IP. Default: {settings.HOST}"
)
@click.option(
    "-p", "--port", show_default=True, type=int, help=f"Port. Default: {settings.PORT}"
)
@click.option("--level", help="Log level")
def serve(host, port, level):
    """Start server."""
    kwargs = {
        "LOGLEVEL": level,
        "HOST": host,
        "PORT": port,
    }
    for name, value in kwargs.items():
        if value:
            settings.set(name, value)
    subprocess.run(["python", "-m", "app.main"])


@click.group()
def cli():
    pass


cli.add_command(serve)

if __name__ == "__main__":
    cli()
