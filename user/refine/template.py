pkgname = "refine"
pkgver = "0.5.2"
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
sha256 = "2e0d5bc3bd709b727c306e6d430c92f06d32eec77034f7a107ee0dbbb55227b5"
