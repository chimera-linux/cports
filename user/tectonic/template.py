pkgname = "tectonic"
pkgver = "0.16.9"
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
sha256 = "9861d4d4230b987d8560f1b84fe6c8a550738401be65b9425b0c7d0466178f2b"

if self.profile().arch in ["loongarch64"]:
    broken = "outdated nix crate, can't update"

if self.profile().wordsize == 32:
    broken = "atomic64"


def post_install(self):
    self.install_license("LICENSE")
