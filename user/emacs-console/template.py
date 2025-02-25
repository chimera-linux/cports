pkgname = "emacs-console"
pkgver = "30.1"
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
hostmakedepends = [
    "automake",
    "gawk",
    "gcc-jit-libs",
    "pkgconf",
    "texinfo",
]
makedepends = [
    "acl-devel",
    "glib-devel",
    "gcc-jit-devel",
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
maintainer = "roastveg <louis@hamptonsoftworks.com>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/emacs/emacs.html"
source = f"https://ftp.gnu.org/gnu/emacs/emacs-{pkgver}.tar.xz"
sha256 = "6ccac1ae76e6af93c6de1df175e8eb406767c23da3dd2a16aa67e3124a6f138f"
# CFI: breaks
hardening = ["vis", "!cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_sysusers(self.files_path / "emacs.conf", name="emacs")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf", name="emacs")
    # remove suid from game exe
    (
        self.destdir
        / f"usr/libexec/emacs/{pkgver}/{self.profile().triplet}/update-game-score"
    ).chmod(0o755)

    self.uninstall("usr/lib/systemd/user")
    self.uninstall("var/games")

    # conflicts with ctags
    self.rename("usr/bin/ctags", "ctags.emacs")
    self.rename("usr/share/man/man1/ctags.1.gz", "ctags.emacs.1.gz")
