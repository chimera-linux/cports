pkgname = "perl-image-exiftool"
pkgver = "13.55"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for editing exif metadata"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://exiftool.org"
source = f"$(CPAN_SITE)/Image/EXIFTOOL/Image-ExifTool-{pkgver}.tar.gz"
sha256 = "5f4c81d34ad406538c2871ad72dbfceb5d9b412b2f16cbbeb4d712d270846667"


@subpackage("perl-image-exiftool-progs")
def _(self):
    self.depends += [self.parent]
    self.renames = ["exiftool"]

    return self.default_progs()
