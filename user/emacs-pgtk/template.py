pkgname = "emacs-pgtk"
pkgver = "31.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-gameuser=:_games",
    "--with-gpm",
    "--with-jpeg",
    "--with-json",
    "--with-pgtk",
    "--with-webp",
    "--with-x-toolkit=gtk3",
    "--without-tiff",
]
make_check_args = [
    "EXCLUDE_TESTS="
    " %eglot-tests.el"  # requires a variety of lsp servers
    " %tramp-tests.el"  # TODO: fails mysteriously
    " %shr-tests.el"  # TODO: zoom-image times out
    " %process-tests.el"  # TODO: times out
    " %package-vc-tests.el"  # TODO: hangs
]
hostmakedepends = [
    "automake",
    "ctags",
    "gawk",
    "pkgconf",
    "texinfo",
]
makedepends = [
    "acl-devel",
    "alsa-lib-devel",
    "fontconfig-devel",
    "giflib-devel",
    "glib-devel",
    "gmp-devel",
    "gnutls-devel",
    "gtk+3-devel",
    "harfbuzz-devel",
    "lcms2-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libwebp-devel",
    "libxml2-devel",
    "linux-headers",
    "ncurses-devel",
    "pango-devel",
    "sqlite-devel",
    "tree-sitter-devel",
]
checkdepends = ["bash", "git", "mandoc"]
depends = ["ctags"]
provides = [f"emacs={pkgver}"]
provider_priority = 20
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
