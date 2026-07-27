pkgname = "tectonic"
pkgver = "0.17.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "geturl-curl,serialization,external-harfbuzz",
]
make_install_args = make_build_args
make_check_args = [
    "--features",
    "external-harfbuzz",
    "--",
    "--skip",
    # internet access
    "no_segfault_after_failed_compilation",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "curl-devel",
    "freetype-devel",
    "graphite2-devel",
    "harfbuzz-devel",
    "icu-devel",
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "Modernized LaTeX engine"
license = "MIT"
url = "https://tectonic-typesetting.github.io/en-US"
source = f"https://github.com/tectonic-typesetting/tectonic/archive/refs/tags/tectonic@{pkgver}.tar.gz"
sha256 = "30adda98f67dd5389844f6023adeeb54b5475c17a54b777900644468fbc9765d"

if self.profile().arch in ["loongarch64"]:
    broken = "outdated nix crate, can't update"

if self.profile().wordsize == 32:
    broken = "atomic64"


def post_install(self):
    self.install_license("LICENSE")
