pkgname = "tig"
pkgver = "2.5.9"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
make_install_args = ["install-doc-man"]
hostmakedepends = ["gmake", "automake", "asciidoc", "xmlto", "pkgconf"]
makedepends = ["ncurses-devel"]
depends = ["git"]
pkgdesc = "Text-mode interface for git"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-2.0-or-later"
url = "https://github.com/jonas/tig"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "0cb4d9e3de00dc92aaa7996e1517845bd9b9a0d4368f3206f618d813e8db8b39"
# test suite tries to access /dev/tty which fails
options = ["!check"]


def post_install(self):
    self.install_completion("contrib/tig-completion.bash", "bash")
    self.install_completion("contrib/tig-completion.zsh", "zsh")
