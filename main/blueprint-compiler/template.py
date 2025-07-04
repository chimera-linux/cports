pkgname = "blueprint-compiler"
pkgver = "0.18.0"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "meson",
    "pkgconf",
]
depends = [
    "gtk4",
    "libadwaita",
    "python-gobject",
]
checkdepends = ["xwayland-run", *depends]
pkgdesc = "Markup language compiler for GTK user interfaces"
license = "LGPL-3.0-or-later"
url = "https://gnome.pages.gitlab.gnome.org/blueprint-compiler"
source = f"https://gitlab.gnome.org/GNOME/blueprint-compiler/-/archive/v{pkgver}/blueprint-compiler-v{pkgver}.tar.gz"
sha256 = "703c7ccd23cb6f77a8fe9c8cae0f91de9274910ca953de77135b6e79dbff1fc3"
