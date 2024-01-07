pkgname = "gnome"
pkgver = "45.1"
pkgrel = 0
build_style = "meta"
depends = [
    f"gnome-core~{pkgver}",
]
pkgdesc = "GNOME desktop environment (session and apps)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://www.gnome.org"


@subpackage("gnome-apps")
def _apps(self):
    self.pkgdesc = "GNOME desktop environment (apps)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        "baobab",
        "eog",
        "epiphany",
        "evince",
        "gnome-browser-connector",
        "gnome-calculator",
        "gnome-calendar",
        "gnome-characters",
        "gnome-clocks",
        "gnome-console",
        # "gnome-contacts",
        # "gnome-connections",
        "gnome-disk-utility",
        "gnome-font-viewer",
        # "gnome-maps",
        # "gnome-music",
        # "gnome-remote-desktop",
        "gnome-screenshot",
        "gnome-software",
        "gnome-shell-extensions",
        # "gnome-system-monitor",
        "gnome-text-editor",
        "gnome-user-docs",
        # "gnome-user-share",
        # "gnome-weather",
        # "orca",
        # "phodav",
        "simple-scan",
        "sushi",
        "totem",
    ]
    return []
