pkgname = "fnf"
pkgver = "0.2"
pkgrel = 1
build_style = "makefile"
pkgdesc = "CLI fuzzy finder"
license = "MIT"
url = "https://github.com/leo-arch/fnf"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2b31b19d2eb71d20854ec34f26ae1258c22b7cba5b634fd85728c0a5f4e6dd68"


def post_install(self):
    self.install_license("LICENSE")
    self.install_bin("contrib/fnf-dvtm")
    self.install_bin("contrib/fnf-tmux")
