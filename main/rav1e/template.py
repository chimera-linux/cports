pkgname = "rav1e"
pkgver = "0.7.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    # skip git_version
    "--features=binaries,asm,threading,signal_support",
]
make_install_args = list(make_build_args)
make_check_args = list(make_build_args)
hostmakedepends = [
    "cargo-auditable",
    "cargo-c",
    "nasm",
    "pkgconf",
]
makedepends = ["rust-std"]
pkgdesc = "AV1 Encoder"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://github.com/xiph/rav1e"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/Cargo.lock",
]
sha256 = [
    "da7ae0df2b608e539de5d443c096e109442cdfa6c5e9b4014361211cf61d030c",
    "4482976bfb7647d707f9a01fa1a3848366988f439924b5c8ac7ab085fba24240",
]


def init_configure(self):
    from cbuild.util import cargo

    self.cargo_c = cargo.Cargo(self, cargo_c=True)


def post_build(self):
    self.cargo_c.build()


def do_install(self):
    self.cargo_c.install()
    self.install_bin(f"target/{self.profile().triplet}/release/rav1e")
    self.install_license("LICENSE")


@subpackage("rav1e-libs")
def _libs(self):
    return self.default_libs()


@subpackage("rav1e-devel")
def _devel(self):
    return self.default_devel()
