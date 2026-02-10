pkgname = "go-bootstrap"
pkgver = "1.25.4"
pkgrel = 0
# just in case
depends = ["!go"]
pkgdesc = "Go programming language bootstrap toolchain"
license = "BSD-3-Clause"
url = "https://go.dev"
options = ["!strip", "!scanrundeps", "!lintstatic", "foreignelf", "execstack"]

match self.profile().goarch:
    case "arm64":
        sha256 = (
            "97cc9292ef0e2cfe44d46cb9d7b4fca92d3e636ebe21141745fea3d334a4acbd"
        )
    case "loong64":
        sha256 = (
            "dd39af03da38b40d01b640dd85c96932b119747fe8d5f5896c9b423ee7c56f4d"
        )
    case "ppc64le":
        sha256 = (
            "a47c93c24670600b8e23ac1070f22f85d8178b6faf253d90cab6a1b213ba10d6"
        )
    case "riscv64":
        sha256 = (
            "821c690b1cc237ea5960560d846c740f0549b39d6d9ad7d7660fd6801f831ecc"
        )
    case "amd64":
        sha256 = (
            "b6ceb7a6f33b5e209beeaa8ddd63e6cacae5d6cf2ccd21e080019c6edff953a2"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"

source = f"https://repo.chimera-linux.org/distfiles/go-bootstrap-{pkgver}-{self.profile().goarch or ''}.tar.zst"


def install(self):
    self.install_license("LICENSE")
    self.install_files("bin", "usr/lib/go-bootstrap")
    self.install_files("src", "usr/lib/go-bootstrap")
    self.install_files("pkg", "usr/lib/go-bootstrap")
