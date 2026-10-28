pkgname = "lazygit"
pkgver = "0.66.2"
pkgrel = 0
build_style = "go"
prepare_after_patch = True
make_build_args = [f"-ldflags=-X main.version=v{pkgver}"]
hostmakedepends = ["go"]
depends = ["git"]
pkgdesc = "Terminal UI for git commands"
license = "MIT"
url = "https://github.com/jesseduffield/lazygit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fcaad0909af765ef87bd873164a4de78435515ab4d8b04f58d6ad51e8ecd00e5"
# need to be in git checkout
options = ["!check"]

if self.profile.arch in ["loongarch64"]:
    broken = (
        "vendor/github.com/creack/pty/pty_linux.go:39:8: undefined: _C_uint"
    )


def post_extract(self):
    self.rm("vendor", recursive=True)


def post_install(self):
    self.install_license("LICENSE")
