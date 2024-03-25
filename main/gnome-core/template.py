pkgname = "gnome-core"
pkgver = "46.0"
pkgrel = 0
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
pkgdesc = "GNOME desktop environment (minimal session)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://www.gnome.org"
