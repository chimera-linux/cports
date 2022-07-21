pkgname = "imagemagick"
pkgver = "7.1.0.25"
_index = pkgver.rindex(".")
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-static"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = [
    "lcms2-devel", "libheif-devel", "libpng-devel", "libtiff-devel", "libwebp-devel",
    "openjpeg-devel", "zlib-devel"
]
pkgdesc = "Create, edit, compose, or convert digital images"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "ImageMagick"
url = "https://www.imagemagick.org"
source = f"https://download.imagemagick.org/ImageMagick/download/ImageMagick-{pkgver[:_index] + '-' + pkgver[_index+1:]}.tar.xz"
sha256 = "871e2b98a6ccc91b2a9f728f1cb4e9988b93269f07a4f5ea7f442c3beeda911a"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libmagic")
def _libs(self):
    return self.default_libs()

@subpackage("libmagic-devel")
def _devel(self):
    return self.default_devel()

