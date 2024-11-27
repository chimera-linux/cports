pkgname = "pngquant"
pkgver = "3.0.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "lcms2-devel",
    "libpng-devel",
    "rust-std",
]
pkgdesc = "Lossy PNG compressor"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/kornelski/pngquant"
_libimagequant = "6e9805761851f1a8320380b9f563961f892ec6ba"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/ImageOptim/libimagequant/archive/{_libimagequant}.tar.gz",
]
source_paths = [".", "lib"]
sha256 = [
    "ddd8889a9c269ba454d0c5e4f7167948d55d77c4570b23f671809fd3a68b6822",
    "d0167e69f9303029bd1df3ea728fe9e7a9c4b64050c266140b119443bd2da4b7",
]


def post_install(self):
    self.install_man("pngquant.1")
