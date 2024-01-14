pkgname = "gdb"
pkgver = "14.1"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--disable-werror",
    "--disable-nls",
    "--with-system-zlib",
    "--with-system-readline",
    "--with-system-gdbinit=/etc/gdb/gdbinint",
    "--with-python=/usr/bin/python",
]
# needs autoconf 2.69
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "texinfo", "python-devel"]
makedepends = [
    "gettext-devel",
    "gmp-devel",
    "libexpat-devel",
    "linux-headers",
    "mpfr-devel",
    "ncurses-devel",
    "python-devel",
    "readline-devel",
    "zlib-devel",
]
depends = [f"gdb-common={pkgver}-r{pkgrel}"]
pkgdesc = "GNU debugger"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gdb"
source = f"$(GNU_SITE)/gdb/gdb-{pkgver}.tar.xz"
sha256 = "d66df51276143451fcbff464cc8723d68f1e9df45a6a2d5635a54e71643edb80"
# massive
options = ["!check", "!cross"]


def post_install(self):
    from cbuild.util import python

    self.rm(self.destdir / "usr/lib", recursive=True)
    self.rm(self.destdir / "usr/include", recursive=True)
    # may conflict with binutils
    self.rm(self.destdir / "usr/share/info/bfd.info")
    self.rm(self.destdir / "usr/share/info/ctf-spec.info")

    python.precompile(self, "usr/share/gdb/python")


@subpackage("gdb-common")
def _common(self):
    self.pkgdesc = f"{pkgdesc} (common files)"

    return ["usr/share"]
