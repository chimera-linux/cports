# in general do not use this; look if it can be patched for libedit first
# there are APIs in readline that are not provided by libedit (usually
# really bad ones) and sometimes we cannot just replace it
pkgname = "readline"
# use a git revision so we don't have to deal with the stupid patches
_gitrev = "447b8290b3e2e2d117dc8e9cdb83b0dc6448a638"
pkgver = "8.3"
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
license = "GPL-3.0-or-later"
url = "https://tiswww.cwru.edu/php/chet/readline/rltop.html"
source = f"https://git.savannah.gnu.org/cgit/readline.git/snapshot/readline-{_gitrev}.tar.gz"
sha256 = "0affa0b657cadd7c63109e99ad5801dff0ba4841395b824d55b4cd52396fff74"


def post_install(self):
    self.uninstall("usr/share/doc")


@subpackage("readline-devel")
def _(self):
    return self.default_devel(extra=["usr/share/info"])
