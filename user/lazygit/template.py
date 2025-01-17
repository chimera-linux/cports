pkgname = "lazygit"
pkgver = "0.45.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}"]
hostmakedepends = ["go"]
depends = ["git"]
pkgdesc = "Terminal UI for git commands"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "MIT"
url = "https://github.com/jesseduffield/lazygit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "11bb69916a32a22d29c90196f18af633bcf22bec2b84a675222edfb6c1f89a87"
# need to be in git checkout
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
