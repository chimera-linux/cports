pkgname = "cargo-c"
pkgver = "0.10.14"
pkgrel = 0
build_style = "cargo"
# no tests in others
make_check_args = ["--lib"]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "libgit2-devel",
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Cargo plugin to install C-ABI libraries"
license = "MIT"
url = "https://github.com/lu-zero/cargo-c"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/Cargo.lock>Cargo.lock.{pkgver}",
]
source_paths = [".", "."]
sha256 = [
    "eb6d09e871516083448f77b8677dbefc1dcc14e88d73eea82bcee903343e19c1",
    "0af99496210d7e5cb70de6643b571a8882120148e628d7a75327937b64fd9841",
]
# mfs be like rebuild literally everything and then run
# test_semver_one_zero_zero and test_semver_zero_zero_zero
options = ["!check"]


def post_extract(self):
    self.cp(self.sources_path / f"Cargo.lock.{pkgver}", "Cargo.lock")


def post_install(self):
    self.install_license("LICENSE")
