pkgname = "lazygit"
pkgver = "0.51.1"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}"]
hostmakedepends = ["go"]
depends = ["git"]
pkgdesc = "Terminal UI for git commands"
license = "MIT"
url = "https://github.com/jesseduffield/lazygit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "467fb3988a375dbfd9288beaae89205d39795a0fd7f156b813d52bbcb57f3506"
# need to be in git checkout
options = ["!check"]

if self.profile().arch in ["loongarch64"]:
    broken = (
        "vendor/github.com/creack/pty/pty_linux.go:39:8: undefined: _C_uint"
    )


def post_install(self):
    self.install_license("LICENSE")
