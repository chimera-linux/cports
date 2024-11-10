pkgname = "tree-sitter-cli"
# match to tree-sitter
pkgver = "0.24.4"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "tree-sitter-cli"]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "cmake"]
makedepends = ["rust-std"]
pkgdesc = "Parser generator tool for tree-sitter bindings"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://tree-sitter.github.io/tree-sitter"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "d704832a6bfaac8b3cbca3b5d773cad613183ba8c04166638af2c6e5dfb9e2d2"
# requires fetching fixtures
options = ["!check"]

if self.profile().arch in ["aarch64", "x86_64"]:
    make_build_args += ["--features", "wasm"]
    make_check_args += ["--features", "wasm"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/tree-sitter")
    self.install_license("LICENSE")
