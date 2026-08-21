pkgname = "lazydocker"
pkgver = "0.25.2"
pkgrel = 1
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.version={pkgver} -X main.buildSource=release",
]
hostmakedepends = ["go"]
pkgdesc = "TUI for docker resource visualization and management"
license = "MIT"
url = "https://github.com/jesseduffield/lazydocker"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "405071220e5be9aa061c65d290e0347143b73ae0a3cc01df164f0105de2b53c4"


def post_install(self):
    self.install_license("LICENSE")
