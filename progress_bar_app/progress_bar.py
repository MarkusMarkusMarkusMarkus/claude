#!/usr/bin/env python3
import rumps
from datetime import datetime, timedelta

class ProgressBarApp(rumps.App):
    def __init__(self):
        super().__init__("Progress", quit_button=None)
        self.birth_year = 1988
        self.life_expectancy = 80
        self.display_mode = "year"
        self.pending = None

        self.menu = ["Day", "Wk", "Mth", "Year", "Life", None, "Quit"]

        self.timer = rumps.Timer(self.on_tick, 1)
        self.timer.start()
        self.on_tick(None)

    @rumps.clicked("Day")
    def day_clicked(self, _):
        self.pending = "day"

    @rumps.clicked("Wk")
    def wk_clicked(self, _):
        self.pending = "wk"

    @rumps.clicked("Mth")
    def mth_clicked(self, _):
        self.pending = "mth"

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

        # Day: 8am to 6pm (10 hours)
        day_start = datetime(now.year, now.month, now.day, 8, 0)
        day_end = datetime(now.year, now.month, now.day, 18, 0)
        if now < day_start:
            d = 1
        elif now > day_end:
            d = 99
        else:
            d = max(1, min(99, ((now - day_start).total_seconds() / (10 * 3600)) * 100))

        # Week
        week_start = datetime(now.year, now.month, now.day) - timedelta(days=now.weekday())
        w = max(1, min(99, ((now - week_start).total_seconds() / (7 * 86400)) * 100))

        # Mth
        month_start = datetime(now.year, now.month, 1)
        if now.month == 12:
            month_end = datetime(now.year + 1, 1, 1)
        else:
            month_end = datetime(now.year, now.month + 1, 1)
        m = max(1, min(99, ((now - month_start).total_seconds() / (month_end - month_start).total_seconds()) * 100))

        # Year
        year_start = datetime(now.year, 1, 1)
        year_end = datetime(now.year + 1, 1, 1)
        y = max(1, min(99, ((now - year_start).total_seconds() / (year_end - year_start).total_seconds()) * 100))

        # Life
        birth = datetime(self.birth_year, 1, 1)
        life_span = self.life_expectancy * 365.25 * 86400
        l = max(1, min(99, ((now - birth).total_seconds() / life_span) * 100))

        self.menu["Day"].title = self.bar(d) + " Day: " + str(int(d)) + "%"
        self.menu["Wk"].title = self.bar(w) + " Wk: " + str(int(w)) + "%"
        self.menu["Mth"].title = self.bar(m) + " Mth: " + str(int(m)) + "%"
        self.menu["Year"].title = self.bar(y) + " Year: " + str(int(y)) + "%"
        self.menu["Life"].title = self.bar(l) + " Life: " + str(int(l)) + "%"

        vals = {"day": (d, "Day"), "wk": (w, "Wk"), "mth": (m, "Mth"), "year": (y, "Year"), "life": (l, "Life")}
        pct, lbl = vals[self.display_mode]
        self.title = self.bar(pct) + " " + lbl + ": " + str(int(pct)) + "%"

if __name__ == "__main__":
    ProgressBarApp().run()
