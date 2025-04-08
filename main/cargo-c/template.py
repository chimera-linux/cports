pkgname = "cargo-c"
pkgver = "0.10.12"
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
    "ae118882067e1e7dcd8106933329cf018ddc6ea56cabfea7642a7699d6ce700f",
    "bacd7d7a73c6b14e78b3898dab29bf765b9c6534950ef8c9b35cde00d7181624",
]
# mfs be like rebuild literally everything and then run
# test_semver_one_zero_zero and test_semver_zero_zero_zero
options = ["!check"]


def post_extract(self):
    self.cp(self.sources_path / f"Cargo.lock.{pkgver}", "Cargo.lock")


def post_install(self):
    self.install_license("LICENSE")
