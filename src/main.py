import argparse
import sys
from rich.console import Console
from rich.panel import Panel
from parking_manager import ParkingManager

# Initialize Rich console for pretty output
console = Console()
manager = ParkingManager()

def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser(description="SpotSaver: Never lose your car or get a ticket again!")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: park
    park_parser = subparsers.add_parser("park", help="Save a new parking location")
    park_parser.add_argument("--loc", required=True, help="Where you parked (e.g., 'Level 3, Row C')")
    park_parser.add_argument("--hours", type=int, required=True, help="How many hours on the meter")
    park_parser.add_argument("--mins", type=int, default=0, help="How many extra minutes (optional)")

    # Command: status
    subparsers.add_parser("status", help="Check how much time is left")

    # Command: clear
    subparsers.add_parser("clear", help="Clear the current parking session")

    # Parse the arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "park":
        ticket = manager.park_car(args.loc, args.hours, args.mins)
        console.print(Panel(f"[bold green]Parking Saved![/bold green]\nLocation: {ticket['location']}\nExpires at: {ticket['end_time']}", title="Success"))

    elif args.command == "status":
        status = manager.get_status()
        if status == "EXPIRED":
            console.print(Panel("[bold red]⚠️  METER EXPIRED! ⚠️[/bold red]", title="WARNING"))
        elif status == "No active parking session.":
            console.print("[yellow]No active parking found.[/yellow]")
        else:
            console.print(Panel(f"[bold cyan]Time Remaining:[/bold cyan] {status}", title="Status"))

    elif args.command == "clear":
        manager.clear_parking()
        console.print("[bold green]Parking session cleared.[/bold green]")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()