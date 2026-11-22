pkgname = "jaq"
pkgver = "3.2.0"
pkgrel = 0
build_style = "cargo"
# disable the default mimalloc feature and just use the system allocator
make_build_args = ["--no-default-features", "--bin", "jaq"]
make_install_args = [*make_build_args]
make_check_args = ["--no-default-features"]
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
    "5478dd880f98abe4fdf13e7c38289aaa98b25e063ba40e8b9e69b22e2dc64ce7",
    "71eb017c8de6db05d859c4ac3cb4a3c20396f839e7b128047fcfe3c56f00e2ba",
]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "jaq"))
    self.install_man(self.sources_path / "jaq.1")
    self.install_license("LICENSE-MIT")
