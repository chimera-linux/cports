pkgname = "mise"
pkgver = "2025.1.9"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
make_build_args = [
    "--no-default-features",
    "--features=native-tls,rustls-native-roots",
]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=toolset::tool_version_list::tests::test_tool_version_list",
]
hostmakedepends = [
    "cargo",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "lua5.1-devel",
    "openssl3-devel",
    "rust-std",
    "zstd-devel",
]
checkdepends = ["bash"]
pkgdesc = "Development environment setup tool"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://mise.jdx.dev"
source = f"https://github.com/jdx/mise/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e44369529d2a786361dd1fa136fea130216768f709cb623447e68f1b19637e13"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/mise")
    self.install_license("LICENSE")
    self.install_man("man/man1/mise.1")
