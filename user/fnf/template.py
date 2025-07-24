pkgname = "fnf"
pkgver = "0.3.1"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers"]
pkgdesc = "CLI fuzzy finder"
license = "MIT"
url = "https://github.com/leo-arch/fnf"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3a65de45f68419528e5fa57d9857aa208f4802ba85de267a09734d7231b6d1eb"


def post_install(self):
    self.install_license("LICENSE")
    self.install_bin("contrib/fnf-dvtm")
    self.install_bin("contrib/fnf-tmux")
