pkgname = "cargo-bootstrap"
pkgver = "1.93.0"
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
            "dfe5f1a6614d5cae16d734bb5c0f9b6a6e63ed4706d6bdce43af89bd5ea4e239"
        )
    case "loongarch64":
        sha256 = (
            "0d6ec829cf87d29f877456e79dd0ce42f4aac7e38a1e53483e8649d23042de0e"
        )
    case "ppc64le":
        sha256 = (
            "0e79922aabf3a297cd168f252e761c2c46238284af03e60ca117dc6577051088"
        )
    case "ppc64":
        sha256 = (
            "a9db197b0ea1cff87f8e361347afba32302120e5f9ba097aba60aad9d071a07b"
        )
    case "ppc":
        sha256 = (
            "56ee33ba338f98ceee870273001c871d9f94f7f69bc9bb67c39478ecd66d1998"
        )
    case "riscv64":
        sha256 = (
            "796a3773383c70730622ae770440954b102b50b2ff0447f9e0c89062bae179ec"
        )
    case "x86_64":
        sha256 = (
            "a6f3f8e72b4de968e4b726bdbdb12f4d902e549befab5e6cbe7f517107fda79f"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
