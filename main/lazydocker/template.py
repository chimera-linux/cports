pkgname = "lazydocker"
pkgver = "0.23.3"
pkgrel = 5
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.version={pkgver} -X main.buildSource=release",
]
hostmakedepends = ["go"]
pkgdesc = "TUI for docker resource visualization and management"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jesseduffield/lazydocker"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6ea52b69c3fb5cb371a01e55d1deeaf053b17fb240be069af577246c5169f4f1"


def post_install(self):
    self.install_license("LICENSE")
