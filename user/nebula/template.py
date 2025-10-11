pkgname = "nebula"
pkgver = "1.9.6"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.Build={pkgver}",
    "./cmd/nebula",
    "./cmd/nebula-cert",
]
hostmakedepends = ["go"]
pkgdesc = "Overlay networking tool"
license = "MIT"
url = "https://github.com/slackhq/nebula"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cb0246ee02e03d84237f0a8e0daf6236ea65d299c275bcd4f2d324a66d1d738b"
# depends on host environment
options = ["!check"]


def install(self):
    self.install_bin("build/nebula*", glob=True)
    self.install_service(self.files_path / "nebula")
    self.install_file("examples/config.yml", "usr/share/nebula")
    self.install_license("LICENSE")
