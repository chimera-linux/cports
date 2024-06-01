pkgname = "cargo-bootstrap"
pkgver = "1.78.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["sqlite", "zlib"]
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
            "b2271f65f5775186b879d613a68651b35aa89aad5c6fb6ecb15e7a4b18f11811"
        )
    case "ppc64le":
        sha256 = (
            "dc0cf612ea33cfbfb89b54b74790da296f57d678d5b399798ca636709be2123a"
        )
    case "ppc64":
        sha256 = (
            "5c3d4cc85dd6964f8401b46a538f83a7d9f53d8b921acbc45d1a236e2123e119"
        )
    case "riscv64":
        sha256 = (
            "65d71fe79f4aa480101972548aa4856e119359fe3954119573691b1423227e0a"
        )
    case "x86_64":
        sha256 = (
            "4d4b93dc002d21ee415eb50a48d2e2685489b41ea962bf77145cc8ee4457d842"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
