pkgname = "blueprint-compiler"
pkgver = "0.16.0"
pkgrel = 2
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
sha256 = "01feb8263fe7a450b0a9fed0fd54cf88947aaf00f86cc7da345f8b39a0e7bd30"
