pkgname = "go-bootstrap"
pkgver = "1.23.6"
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
            "e13364ae0ba9545ee0af7120c902bffb8c3749ffb9ef4ed1b46a9a589b8c4e70"
        )
    case "ppc64le":
        sha256 = (
            "c71193824401538ef41cd981b1cf77710b7a35e25c3bad32304e692d365a0d59"
        )
    case "riscv64":
        sha256 = (
            "f5897db05a93e196f4b7abdfd75931a118a1850532b7b6473ddc9fc6da7b8774"
        )
    case "amd64":
        sha256 = (
            "dcadf4d5ac3a7d812538f958509f4a45ef3244b1bae22f8bf5eeea4e3e029fb8"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"

source = f"https://repo.chimera-linux.org/distfiles/go-bootstrap-{pkgver}-{self.profile().goarch or ''}.tar.zst"


def install(self):
    self.install_license("LICENSE")
    self.install_files("bin", "usr/lib/go-bootstrap")
    self.install_files("src", "usr/lib/go-bootstrap")
    self.install_files("pkg", "usr/lib/go-bootstrap")
