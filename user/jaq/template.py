pkgname = "jaq"
pkgver = "3.1.2"
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
    "54ac66fac30a1d28c54f19716215cf4256877c69964c1c0150c3976bde618b93",
    "897aa15830beae6a357b4ff6f576dc5c76aa6ca79ad05cc16b47c809c58a9572",
]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "jaq"))
    self.install_man(self.sources_path / "jaq.1")
    self.install_license("LICENSE-MIT")
