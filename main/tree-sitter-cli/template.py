pkgname = "tree-sitter-cli"
# match to tree-sitter
pkgver = "0.25.8"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "tree-sitter-cli"]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "cmake"]
makedepends = ["rust-std"]
pkgdesc = "Parser generator tool for tree-sitter bindings"
license = "MIT"
url = "https://tree-sitter.github.io/tree-sitter"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "178b575244d967f4920a4642408dc4edf6de96948d37d7f06e5b78acee9c0b4e"
# requires fetching fixtures
options = ["!check"]

if self.profile().arch in ["aarch64", "x86_64"]:
    make_build_args += ["--features", "wasm"]
    make_check_args += ["--features", "wasm"]


def post_prepare(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "cc")


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/tree-sitter")
    self.install_license("LICENSE")
