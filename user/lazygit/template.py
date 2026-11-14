pkgname = "lazygit"
pkgver = "0.66.3"
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
sha256 = "49e80d28e03e53048105f6ebb5afefbe5caacffa8549347d8a59eab3a00dafe1"
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
