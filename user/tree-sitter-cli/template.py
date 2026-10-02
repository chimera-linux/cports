pkgname = "tree-sitter-cli"
# match to tree-sitter
pkgver = "0.27.0"
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
sha256 = "d35c96e68736bd9569d2757c3cc71052485f33082c3825f1aed9d0e86013a159"
# requires fetching fixtures
options = ["!check"]

if self.profile.arch in ["aarch64", "x86_64"]:
    make_build_args += ["--features", "wasm"]
    make_check_args += ["--features", "wasm"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "tree-sitter"))
    self.install_license("LICENSE")
