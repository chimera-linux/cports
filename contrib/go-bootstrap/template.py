pkgname = "go-bootstrap"
pkgver = "1.19.1"
pkgrel = 0
# just in case
depends = ["!go"]
pkgdesc = "Go programming language bootstrap toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://go.dev"
options = ["!strip", "!scanrundeps", "!lintstatic", "foreignelf", "execstack"]

match self.profile().goarch:
    case "arm64":
        sha256 = (
            "33d348597dd9685a0f06ed71603836718a18b8321c1a6288430b92804b3300ee"
        )
    case "ppc64le":
        sha256 = (
            "0edbe77b7ed3d85c1f03864bb2ad85f92af739014ad1fc9fb011173c0607eb3d"
        )
    case "riscv64":
        sha256 = (
            "bac78ae4493652c8df18fff4151304d907fe1c033f1b08888ecf1dbed93df7bb"
        )
    case "amd64":
        sha256 = (
            "cb2aed391ab73c579d0d0bef9900a90d4526c2197d6aa0c1f22df05084adf090"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"

source = f"https://repo.chimera-linux.org/distfiles/go-bootstrap-{pkgver}-{self.profile().goarch or ''}.tar.xz"


def do_install(self):
    self.install_license("LICENSE")
    self.install_files("bin", "usr/lib/go-bootstrap")
    self.install_files("src", "usr/lib/go-bootstrap")
    self.install_files("pkg", "usr/lib/go-bootstrap")
