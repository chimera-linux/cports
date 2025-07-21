pkgname = "tectonic"
pkgver = "0.15.0"
pkgrel = 4
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "geturl-curl,serialization,external-harfbuzz",
]
make_install_args = make_build_args
make_check_args = ["--features", "external-harfbuzz"]
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
sha256 = "3c13de312c4fe39ff905ad17e64a15a3a59d33ab65dacb0a8b9482c57e6bc6aa"

if self.profile().arch in ["loongarch64"]:
    broken = "outdated nix crate, can't update"


def pre_prepare(self):
    # rust 1.80 type inference regression
    self.do(
        "cargo",
        "update",
        "--package",
        "time",
        "--precise",
        "0.3.36",
        allow_network=True,
    )


def post_install(self):
    self.install_license("LICENSE")
