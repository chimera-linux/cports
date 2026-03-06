pkgname = "lazydocker"
pkgver = "0.24.4"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.version={pkgver} -X main.buildSource=release",
]
hostmakedepends = ["go"]
pkgdesc = "TUI for docker resource visualization and management"
license = "MIT"
url = "https://github.com/jesseduffield/lazydocker"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f8299de3c1a86b81ff70e2ae46859fc83f2b69e324ec5a16dd599e8c49fb4451"


def post_install(self):
    self.install_license("LICENSE")
