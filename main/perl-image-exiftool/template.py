pkgname = "perl-image-exiftool"
pkgver = "13.27"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for editing exif metadata"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://exiftool.org"
source = f"{url}/Image-ExifTool-{pkgver}.tar.gz"
sha256 = "4b772e8766f8eb098ac8ab208fd80f7736bc65a23a1104511173709f48db43a4"


@subpackage("perl-image-exiftool-progs")
def _(self):
    self.depends += [self.parent]
    self.provides = [self.with_pkgver("exiftool")]

    return self.default_progs()
