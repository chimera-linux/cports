pkgname = "perl-image-exiftool"
pkgver = "13.45"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for editing exif metadata"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://exiftool.org"
source = f"{url}/Image-ExifTool-{pkgver}.tar.gz"
sha256 = "c2328f14b86be36c624332f93d387fbe3fb37f1ff3c1d26e7e6eaf65e0a9047b"


@subpackage("perl-image-exiftool-progs")
def _(self):
    self.depends += [self.parent]
    self.renames = ["exiftool"]

    return self.default_progs()
