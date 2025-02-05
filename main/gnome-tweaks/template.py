pkgname = "gnome-tweaks"
pkgver = "46.1"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later AND CC0-1.0"
url = "https://wiki.gnome.org/Apps/Tweaks"
source = (
    f"$(GNOME_SITE)/gnome-tweaks/{pkgver[:-2]}/gnome-tweaks-{pkgver}.tar.xz"
)
sha256 = "2f192a7085fbd6843ecf825716d9da21ec9272029149ea35f3e159e0ac309b80"
