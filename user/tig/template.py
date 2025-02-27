pkgname = "tig"
pkgver = "2.5.12"
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
sha256 = "5dda8a098810bb499096e17fc9f69c0a5915a23f46be27209fc8195d7a792108"
# test suite tries to access /dev/tty which fails
options = ["!check"]


def post_install(self):
    self.install_completion("contrib/tig-completion.bash", "bash")
    self.install_completion("contrib/tig-completion.zsh", "zsh")
