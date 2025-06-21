pkgname = "fnf"
pkgver = "0.1"
pkgrel = 1
build_style = "makefile"
pkgdesc = "CLI fuzzy finder"
license = "MIT"
url = "https://github.com/leo-arch/fnf"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "878eae406a5fdc9e8b88d28c264f772da258ddad8378c50b8e08cbc9ce0df07a"


def post_install(self):
    self.install_license("LICENSE")
    self.install_bin("contrib/fnf-dvtm")
    self.install_bin("contrib/fnf-tmux")
