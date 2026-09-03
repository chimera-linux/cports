pkgname = "emacs-console"
pkgver = "31.1"
pkgrel = 0
build_style = "gnu_configure"
# TODO gccjit (cba to figure it out for now)
configure_args = [
    "--with-gameuser=:_games",
    "--with-gpm",
    "--with-json",
    "--without-file-notification",
    "--without-sound",
    "--without-x",
]
make_check_args = [
    "EXCLUDE_TESTS="
    " %eglot-tests.el"  # requires a variety of lsp servers
    " %tramp-tests.el"  # TODO: fails mysteriously
    " %package-vc-tests.el"  # TODO: hangs
]
hostmakedepends = [
    "automake",
    "gawk",
    "pkgconf",
    "texinfo",
]
makedepends = [
    "acl-devel",
    "glib-devel",
    "gmp-devel",
    "gnutls-devel",
    "lcms2-devel",
    "libxml2-devel",
    "linux-headers",
    "ncurses-devel",
    "tree-sitter-devel",
]
checkdepends = ["bash", "git", "mandoc"]
depends = ["ctags"]
provides = [f"emacs={pkgver}"]
provider_priority = 0
pkgdesc = "Extensible, customizable, self-documenting, real-time display editor"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/emacs/emacs.html"
source = f"$(GNU_SITE)/emacs/emacs-{pkgver}.tar.xz"
sha256 = "1da5790d9580c81932b5bf700633114468da7b3412d69faa767daebf974f4586"


def post_install(self):
    self.install_sysusers(self.files_path / "emacs.conf", name="emacs")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf", name="emacs")
    # remove suid from game exe
    (
        self.destdir
        / f"usr/lib/emacs/{pkgver}/{self.profile().triplet}/update-game-score"
    ).chmod(0o755)

    self.uninstall("usr/lib/systemd/user")
    self.uninstall("var/games")
