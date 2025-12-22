pkgname = "lazygit"
pkgver = "0.58.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}"]
hostmakedepends = ["go"]
depends = ["git"]
pkgdesc = "Terminal UI for git commands"
license = "MIT"
url = "https://github.com/jesseduffield/lazygit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9f714b3d35fa7cae5a2193cf11a2e9bc97bd0a9bbf52ccaea432765bf8f63f3c"
# need to be in git checkout
options = ["!check"]

if self.profile().arch in ["loongarch64"]:
    broken = (
        "vendor/github.com/creack/pty/pty_linux.go:39:8: undefined: _C_uint"
    )


def post_install(self):
    self.install_license("LICENSE")
