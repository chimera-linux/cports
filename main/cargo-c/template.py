pkgname = "cargo-c"
pkgver = "0.10.0"
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
pkgdesc = "Cargo plugin for install C-ABI libraries"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/lu-zero/cargo-c"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/Cargo.lock",
]
sha256 = [
    "85230801f57c1f2b85d99fae3fc43f93080ecc0e3763a6af178fc5e6c218004b",
    "ba3fee6cbeba8c4ea8d0ca56bc72bc616eb7f2a9e705017c8e612f16f472cc30",
]


def post_install(self):
    self.install_license("LICENSE")
