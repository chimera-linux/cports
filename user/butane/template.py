pkgname = "butane"
pkgver = "0.25.1"
pkgrel = 0
build_style = "go"
make_dir = "bin"
make_build_args = [
    f"-ldflags=-X github.com/coreos/butane/internal/version.Raw={pkgver}",
    "./internal/main.go",
]
hostmakedepends = ["go"]
depends = []
pkgdesc = (
    "Converts friendly Butane Configs into machine-readable Ignition Configs"
)
license = "Apache-2.0"
url = "https://coreos.github.io/butane"
source = f"https://github.com/coreos/butane/archive/v{pkgver}.tar.gz"
sha256 = "14203e7fa13f5753e332c472d0d7be3fc7ddf9a637873463793d898bb61cf69c"


def install(self):
    self.install_bin(f"{self.make_dir}/main", name="butane")
