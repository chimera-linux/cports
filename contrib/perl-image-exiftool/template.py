pkgname = "perl-image-exiftool"
pkgver = "12.96"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for editing exif metadata"
maintainer = "psykose <alice@ayaya.dev>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://exiftool.org"
source = f"https://exiftool.org/Image-ExifTool-{pkgver}.tar.gz"
sha256 = "405a23f31be0d2fb248dc30d96c4ec7f63f9b1af8c92e753fe6c654a595813db"


@subpackage("exiftool")
def _(self):
    self.depends += [self.parent]
    return ["usr/bin"]
