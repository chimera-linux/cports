pkgname = "perl-image-exiftool"
pkgver = "12.95"
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
sha256 = "ce88e0bf47c3097a814fa847e5576dd3f9d4c91b380b5bcf4cb1e55d1c289a91"


@subpackage("exiftool")
def _(self):
    self.depends += [self.parent]
    return ["usr/bin"]
