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
    click.echo(click.style(result, bg = "green", fg = "white")
    '''
    inches = result["height_inches"]
    human_readable = result["height_human_readable"]
    if int(inches) > 72:
        click.echo(click.style(human_readable, bg="green", fg="white"))
    else:
        click.echo(click.style(human_readable, bg="red", fg="white"))
    '''

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    predictcli()
