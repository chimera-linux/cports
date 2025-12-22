pkgname = "lazygit"
pkgver = "0.57.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}"]
hostmakedepends = ["go"]
depends = ["git"]
pkgdesc = "Terminal UI for git commands"
license = "MIT"
url = "https://github.com/jesseduffield/lazygit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "19789e74db57f0fdd80a43f284edc549bd25319c922149ed754bdd7cfe9004cf"
# need to be in git checkout
options = ["!check"]

if self.profile().arch in ["loongarch64"]:
    broken = (
        "vendor/github.com/creack/pty/pty_linux.go:39:8: undefined: _C_uint"
    )


def post_install(self):
    self.install_license("LICENSE")
