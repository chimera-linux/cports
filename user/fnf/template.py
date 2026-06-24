pkgname = "fnf"
pkgver = "0.4"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers"]
pkgdesc = "CLI fuzzy finder"
license = "MIT"
url = "https://github.com/leo-arch/fnf"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "13aa1c1bddfa6be4f458af3e077ed0c1bbd91400d89cf670c1a10cafd525c8f5"


def post_install(self):
    self.install_license("LICENSE")
    self.install_bin("contrib/fnf-dvtm")
    self.install_bin("contrib/fnf-tmux")
    self.install_files("contrib/key-bindings.zsh", "usr/share/fnf")
