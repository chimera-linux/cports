pkgname = "emacs-pgtk"
pkgver = "30.2"
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
    " %tramp-tests.el"  # fails mysteriously TODO
    " %shr-tests.el"  # TODO zoom-image times out
]
hostmakedepends = [
    "automake",
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
provides = [f"emacs={pkgver}"]
provider_priority = 20
pkgdesc = "Extensible, customizable, self-documenting, real-time display editor"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/emacs/emacs.html"
source = f"$(GNU_SITE)/emacs/emacs-{pkgver}.tar.xz"
sha256 = "b3f36f18a6dd2715713370166257de2fae01f9d38cfe878ced9b1e6ded5befd9"
# CFI: breaks
hardening = ["vis", "!cfi"]


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
