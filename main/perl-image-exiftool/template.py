pkgname = "perl-image-exiftool"
pkgver = "13.02"
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
sha256 = "b98ce4f610b7ca8b4989b94f12e1f4f40d4aa2b364d9c2915e97f41dc0f5d008"


@subpackage("exiftool")
def _(self):
    self.depends += [self.parent]
    return ["usr/bin"]
