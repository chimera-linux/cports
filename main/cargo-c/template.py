pkgname = "cargo-c"
pkgver = "0.10.3"
pkgrel = 1
build_style = "cargo"
prepare_after_patch = True
# no tests in others
make_check_args = ["--lib"]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libcurl-devel",
    "libgit2-devel",
    "openssl-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Cargo plugin to install C-ABI libraries"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/lu-zero/cargo-c"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/Cargo.lock>Cargo.lock.{pkgver}",
]
sha256 = [
    "922171afb3ceaf6553ff3916ae4663d3743ba22f80725f2300a26b76eb6eb94f",
    "6c099fe28666e4c6b5da41b65d00de35c9c60ab336c625d845f28055a0e90a7d",
]
# mfs be like rebuild literally everything and then run
# test_semver_one_zero_zero and test_semver_zero_zero_zero
options = ["!check"]


def post_extract(self):
    self.cp(self.sources_path / f"Cargo.lock.{pkgver}", "Cargo.lock")


def post_install(self):
    self.install_license("LICENSE")
