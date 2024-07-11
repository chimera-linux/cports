pkgname = "bemenu"
pkgver = "0.6.22"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["scdoc", "gmake", "pkgconf", "wayland-progs"]
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
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "2bd579c37986797bb1bcc8f475cae4cd4c7d59eec479fdb1ae680493fdd34abb"
hardening = ["vis", "!cfi"]
# no check target defined
options = ["!check"]


@subpackage("bemenu-devel")
def _devel(self):
    return self.default_devel()


def _subpkg(sname, sdesc):
    @subpackage(f"bemenu-{sname}")
    def _spkg(self):
        self.subdesc = "{sdesc} backend"
        self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
        self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

        return [f"usr/lib/bemenu/bemenu-renderer-{sname}.so"]


for _sname, _sdesc in [
    ("curses", "curses"),
    ("wayland", "Wayland"),
    ("x11", "X11"),
]:
    _subpkg(_sname, _sdesc)
