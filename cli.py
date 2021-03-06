#!/usr/bin/env python
import click
from mlib import predict

#var=

@click.command()
@click.option(
    "--OverallQual",
    prompt="Overall house quality, ranging from 0 to 10",
    help="Pass in the value for the overall house quality, ranging from 0 to 10",
)
def predictcli(OverallQual):
    """Predicts the sales prive of a house, based on its overall quality"""

    result = predict(OverallQual)
    click.echo(click.style(result["height_inches"], bg = "green", fg = "white"))

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    predictcli()
