pkgname = "tig"
pkgver = "2.5.8"
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
sha256 = "b70e0a42aed74a4a3990ccfe35262305917175e3164330c0889bd70580406391"
# test suite tries to access /dev/tty which fails
options = ["!check"]


def post_install(self):
    self.install_completion("contrib/tig-completion.bash", "bash")
    self.install_completion("contrib/tig-completion.zsh", "zsh")
