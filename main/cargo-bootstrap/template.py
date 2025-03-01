pkgname = "cargo-bootstrap"
pkgver = "1.85.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["sqlite", "zlib-ng-compat"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://repo.chimera-linux.org/distfiles/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = (
            "6b5d29babfcef4f8bc8300dacadc57b4d4d887d3fde98c876ada87f0f166887b"
        )
    case "ppc64le":
        sha256 = (
            "a37e89832f7aa73b268b3cb63f6c9b88966fc15e6a4ed1a3f52669f3ca432c54"
        )
    case "ppc64":
        sha256 = (
            "aa0505b135ea570510c56e449f44beb18f35529489be565702267652480c0089"
        )
    case "ppc":
        sha256 = (
            "b0a3c6888446f752efd801e6c8d3b6b9211c979551d404d6d833b60d7090f912"
        )
    case "riscv64":
        sha256 = (
            "dcbebeac22f3bc0f9c081972c30ad352edaa0f2138be5229b615d7eaacff1099"
        )
    case "x86_64":
        sha256 = (
            "be762f4c3d3c780793b4b74e7a6af3671e1d5198196a4fa26b253d5d85f8dd23"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
