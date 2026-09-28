pkgname = "gdb"
pkgver = "17.2"
pkgrel = 0
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
hostmakedepends = ["gsed", "pkgconf", "texinfo", "python-devel"]
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
depends = [self.with_pkgver("gdb-common")]
pkgdesc = "GNU debugger"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gdb"
source = f"$(GNU_SITE)/gdb/gdb-{pkgver}.tar.xz"
sha256 = "1c036c0d72e4b3d1fb5c94c88632add6f9d76f4d7c4d2ea793c12a9f19a3228c"
# weird autotools bullshittery
env = {"SED": "gsed"}
# massive
options = ["!check", "!cross"]


def post_install(self):
    from cbuild.util import python

    self.uninstall("usr/lib")
    self.uninstall("usr/include")
    # may conflict with binutils
    self.uninstall("usr/share/info/bfd.info")
    self.uninstall("usr/share/info/ctf-spec.info")
    self.uninstall("usr/share/info/sframe-spec.info")

    python.precompile(self, "usr/share/gdb/python")


@subpackage("gdb-common")
def _(self):
    self.subdesc = "common files"

    return ["usr/share"]
