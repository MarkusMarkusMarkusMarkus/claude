#!/usr/bin/env python3
import rumps
from datetime import datetime, timedelta
from astral import LocationInfo
from astral.sun import sun

class ProgressBarApp(rumps.App):
    def __init__(self):
        super().__init__("Progress", quit_button=None)
        self.birth_year = 1988
        self.life_expectancy = 80
        self.display_mode = "year"
        self.pending = None

        # Set your location for daylight calculation
        # Default: San Francisco. Change to your city!
        self.location = LocationInfo("San Francisco", "USA", "America/Los_Angeles", 37.77, -122.41)

        self.menu = ["Work", "Useful", "Daylight", "Week", "Month", "Year", "Life", None, "Quit"]

        self.timer = rumps.Timer(self.on_tick, 1)
        self.timer.start()
        self.on_tick(None)

    @rumps.clicked("Work")
    def work_clicked(self, _):
        self.pending = "work"

    @rumps.clicked("Useful")
    def useful_clicked(self, _):
        self.pending = "useful"

    @rumps.clicked("Daylight")
    def daylight_clicked(self, _):
        self.pending = "daylight"

    @rumps.clicked("Week")
    def week_clicked(self, _):
        self.pending = "week"

    @rumps.clicked("Month")
    def month_clicked(self, _):
        self.pending = "month"

    @rumps.clicked("Year")
    def year_clicked(self, _):
        self.pending = "year"

    @rumps.clicked("Life")
    def life_clicked(self, _):
        self.pending = "life"

    @rumps.clicked("Quit")
    def quit_clicked(self, _):
        rumps.quit_application()

    def bar(self, pct):
        pct = max(0, min(100, pct))
        f = int(pct / 100 * 10)
        return chr(9608) * f + chr(9618) * (10 - f)

    def on_tick(self, _):
        if self.pending:
            self.display_mode = self.pending
            self.pending = None

        now = datetime.now()

        # Work day: 8am to 1pm (5 hours)
        work_start = datetime(now.year, now.month, now.day, 8, 0)
        work_end = datetime(now.year, now.month, now.day, 13, 0)
        if now < work_start:
            work = 1
        elif now > work_end:
            work = 99
        else:
            work = max(1, min(99, ((now - work_start).total_seconds() / (5 * 3600)) * 100))

        # Useful day: 8am to 8pm (12 hours)
        useful_start = datetime(now.year, now.month, now.day, 8, 0)
        useful_end = datetime(now.year, now.month, now.day, 20, 0)
        if now < useful_start:
            useful = 1
        elif now > useful_end:
            useful = 99
        else:
            useful = max(1, min(99, ((now - useful_start).total_seconds() / (12 * 3600)) * 100))

        # Daylight: sunrise to sunset (based on location)
        try:
            s = sun(self.location.observer, date=now.date())
            sunrise = s['sunrise'].replace(tzinfo=None)
            sunset = s['sunset'].replace(tzinfo=None)
            if now < sunrise:
                daylight = 1
            elif now > sunset:
                daylight = 99
            else:
                daylight = max(1, min(99, ((now - sunrise).total_seconds() / (sunset - sunrise).total_seconds()) * 100))
        except:
            # Fallback if astral fails
            daylight = 50

        # Week
        week_start = datetime(now.year, now.month, now.day) - timedelta(days=now.weekday())
        week = max(1, min(99, ((now - week_start).total_seconds() / (7 * 86400)) * 100))

        # Month
        month_start = datetime(now.year, now.month, 1)
        if now.month == 12:
            month_end = datetime(now.year + 1, 1, 1)
        else:
            month_end = datetime(now.year, now.month + 1, 1)
        month = max(1, min(99, ((now - month_start).total_seconds() / (month_end - month_start).total_seconds()) * 100))

        # Year
        year_start = datetime(now.year, 1, 1)
        year_end = datetime(now.year + 1, 1, 1)
        year = max(1, min(99, ((now - year_start).total_seconds() / (year_end - year_start).total_seconds()) * 100))

        # Life
        birth = datetime(self.birth_year, 1, 1)
        life_span = self.life_expectancy * 365.25 * 86400
        life = max(1, min(99, ((now - birth).total_seconds() / life_span) * 100))

        self.menu["Work"].title = self.bar(work) + " Work: " + str(int(work)) + "%"
        self.menu["Useful"].title = self.bar(useful) + " Useful: " + str(int(useful)) + "%"
        self.menu["Daylight"].title = self.bar(daylight) + " Daylight: " + str(int(daylight)) + "%"
        self.menu["Week"].title = self.bar(week) + " Week: " + str(int(week)) + "%"
        self.menu["Month"].title = self.bar(month) + " Month: " + str(int(month)) + "%"
        self.menu["Year"].title = self.bar(year) + " Year: " + str(int(year)) + "%"
        self.menu["Life"].title = self.bar(life) + " Life: " + str(int(life)) + "%"

        vals = {
            "work": (work, "Work"),
            "useful": (useful, "Useful"),
            "daylight": (daylight, "Day"),
            "week": (week, "Week"),
            "month": (month, "Month"),
            "year": (year, "Year"),
            "life": (life, "Life")
        }
        pct, lbl = vals[self.display_mode]
        self.title = self.bar(pct) + " " + lbl + ": " + str(int(pct)) + "%"

if __name__ == "__main__":
    ProgressBarApp().run()
