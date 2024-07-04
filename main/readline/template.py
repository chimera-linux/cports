# in general do not use this; look if it can be patched for libedit first
# there are APIs in readline that are not provided by libedit (usually
# really bad ones) and sometimes we cannot just replace it
pkgname = "readline"
# use a git revision so we don't have to deal with the stupid patches
_gitrev = "7274faabe97ce53d6b464272d7e6ab6c1392837b"
pkgver = "8.2.001"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-curses",
    "--enable-multibyte",
    "bash_cv_termcap_lib=libncursesw",
    "--disable-static",
]
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel"]
pkgdesc = "GNU Readline library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://tiswww.cwru.edu/php/chet/readline/rltop.html"
source = f"http://git.savannah.gnu.org/cgit/{pkgname}.git/snapshot/{pkgname}-{_gitrev}.tar.gz"
sha256 = "a492621bc1dcf18ee89851942ad1752025ffaae661a5cd9f188f54f892989e77"


def post_install(self):
    self.uninstall("usr/share/doc")


@subpackage("libhistory")
def _history(self):
    self.pkgdesc = f"{pkgdesc} (history library)"

    return ["usr/lib/libhistory.so.*"]


@subpackage("readline-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/info"])


configure_gen = []
