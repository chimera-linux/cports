pkgname = "cargo-bootstrap"
pkgver = "1.72.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["zlib"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://repo.chimera-linux.org/distfiles/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = (
            "71e072bad3e93023a10281c033e21e8dd402364430fa0def48d117375a3aca48"
        )
    case "ppc64le":
        sha256 = (
            "33f15931db1e2360111480742d60626f4f032244322979944405aac71f1f4ee2"
        )
    case "ppc64":
        sha256 = (
            "bc1b62bf6ec29a6c6128c34ee2d894941d1319e73745b876d627a8071b40401b"
        )
    case "riscv64":
        sha256 = (
            "33f4da308ae93a2b93404be5681bdacc83906f4c12027deb503814ad43e97c57"
        )
    case "x86_64":
        sha256 = (
            "f46457558f5f0de2de2583a684ba2508f0accbb6718502bb670362d4326d30ec"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
