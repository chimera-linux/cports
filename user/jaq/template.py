pkgname = "jaq"
pkgver = "3.0.0"
pkgrel = 0
build_style = "cargo"
# disable the default mimalloc feature and just use the system allocator
make_build_args = ["--no-default-features", "--bin", "jaq"]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "JSON data processing tool with jq compatible syntax"
license = "MIT"
url = "https://github.com/01mf02/jaq"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/jaq.1",
]
source_paths = [".", "manpage"]
sha256 = [
    "c56948c90d0c3566c8b33eedd9fa61587ffbb2feef7d78172955876d6e10a315",
    "01c39aa68e2086d3dfe88031984f25cd1eb6d3f146b371f55c7c4e9ba2dbfa77",
]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/jaq")
    self.install_man(self.sources_path / "jaq.1")
    self.install_license("LICENSE-MIT")
