pkgname = "tree-sitter-cli"
# match to tree-sitter
pkgver = "0.25.10"
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
sha256 = "ad5040537537012b16ef6e1210a572b927c7cdc2b99d1ee88d44a7dcdc3ff44c"
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
