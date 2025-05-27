pkgname = "rav1e"
pkgver = "0.8.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    # skip git_version
    "--features=binaries,asm,threading,signal_support",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "cargo-c",
    "nasm",
    "pkgconf",
]
makedepends = ["rust-std"]
pkgdesc = "AV1 encoder"
license = "BSD-2-Clause"
url = "https://github.com/xiph/rav1e"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2580bb4b4efae50e0a228e8ba80db1f73805a0e6f6a8c22bee066c90afb35ba0"


def post_build(self):
    self.cargo.cbuild()


def install(self):
    self.cargo.cinstall()
    self.install_bin(f"target/{self.profile().triplet}/release/rav1e")
    self.install_license("LICENSE")


@subpackage("rav1e-libs")
def _(self):
    return self.default_libs()


@subpackage("rav1e-devel")
def _(self):
    return self.default_devel()
