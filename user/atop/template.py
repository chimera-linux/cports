pkgname = "atop"
pkgver = "2.13.0"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "SBINPATH=/usr/bin",
]
make_install_target = "genericinstall"
make_install_args = [*make_build_args]
hostmakedepends = [
    "clang",
    "gmake",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "linux-headers",
    "ncurses-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "ASCII full-screen performance monitor"
license = "GPL-2.0-only"
url = "https://github.com/Atoptool/atop"
source = f"https://github.com/Atoptool/atop/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5ee38c93afd64767a09a06698a0e90bfc390189a5058d245878a559d476d8572"
tool_flags = {
    # From pkgconf --cflags ncursesw
    "CFLAGS": ["-DNCURSES_WIDECHAR"]
}
# no tests
options = ["!check"]


def post_install(self):
    # /etc/default/atop
    # we don't ship any services that could use it right now
    self.uninstall("etc")
