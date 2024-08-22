pkgname = "bemenu"
pkgver = "0.6.23"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["scdoc", "pkgconf", "wayland-progs"]
makedepends = [
    "cairo-devel",
    "libx11-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "ncurses-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Dynamic menu library and client program inspired by dmenu"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "GPL-3.0-only AND LGPL-3.0-only"
url = "https://github.com/Cloudef/bemenu"
source = f"{url}/releases/download/{pkgver}/bemenu-{pkgver}.tar.gz"
sha256 = "7cd336fb827b50a12c398a5daf6d2e6a07e291217116e725e7f1e021d9e0cdd9"
hardening = ["vis", "!cfi"]
# no check target defined
options = ["!check"]


@subpackage("bemenu-devel")
def _(self):
    return self.default_devel()


def _subpkg(sname, sdesc):
    @subpackage(f"bemenu-{sname}")
    def _(self):
        self.subdesc = f"{sdesc} backend"
        self.depends = [self.parent]
        self.install_if = [self.parent]

        return [f"usr/lib/bemenu/bemenu-renderer-{sname}.so"]


for _sname, _sdesc in [
    ("curses", "curses"),
    ("wayland", "Wayland"),
    ("x11", "X11"),
]:
    _subpkg(_sname, _sdesc)
