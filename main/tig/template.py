pkgname = "tig"
pkgver = "2.5.10"
pkgrel = 1
build_style = "gnu_configure"
make_dir = "."
make_install_args = ["install-doc-man"]
hostmakedepends = ["automake", "asciidoc", "xmlto", "pkgconf"]
makedepends = ["ncurses-devel"]
depends = ["git"]
pkgdesc = "Text-mode interface for git"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-2.0-or-later"
url = "https://github.com/jonas/tig"
source = f"{url}/releases/download/tig-{pkgver}/tig-{pkgver}.tar.gz"
sha256 = "f655cc1366fc10058a2bd505bb88ca78e653ff7526c1b81774c44b9d841210e3"
# test suite tries to access /dev/tty which fails
options = ["!check"]


def post_install(self):
    self.install_completion("contrib/tig-completion.bash", "bash")
    self.install_completion("contrib/tig-completion.zsh", "zsh")
