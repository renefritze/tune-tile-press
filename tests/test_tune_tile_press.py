"""Tests for `tune-tile-press` package."""

from click.testing import CliRunner

import tune_tile_press
from tune_tile_press import cli


def test_version():
    assert tune_tile_press.__version__


def test_import():
    import tune_tile_press  # noqa: F401, PLC0415


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "tune_tile_press.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
