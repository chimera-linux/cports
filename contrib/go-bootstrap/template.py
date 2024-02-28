pkgname = "go-bootstrap"
pkgver = "1.21.7"
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
            "15adfc838d635de3d21b48fad22d45d266fa1f691749e7072eeb5ae8eed2da06"
        )
    case "ppc64le":
        sha256 = (
            "9b19aca596c1f04fe87b2089a83ffdde02674615fbb180d1777960eb27ad28d6"
        )
    case "riscv64":
        sha256 = (
            "5ec7254b60e75b4f910615020e0c5d21305a127ede1b60c28d440e095b2445f6"
        )
    case "amd64":
        sha256 = (
            "274ecc1b63183d372d61609d5cf6c8527c20abf8fb401ffb1aa438e6b103f12e"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"

source = f"https://repo.chimera-linux.org/distfiles/go-bootstrap-{pkgver}-{self.profile().goarch or ''}.tar.xz"


def do_install(self):
    self.install_license("LICENSE")
    self.install_files("bin", "usr/lib/go-bootstrap")
    self.install_files("src", "usr/lib/go-bootstrap")
    self.install_files("pkg", "usr/lib/go-bootstrap")
