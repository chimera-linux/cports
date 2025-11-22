pkgname = "refine"
pkgver = "0.6.3"
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
sha256 = "58dfc0879b03068aeb2207fe2989f6f2bfed96a4142de837024828cf48a149f8"
