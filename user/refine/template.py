pkgname = "refine"
pkgver = "0.5.7"
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
sha256 = "d1e11b7fb2cc6248a95c0cc0c32a6e5b1460216b923803bd935b13cf3574f8fc"
