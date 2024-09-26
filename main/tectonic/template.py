pkgname = "tectonic"
pkgver = "0.15.0"
pkgrel = 1
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
    "freetype-devel",
    "graphite2-devel",
    "harfbuzz-devel",
    "icu-devel",
    "libcurl-devel",
    "openssl-devel",
    "rust-std",
]
pkgdesc = "Modernized LaTeX engine"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://tectonic-typesetting.github.io/en-US"
source = f"https://github.com/tectonic-typesetting/tectonic/archive/refs/tags/tectonic@{pkgver}.tar.gz"
sha256 = "3c13de312c4fe39ff905ad17e64a15a3a59d33ab65dacb0a8b9482c57e6bc6aa"


def post_install(self):
    self.install_license("LICENSE")
