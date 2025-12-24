# Progress Bar Menu App

A macOS menu bar application that displays progress bars for different time periods.

## Features

- **Day**: Shows progress from 8am to 6pm (10-hour workday)
- **Week**: Shows progress through the current week
- **Month**: Shows progress through the current month
- **Year**: Shows progress through the current year
- **Life**: Shows progress based on birth year (1988) and life expectancy (80 years)

## Requirements

- macOS
- Python 3
- rumps library

## Installation

```bash
pip3 install rumps
```

## Building the App

```bash
cd ~/progress_bar_app
python3 setup.py py2app
```

## Running

After building:
```bash
open dist/progress_bar.app
```

Or run directly:
```bash
python3 progress_bar.py
```

## Features

- Values are clamped between 1-99% to avoid edge cases
- Click menu items to switch between different display modes
- Visual progress bar using block characters (█ and ▒)
