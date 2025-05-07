pkgname = "refine"
pkgver = "0.5.9"
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
sha256 = "44311b03a73ccfc67d69db8b2aca676495085a39a16c66300068ff8e833f70a0"
