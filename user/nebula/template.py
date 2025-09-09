pkgname = "nebula"
pkgver = "1.9.7"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.Build={pkgver}",
    "./cmd/nebula",
    "./cmd/nebula-cert",
]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Overlay networking tool"
license = "MIT"
url = "https://github.com/slackhq/nebula"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b8ca239c6c728deadbb28927c5332e4abf0466121d76616827adbaabbba32d05"
# depends on host environment
options = ["!check"]


def install(self):
    self.install_bin("build/nebula*", glob=True)
    self.install_service(self.files_path / "nebula")
    self.install_file("examples/config.yml", "usr/share/nebula")
    self.install_license("LICENSE")
