pkgname = "emacs-console"
pkgver = "29.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-gameuser=:_games",
    "--with-gpm",
    "--with-json",
    "--without-file-notification",
    "--without-sound",
    "--without-x",
]
make_cmd = "gmake"
hostmakedepends = [
    "autoconf",
    "automake",
    "gawk",
    "gmake",
    "pkgconf",
    "texinfo",
]
makedepends = [
    "acl-devel",
    "glib-devel",
    "gmp-devel",
    "gnutls-devel",
    "jansson-devel",
    "lcms2-devel",
    "libxml2-devel",
    "linux-headers",
    "ncurses-devel",
    "tree-sitter-devel",
]
provides = [f"emacs={pkgver}"]
provider_priority = 0
pkgdesc = "Extensible, customizable, self-documenting, real-time display editor"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/emacs/emacs.html"
source = f"https://ftp.gnu.org/gnu/emacs/emacs-{pkgver}.tar.xz"
sha256 = "d2f881a5cc231e2f5a03e86f4584b0438f83edd7598a09d24a21bd8d003e2e01"
# FIXME cfi: breaks
hardening = ["vis"]
# no tests
options = ["!check"]

system_groups = ["_games"]


def post_install(self):
    # remove suid from game exe
    (
        self.destdir
        / f"usr/libexec/emacs/{pkgver}/{self.profile().triplet}/update-game-score"
    ).chmod(0o755)
