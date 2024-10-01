pkgname = "lazygit"
pkgver = "0.44.1"
pkgrel = 1
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}"]
hostmakedepends = ["go"]
depends = ["git"]
pkgdesc = "Terminal UI for git commands"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "MIT"
url = "https://github.com/jesseduffield/lazygit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "02b67d38e07ae89b0ddd3b4917bd0cfcdfb5e158ed771566d3eb81f97f78cc26"
# need to be in git checkout
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
