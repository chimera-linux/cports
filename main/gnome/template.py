pkgname = "gnome"
pkgver = "46.1"
pkgrel = 1
build_style = "meta"
# a bunch of stuff is indirect dependencies we don't need to list
# some of them are here anyway, for clarity but no other purpose
depends = [
    "adwaita-icon-theme",
    "dconf",
    "desktop-file-utils",
    "fonts-cantarell-otf",
    "fonts-source-code-pro-otf",
    "gdm",
    "gjs",
    "glib-networking",
    "gnome-backgrounds-gnome",
    "gnome-bluetooth",
    "gnome-color-manager",
    "gnome-control-center",
    "gnome-desktop",
    "gnome-initial-setup",
    "gnome-keyring",
    "gnome-online-accounts",
    "gnome-session",
    "gnome-settings-daemon",
    "gnome-shell",
    "gnome-video-effects",
    "gsettings-desktop-schemas",
    "gvfs",
    "mutter",
    "nautilus",
    "tracker",
    "tracker-miners",
    "yelp",
    "xdg-desktop-portal-gnome",
    "xdg-user-dirs-gtk",
]
# backwards compat
provides = [f"gnome-core={pkgver}-r{pkgrel}"]
pkgdesc = "GNOME desktop environment (session)"
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
        "gnome-contacts",
        # "gnome-connections",
        "gnome-disk-utility",
        "gnome-font-viewer",
        "gnome-maps",
        # "gnome-music",
        # "gnome-remote-desktop",
        "gnome-screenshot",
        "gnome-software",
        "gnome-shell-extensions",
        "gnome-system-monitor",
        "gnome-text-editor",
        "gnome-user-docs",
        # "gnome-user-share",
        "gnome-weather",
        # "orca",
        # "phodav",
        "simple-scan",
        "sushi",
        "totem",
    ]
    return []
