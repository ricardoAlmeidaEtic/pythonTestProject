import click

@click.group
@click.argument('list_arg')
@click.pass_context
def main(ctx):
    ctx.ensure_object(list)

@main.command()
@click.argument('list_arg')
@click.argument('name')
@click.pass_context
def add(ctx, list_arg, name):
    ctx.obj.append(name)

@main.command()
def read(ctx, list_arg):
    print(list_arg)