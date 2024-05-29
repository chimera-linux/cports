pkgname = "xfce4"
pkgver = "4.18"
pkgrel = 1
build_style = "meta"
depends = [
    "thunar",
    "thunar-volman",
    "tumbler",
    "xfce4-appfinder",
    "xfce4-panel",
    "xfce4-power-manager",
    "xfce4-screenshooter",
    "xfce4-session",
    "xfce4-settings",
    "xfdesktop",
    "xfwm4",
]
pkgdesc = "Xfce desktop environment (session)"
maintainer = "triallax <triallax@tutanota.com>"
license = "custom:meta"
url = "https://www.xfce.org"


@subpackage("xfce4-apps")
def _apps(self):
    self.pkgdesc = "Xfce desktop environment (apps)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        "catfish",
        "gigolo",
        "mousepad",
        "orage",
        "parole",
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
        "xfdashboard",
        # "orca"
    ]
    return []
