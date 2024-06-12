import uvicorn
from app import Server
from config import settings
import click

server = Server()
app = server.app
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

    
    
    uvicorn.run(
        app="__main__:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
    )

if __name__ == "__main__":
    serve()
