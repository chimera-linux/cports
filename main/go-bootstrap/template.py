pkgname = "go-bootstrap"
pkgver = "1.24.0"
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
            "a694eb1a1e1c45f435f673040bfe5f5f0b6f028eb796fb9c50de7f72217fc50f"
        )
    case "loong64":
        sha256 = (
            "dc709c3762393fdb6ca28c23449b51568c59947bbebd1f3cd43633a76d361d02"
        )
    case "ppc64le":
        sha256 = (
            "158f4045f8a6ae0926d488e71582cfad962a1683d9ef6b2789e15ad5020f17a0"
        )
    case "riscv64":
        sha256 = (
            "263f04498e2e2479488728b3c1da7609b06cd18d8033f925538fd43b617fb318"
        )
    case "amd64":
        sha256 = (
            "8f6ba7f20231f7c60ef1100fccda81ed49102f8fe9d32eef091df2d14d540604"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"

source = f"https://repo.chimera-linux.org/distfiles/go-bootstrap-{pkgver}-{self.profile().goarch or ''}.tar.zst"


def install(self):
    self.install_license("LICENSE")
    self.install_files("bin", "usr/lib/go-bootstrap")
    self.install_files("src", "usr/lib/go-bootstrap")
    self.install_files("pkg", "usr/lib/go-bootstrap")
