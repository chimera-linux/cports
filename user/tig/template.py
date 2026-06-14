pkgname = "tig"
pkgver = "2.6.1"
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
sha256 = "5adeabdcd93aa0423d618da8b878b53482bef6e0e9e1fe224acc0f18031fe91e"
# test suite tries to access /dev/tty which fails
options = ["!check"]


def post_install(self):
    self.install_completion("contrib/tig-completion.bash", "bash")
    self.install_completion("contrib/tig-completion.zsh", "zsh")
