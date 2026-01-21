"""Console script for tune-tile-press."""

import sys

import click


@click.command()
def main(args=None):
    """Console script for tune-tile-press."""
    click.echo("Replace this message by putting your code into tune_tile_press.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    print(f"Gotta use the args: {args}")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
