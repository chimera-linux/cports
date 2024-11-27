pkgname = "blueprint-compiler"
pkgver = "0.14.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://jwestman.pages.gitlab.gnome.org/blueprint-compiler"
source = f"https://gitlab.gnome.org/jwestman/blueprint-compiler/-/archive/v{pkgver}/blueprint-compiler-v{pkgver}.tar.gz"
sha256 = "05faf3810cb76d4e2d2382c6a7e6c8096af27e144e2260635c97f6a173d67234"
