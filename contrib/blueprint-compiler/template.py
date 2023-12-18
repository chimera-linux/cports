pkgname = "blueprint-compiler"
pkgver = "0.10.0"
pkgrel = 1
build_style = "meson"
make_check_wrapper = ["weston-headless-run"]
hostmakedepends = [
    "meson",
    "pkgconf",
]
depends = [
    "gtk4",
    "libadwaita",
    "python-gobject",
]
checkdepends = ["weston"] + depends
pkgdesc = "Markup language compiler for GTK user interfaces"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later"
url = "https://jwestman.pages.gitlab.gnome.org/blueprint-compiler"
source = f"https://gitlab.gnome.org/jwestman/blueprint-compiler/-/archive/v{pkgver}/blueprint-compiler-v{pkgver}.tar.gz"
sha256 = "2bc729b36897d0959a9890fb0997c9847aa9d2fc9356520bd8a46ed0b51ff4c0"
