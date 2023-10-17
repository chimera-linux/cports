pkgname = "pngquant"
pkgver = "3.0.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "rust-std",
    "lcms2-devel",
    "libpng-devel",
]
pkgdesc = "Lossy PNG compressor"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/kornelski/pngquant"
_libimagequant = "9f15d1c53938a441a6bbfb2de866492797f69e22"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/ImageOptim/libimagequant/archive/{_libimagequant}.tar.gz",
]
source_paths = [".", "lib"]
sha256 = [
    "488e4587c27c7515427b231530cc070a6b123727137b32c501658cff3f8a3451",
    "06738e69b3d807ac99b2e40e00fce74293a60c6c2ac8c4fb3362cdcfc2bd0fb2",
]


def post_install(self):
    self.install_man("pngquant.1")
