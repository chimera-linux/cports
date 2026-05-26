pkgname = "blueprint-compiler"
pkgver = "0.20.4"
pkgrel = 1
build_style = "meson"
make_check_args = ["--timeout-multiplier", "3"]
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
sha256 = "6f0f72fbce0919045047f30b56590e71cd82c66b890c37fe765a40494fd34feb"
