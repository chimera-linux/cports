pkgname = "cargo-c"
pkgver = "0.10.5"
pkgrel = 0
build_style = "cargo"
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
    "3f131a6a647851a617a87daaaf777a9e50817957be0af29806615613e98efc8a",
    "2b5660aabd70f6a12390a19bcdeacc585c418d24aaa6855bd396a1c3a5684320",
]
# mfs be like rebuild literally everything and then run
# test_semver_one_zero_zero and test_semver_zero_zero_zero
options = ["!check"]


def post_extract(self):
    self.cp(self.sources_path / f"Cargo.lock.{pkgver}", "Cargo.lock")


def post_install(self):
    self.install_license("LICENSE")
