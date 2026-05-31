pkgname = "cargo-bootstrap"
pkgver = "1.95.0"
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
            "2285f916e284a1417962457383c209b25b8a6cc12c815ef79e1bb7d950932e8c"
        )
    case "loongarch64":
        sha256 = (
            "de715f05fc281e06d36af42a486d5d32609f87492bba772523366315d7a60914"
        )
    case "ppc64le":
        sha256 = (
            "4424bc34c41ad929ca9ae70f02f775e51c12d314c94d162d9cc28aca386ec7e7"
        )
    case "ppc64":
        sha256 = (
            "b377c33ba170ec778fa10a67a6ecad0ee0829396ef328644524ce779c9ff1e64"
        )
    case "ppc":
        sha256 = (
            "b0daee5d4d2d526171d4b7fcef14129c7a9b353f7d60e97f6c761c0f4f823ec3"
        )
    case "riscv64":
        sha256 = (
            "1b233c1fd8abae00a89c27609f62cfe4f3135a24fe916599b1ff197eb4463dfe"
        )
    case "x86_64":
        sha256 = (
            "111f442365a9842427b7111d5d4f23038031d2309ae640a970cd5ca26cc80fc8"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
