pkgname = "gnome-tweaks"
pkgver = "49.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libgudev-devel",
    "python-gobject-devel",
]
depends = [
    "gnome-settings-daemon",
    "gnome-shell",
    "libadwaita",
    "python-gobject",
    "sound-theme-freedesktop",
]
pkgdesc = "GNOME tweak tool"
license = "GPL-3.0-or-later AND CC0-1.0"
url = "https://wiki.gnome.org/Apps/Tweaks"
source = (
    f"$(GNOME_SITE)/gnome-tweaks/{pkgver[:-2]}/gnome-tweaks-{pkgver}.tar.xz"
)
sha256 = "b3909bdcb4905b68427d6ab581e01f436dff8e5c0a389b1e0b14500f18806ebb"
