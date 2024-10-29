pkgname = "c2rust"
pkgver = "0.19.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--package", "c2rust"]
hostmakedepends = [
    "cargo-auditable",
    "clang-tools-extra",
    "cmake",
    "pkgconf",
]
makedepends = [
    "clang-devel",
    "clang-devel-static",
    "llvm-devel",
    "rust-std",
    "tinycbor-devel",
]
checkdepends = [
    "python",
    "python-plumbum",
    "python-psutil",
    "python-tomli",
]
pkgdesc = "C to Rust migration tool"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://c2rust.com"
source = (
    f"https://github.com/immunant/c2rust/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "912c28e5e289d1a9ef1e0f6c89db97eba19eda58625ca8bdc5b513fdb3c19ba4"
# check: requires nightly
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/c2rust")
    self.install_bin(
        f"target/{self.profile().triplet}/release/c2rust-transpile"
    )
    self.install_license("LICENSE")
