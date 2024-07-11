# in general do not use this; look if it can be patched for libedit first
# there are APIs in readline that are not provided by libedit (usually
# really bad ones) and sometimes we cannot just replace it
pkgname = "readline"
# use a git revision so we don't have to deal with the stupid patches
_gitrev = "5d4d92f221d6aac4be445bdd8cd9b48d9ac33f04"
pkgver = "8.2.010"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-multibyte",
    "--with-curses",
    "bash_cv_termcap_lib=libncursesw",
]
# broken af
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel"]
pkgdesc = "GNU Readline library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://tiswww.cwru.edu/php/chet/readline/rltop.html"
source = f"https://git.savannah.gnu.org/cgit/readline.git/snapshot/readline-{_gitrev}.tar.gz"
sha256 = "08b86f4db02481b4105d62f137fa6469bcb5d16ffc01bccb9c3d1be83d33974e"


def post_install(self):
    self.uninstall("usr/share/doc")


@subpackage("libhistory")
def _history(self):
    self.subdesc = "history library"

    return ["usr/lib/libhistory.so.*"]


@subpackage("readline-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/info"])
