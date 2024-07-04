pkgname = "gdb"
pkgver = "14.2"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--disable-werror",
    "--disable-nls",
    "--with-system-zlib",
    "--with-system-zstd",
    "--with-system-readline",
    "--with-system-gdbinit=/etc/gdb/gdbinint",
    "--with-python=/usr/bin/python",
]
# needs autoconf 2.69
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "texinfo", "python-devel"]
makedepends = [
    "elfutils-devel",
    "gettext-devel",
    "gmp-devel",
    "libexpat-devel",
    "linux-headers",
    "mpfr-devel",
    "ncurses-devel",
    "python-devel",
    "readline-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = [f"gdb-common={pkgver}-r{pkgrel}"]
pkgdesc = "GNU debugger"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gdb"
source = f"$(GNU_SITE)/gdb/gdb-{pkgver}.tar.xz"
sha256 = "2d4dd8061d8ded12b6c63f55e45344881e8226105f4d2a9b234040efa5ce7772"
# massive
options = ["!check", "!cross"]


def post_install(self):
    from cbuild.util import python

    self.uninstall("usr/lib")
    self.uninstall("usr/include")
    # may conflict with binutils
    self.uninstall("usr/share/info/bfd.info")
    self.uninstall("usr/share/info/ctf-spec.info")

    python.precompile(self, "usr/share/gdb/python")


@subpackage("gdb-common")
def _common(self):
    self.pkgdesc = f"{pkgdesc} (common files)"

    return ["usr/share"]
