from rich import print
from rich.table import Table

print("[bold green]Hello[/bold green]")

table = Table()

table.add_column("Name")
table.add_column("Age")

table.add_row("Nayan", "21")
table.add_row("Rahul", "22")

print(table)