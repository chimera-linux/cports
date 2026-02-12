pkgname = "lazygit"
pkgver = "0.58.1"
pkgrel = 1
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}"]
hostmakedepends = ["go"]
depends = ["git"]
pkgdesc = "Terminal UI for git commands"
license = "MIT"
url = "https://github.com/jesseduffield/lazygit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e4f0d4f3cebc70a802f95c52265e34ee879265103ebb70b5dd449ae791d0cbbb"
# need to be in git checkout
options = ["!check"]

if self.profile().arch in ["loongarch64"]:
    broken = (
        "vendor/github.com/creack/pty/pty_linux.go:39:8: undefined: _C_uint"
    )


def post_install(self):
    self.install_license("LICENSE")
