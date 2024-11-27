pkgname = "rav1e"
pkgver = "0.7.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/xiph/rav1e"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/Cargo.lock>Cargo.lock.{pkgver}",
]
sha256 = [
    "da7ae0df2b608e539de5d443c096e109442cdfa6c5e9b4014361211cf61d030c",
    "4482976bfb7647d707f9a01fa1a3848366988f439924b5c8ac7ab085fba24240",
]


def post_extract(self):
    self.cp(self.sources_path / f"Cargo.lock.{pkgver}", "Cargo.lock")


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
