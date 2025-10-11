pkgname = "tig"
pkgver = "2.6.0"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
make_install_args = ["install-doc-man"]
hostmakedepends = ["automake", "asciidoc", "xmlto", "pkgconf"]
makedepends = ["ncurses-devel"]
depends = ["git"]
pkgdesc = "Text-mode interface for git"
license = "GPL-2.0-or-later"
url = "https://github.com/jonas/tig"
source = f"{url}/releases/download/tig-{pkgver}/tig-{pkgver}.tar.gz"
sha256 = "99d4a0fdd3d93547ebacfe511195cb92e4f75b91644c06293c067f401addeb3e"
# test suite tries to access /dev/tty which fails
options = ["!check"]


def post_install(self):
    self.install_completion("contrib/tig-completion.bash", "bash")
    self.install_completion("contrib/tig-completion.zsh", "zsh")
