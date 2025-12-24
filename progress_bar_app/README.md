# Progress Bar Menu App

A macOS menu bar application that displays progress bars for different time periods.

## Features

- **Work**: Shows progress from 8am to 1pm (5-hour work period)
- **Useful**: Shows progress from 8am to 8pm (12-hour useful day)
- **Daylight**: Shows progress from sunrise to sunset (location-based)
- **Week**: Shows progress through the current week
- **Month**: Shows progress through the current month
- **Year**: Shows progress through the current year
- **Life**: Shows progress based on birth year (1988) and life expectancy (80 years)

## Requirements

- macOS
- Python 3
- rumps library
- astral library (for sunrise/sunset calculations)

## Installation

1. **Install Python 3** (if not already installed):
   ```bash
   brew install python3
   ```

2. **Install required libraries**:
   ```bash
   pip3 install rumps astral
   ```

3. **Configure your location** (optional):
   Edit `progress_bar.py` and update line 17 with your city coordinates:
   ```python
   self.location = LocationInfo("YourCity", "Country", "Timezone", latitude, longitude)
   ```

4. **Customize your settings** (optional):
   - Line 10: Change `birth_year` to your birth year
   - Line 11: Change `life_expectancy` if desired

## Running the App

### Option 1: Run directly (for testing)
```bash
cd progress_bar_app
python3 progress_bar.py
```

### Option 2: Build standalone app
```bash
cd progress_bar_app
python3 setup.py py2app
open dist/progress_bar.app
```

To run the app at login:
1. Open **System Preferences** > **Users & Groups** > **Login Items**
2. Click the **+** button
3. Navigate to `progress_bar_app/dist/` and select `progress_bar.app`

## Usage

- The menu bar will show a progress bar and percentage for your selected mode
- Click the menu bar icon to see all progress bars
- Click any item to switch the main display to that mode
- Click "Quit" to exit the app

## Customization

Edit `progress_bar.py` to adjust:
- **Work hours**: Line 66-67 (currently 8am-1pm)
- **Useful hours**: Line 76-77 (currently 8am-8pm)
- **Location**: Line 17 (for accurate sunrise/sunset)
- **Birth year**: Line 10
- **Life expectancy**: Line 11

## Additional Features

- Values clamped between 1-99% to avoid edge cases
- Real-time sunrise/sunset calculation based on your location
- Updates every second
- Visual progress bars using block characters (█ and ▒)
