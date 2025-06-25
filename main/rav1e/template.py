pkgname = "rav1e"
pkgver = "0.8.1"
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
sha256 = "06d1523955fb6ed9cf9992eace772121067cca7e8926988a1ee16492febbe01e"


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
