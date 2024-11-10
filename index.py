import curses

# Sample static job data (to display in the UI)
jobs = [
    {"title": "Software Engineer", "company": "Acme Corp", "location": "New York"},
    {"title": "Data Scientist", "company": "DataWiz", "location": "San Francisco"},
    {"title": "Product Manager", "company": "Innovate Inc", "location": "Seattle"},
    {"title": "UI/UX Designer", "company": "Creative Minds", "location": "Austin"},
    {"title": "DevOps Engineer", "company": "CloudNet", "location": "Remote"},
]

# Function to draw the UI
def draw_ui(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Set color pair for retro look
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(1))
    
    # Draw the title
    stdscr.addstr(1, 10, "=== JOB DIRECTORY ===", curses.A_BOLD)
    
    # Draw a simple search bar
    stdscr.addstr(3, 2, "Search: ______________________________")
    
    # Draw job list headers
    stdscr.addstr(5, 2, "Title                     Company               Location")
    stdscr.addstr(6, 2, "-" * 50)
    
    # Draw static job listings
    y = 7  # Starting row for job listings
    for job in jobs:
        title = job["title"].ljust(25)    # Title column (padded to 25 chars)
        company = job["company"].ljust(20)  # Company column (padded to 20 chars)
        location = job["location"]          # Location column
        stdscr.addstr(y, 2, f"{title} {company} {location}")
        y += 1

    # Draw navigation instructions
    stdscr.addstr(y + 2, 2, "[N] Next Page    [P] Previous Page    [Q] Quit", curses.A_BOLD)
    
    # Refresh the screen to display content
    stdscr.refresh()
    
    # Wait for user input and respond to it
    while True:
        key = stdscr.getch()
        if key == ord("q") or key == ord("Q"):
            break
        elif key == ord("n") or key == ord("N"):
            stdscr.addstr(y + 4, 2, "Next Page (placeholder)", curses.A_DIM)
        elif key == ord("p") or key == ord("P"):
            stdscr.addstr(y + 4, 2, "Previous Page (placeholder)", curses.A_DIM)
        stdscr.refresh()

# Main function to start the UI
def main():
    curses.wrapper(draw_ui)

if __name__ == "__main__":
    main()
