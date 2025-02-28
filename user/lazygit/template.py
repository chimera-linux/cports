pkgname = "lazygit"
pkgver = "0.48.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}"]
hostmakedepends = ["go"]
depends = ["git"]
pkgdesc = "Terminal UI for git commands"
license = "MIT"
url = "https://github.com/jesseduffield/lazygit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b8507602e19a0ab7b1e2c9f26447df87d068be9bf362394106bad8a56ce25f82"
# need to be in git checkout
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
