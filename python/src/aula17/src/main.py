import ast
import click
import os


@click.group()
def main():
    pass

@main.command()
def hello():
    print("hello")
