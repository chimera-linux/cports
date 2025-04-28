pkgname = "refine"
pkgver = "0.5.8"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "meson",
    "ninja",
    "pkgconf",
]
depends = [
    "gtk4",
    "libadwaita",
    "libportal",
    "libportal-gtk4",
    "pango",
    "python-gobject",
]
pkgdesc = "Tweak various aspects of GNOME"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/TheEvilSkeleton/Refine"
source = f"{url}/-/archive/{pkgver}/Refine-{pkgver}.tar.bz2"
sha256 = "e48270efd87ef080877586e73baf0918d35cde21e354185d268cbbd46ec83a95"
