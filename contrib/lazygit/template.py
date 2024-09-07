pkgname = "lazygit"
pkgver = "0.44.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
depends = ["git"]
pkgdesc = "Terminal UI for git commands"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "MIT"
url = "https://github.com/jesseduffield/lazygit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6cf617510127892f3ede2aea767ce725197902418ef7087c1cf0e91f06d00a16"
# need to be in git checkout
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
