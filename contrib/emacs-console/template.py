pkgname = "emacs-console"
pkgver = "29.4"
pkgrel = 1
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
sha256 = "ba897946f94c36600a7e7bb3501d27aa4112d791bfe1445c61ed28550daca235"
# CFI: breaks
hardening = ["vis", "!cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_sysusers(self.files_path / "emacs.conf", name="emacs")
    # remove suid from game exe
    (
        self.destdir
        / f"usr/libexec/emacs/{pkgver}/{self.profile().triplet}/update-game-score"
    ).chmod(0o755)

    self.uninstall("usr/lib/systemd/user")

    # conflicts with ctags
    self.rename("usr/bin/ctags", "ctags.emacs")
    self.rename("usr/share/man/man1/ctags.1.gz", "ctags.emacs.1.gz")
