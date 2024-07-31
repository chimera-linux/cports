pkgname = "gdb"
pkgver = "15.1"
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
hostmakedepends = ["gmake", "gsed", "pkgconf", "texinfo", "python-devel"]
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gdb"
source = f"$(GNU_SITE)/gdb/gdb-{pkgver}.tar.xz"
sha256 = "38254eacd4572134bca9c5a5aa4d4ca564cbbd30c369d881f733fb6b903354f2"
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
def _common(self):
    self.subdesc = "common files"

    return ["usr/share"]
