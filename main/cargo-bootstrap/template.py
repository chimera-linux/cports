pkgname = "cargo-bootstrap"
pkgver = "1.96.0"
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
            "a499c80fbfa6592683694316a64152a7f0074aafda1c785da5d8b91c744026b7"
        )
    case "loongarch64":
        sha256 = (
            "acc76d7ab5b61c4bf6d4e394aba6a6c12a054cc71a325564f49602ac8fe6a31a"
        )
    case "ppc64le":
        sha256 = (
            "156d38c0e32c750a45adc1350f62cd3333b57417e9f8dbee0f47d036ce77e9be"
        )
    case "riscv64":
        sha256 = (
            "9f90f4e4542c7a66813c3c5cee1ea6bb488f4a8726029233e23fa70ed8c06493"
        )
    case "x86_64":
        sha256 = (
            "d9e75d8cb78e7b73f1f2fdc63b8b6cc851707cc23b4cbbdb6e1bbba34a974549"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
