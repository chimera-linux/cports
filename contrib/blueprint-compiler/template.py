pkgname = "blueprint-compiler"
pkgver = "0.12.0"
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
checkdepends = ["xwayland-run"] + depends
pkgdesc = "Markup language compiler for GTK user interfaces"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later"
url = "https://jwestman.pages.gitlab.gnome.org/blueprint-compiler"
source = f"https://gitlab.gnome.org/jwestman/blueprint-compiler/-/archive/v{pkgver}/blueprint-compiler-v{pkgver}.tar.gz"
sha256 = "6dbb4ea851cec164030abded5949ea77ff92032e23527e1c0597d7efe0c36a81"
