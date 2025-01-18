pkgname = "lazygit"
pkgver = "0.45.2"
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
sha256 = "dd3d6645ee429f0c554338c1fdb940733793ad915ae72653132664aa7c26bbcb"
# need to be in git checkout
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
