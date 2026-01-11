pkgname = "perl-image-exiftool"
pkgver = "13.30"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for editing exif metadata"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://exiftool.org"
source = f"{url}/Image-ExifTool-{pkgver}.tar.gz"
sha256 = "885afd06c4efcc60d1df703cc88ba7ddc3bb6fed854cfbaa9e6cd72adfbe8da9"


@subpackage("perl-image-exiftool-progs")
def _(self):
    self.depends += [self.parent]
    self.renames = ["exiftool"]

    return self.default_progs()
