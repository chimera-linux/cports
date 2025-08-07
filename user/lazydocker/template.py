pkgname = "lazydocker"
pkgver = "0.24.1"
pkgrel = 8
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.version={pkgver} -X main.buildSource=release",
]
hostmakedepends = ["go"]
pkgdesc = "TUI for docker resource visualization and management"
license = "MIT"
url = "https://github.com/jesseduffield/lazydocker"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f54197d333a28e658d2eb4d9b22461ae73721ec9e4106ba23ed177fc530c21f4"


def post_install(self):
    self.install_license("LICENSE")
