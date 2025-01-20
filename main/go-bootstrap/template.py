pkgname = "go-bootstrap"
pkgver = "1.22.4"
pkgrel = 1
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
            "cc3bb22dab758904e4433dc41ba834ea4592ae9a49842cd146dac74f349cbd81"
        )
    case "ppc64le":
        sha256 = (
            "2adec370003b542ff4b73f7a647b4fa4a1b8234751619e5386b148f7b38393ef"
        )
    case "riscv64":
        sha256 = (
            "ff3899e7e17049204e1a8e2fe88bcb3f80c850f95e846ec6a6ef204cdfdff9e5"
        )
    case "amd64":
        sha256 = (
            "289d3bb8b3ff23df4cc346dd88967ff7aa1d2ca7a5aaaadfb0433df8cb2f75de"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"

source = f"https://repo.chimera-linux.org/distfiles/go-bootstrap-{pkgver}-{self.profile().goarch or ''}.tar.xz"


def install(self):
    self.install_license("LICENSE")
    self.install_files("bin", "usr/lib/go-bootstrap")
    self.install_files("src", "usr/lib/go-bootstrap")
    self.install_files("pkg", "usr/lib/go-bootstrap")
