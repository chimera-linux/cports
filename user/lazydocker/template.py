pkgname = "lazydocker"
pkgver = "0.25.0"
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
sha256 = "480234dec2dbe989462d177f1aa78debec972893ab5981d48d23d7aec8430a58"


def post_install(self):
    self.install_license("LICENSE")
