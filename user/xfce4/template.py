pkgname = "xfce4"
pkgver = "4.20"
pkgrel = 2
build_style = "meta"
depends = [
    "gvfs",
    "thunar",
    "thunar-volman",
    "tumbler",
    "udisks",
    "xfce4-appfinder",
    "xfce4-panel",
    "xfce4-power-manager",
    "xfce4-screenshooter",
    "xfce4-session",
    "xfce4-settings",
    "xfdesktop",
    "xfwm4",
]
pkgdesc = "Xfce desktop environment"
subdesc = "session"
license = "custom:meta"
url = "https://www.xfce.org"


@subpackage("xfce4-apps")
def _(self):
    self.subdesc = "apps"
    self.install_if = [self.parent]
    self.depends = [
        "catfish",
        "gigolo",
        "mousepad",
        "orage",
        "orca",
        # "parole", # dbus-glib
        "pavucontrol",
        "ristretto",
        "xfburn",
        "xfce4-dict",
        "xfce4-mixer",
        "xfce4-notifyd",
        "xfce4-screensaver",
        "xfce4-taskmanager",
        "xfce4-terminal",
        "xfce4-volumed-pulse",
        # "xfdashboard", # clutter
    ]
    return []


@subpackage("xfce4-panel-plugins")
def _(self):
    self.subdesc = "panel plugins"
    self.install_if = [self.parent]
    self.depends = [
        "xfce4-battery-plugin",
        "xfce4-calculator-plugin",
        "xfce4-clipman-plugin",
        "xfce4-cpufreq-plugin",
        "xfce4-cpugraph-plugin",
        "xfce4-diskperf-plugin",
        "xfce4-docklike-plugin",
        "xfce4-eyes-plugin",
        "xfce4-fsguard-plugin",
        "xfce4-generic-slider",
        "xfce4-genmon-plugin",
        "xfce4-indicator-plugin",
        "xfce4-mailwatch-plugin",
        "xfce4-netload-plugin",
        "xfce4-notes-plugin",
        "xfce4-places-plugin",
        "xfce4-pulseaudio-plugin",
        "xfce4-sensors-plugin",
        "xfce4-smartbookmark-plugin",
        "xfce4-stopwatch-plugin",
        "xfce4-systemload-plugin",
        "xfce4-time-out-plugin",
        "xfce4-timer-plugin",
        "xfce4-verve-plugin",
        "xfce4-wavelan-plugin",
        "xfce4-weather-plugin",
        "xfce4-whiskermenu-plugin",
        "xfce4-windowck-plugin",
        "xfce4-xkb-plugin",
    ]
    return []
