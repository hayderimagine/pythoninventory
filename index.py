import curses
import time

# Sample static job data
jobs = [
    {"title": "Software Engineer", "company": "Acme Corp", "location": "New York"},
    {"title": "Data Scientist", "company": "DataWiz", "location": "San Francisco"},
    {"title": "Product Manager", "company": "Innovate Inc", "location": "Seattle"},
    {"title": "UI/UX Designer", "company": "Creative Minds", "location": "Austin"},
    {"title": "DevOps Engineer", "company": "CloudNet", "location": "Remote"},
]

def draw_ui(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Set color pair for retro look
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(1))
    
    # Draw title
    stdscr.addstr(1, 10, "=== JOB DIRECTORY ===", curses.A_BOLD)
    
    # Draw search bar
    stdscr.addstr(3, 2, "Search: ______________________________")
    
    # Draw job list header
    stdscr.addstr(5, 2, "Title                     Company               Location")
    stdscr.addstr(6, 2, "-" * 50)
    
    # Draw job listings
    y = 7
    for job in jobs:
        title = job["title"].ljust(25)
        company = job["company"].ljust(20)
        location = job["location"]
        stdscr.addstr(y, 2, f"{title} {company} {location}")
        y += 1

    # Draw navigation instructions
    stdscr.addstr(y + 2, 2, "[N] Next Page    [P] Previous Page    [Q] Quit", curses.A_BOLD)
    
    # Refresh the screen to show content
    stdscr.refresh()
    
    # Wait for user input
    while True:
        key = stdscr.getch()
        if key == ord("q") or key == ord("Q"):
            break

def main():
    # Initialize curses
    curses.wrapper(draw_ui)

if __name__ == "__main__":
    main()
