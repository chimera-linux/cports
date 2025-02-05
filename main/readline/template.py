# in general do not use this; look if it can be patched for libedit first
# there are APIs in readline that are not provided by libedit (usually
# really bad ones) and sometimes we cannot just replace it
pkgname = "readline"
# use a git revision so we don't have to deal with the stupid patches
_gitrev = "037d85f199a8c6e5b16689a46c8bc31b586a0c94"
pkgver = "8.2.013"
pkgrel = 1
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
sha256 = "86959fc06a4ad8a3852b68ce67f5bb2f98d7d95548bbfc5c87e806042a8567e1"


def post_install(self):
    self.uninstall("usr/share/doc")


@subpackage("readline-devel")
def _(self):
    return self.default_devel(extra=["usr/share/info"])
