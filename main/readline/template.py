# in general do not use this; look if it can be patched for libedit first
# there are APIs in readline that are not provided by libedit (usually
# really bad ones) and sometimes we cannot just replace it
pkgname = "readline"
# use a git revision so we don't have to deal with the stupid patches
_gitrev = "9ba3434aa5434e509300a3722b0479fd30480b44"
pkgver = "8.1.001"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-curses", "--enable-multibyte", "bash_cv_termcap_lib=libncursesw",
    "--disable-static",
]
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel"]
pkgdesc = "GNU Readline library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://tiswww.cwru.edu/php/chet/readline/rltop.html"
source = f"http://git.savannah.gnu.org/cgit/{pkgname}.git/snapshot/{pkgname}-{_gitrev}.tar.gz"
sha256 = "a5064095f96eac70e53545525c127f6d39b3ee0b7effcdc7c75ece27960e93e2"

def post_install(self):
    self.rm(self.destdir / "usr/share/doc", recursive = True)

@subpackage("libhistory")
def _history(self):
    self.pkgdesc = f"{pkgdesc} (history library)"

    return ["usr/lib/libhistory.so.*"]

@subpackage("readline-devel")
def _devel(self):
    return self.default_devel(man = True, extra = ["usr/share/info"])
