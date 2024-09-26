pkgname = "gnome"
pkgver = "46.3"
pkgrel = 2
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
    "xdg-desktop-portal-gnome",
    "xdg-user-dirs-gtk",
    "yelp",
]
# backwards compat
provides = [self.with_pkgver("gnome-core")]
pkgdesc = "GNOME desktop environment"
subdesc = "session"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://www.gnome.org"


@subpackage("gnome-apps")
def _(self):
    self.subdesc = "apps"
    self.install_if = [self.parent]
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
        # "gnome-connections",
        "gnome-console",
        "gnome-contacts",
        "gnome-disk-utility",
        "gnome-font-viewer",
        "gnome-maps",
        # "gnome-music",
        # "gnome-remote-desktop",
        "gnome-shell-extensions",
        "gnome-software",
        "gnome-system-monitor",
        "gnome-text-editor",
        "gnome-tour",
        "gnome-user-docs",
        # "gnome-user-share",
        "gnome-weather",
        "orca",
        # "phodav",
        "simple-scan",
        "snapshot",
        "sushi",
        "totem",
    ]
    return []
