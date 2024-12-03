pkgname = "perl-image-exiftool"
pkgver = "13.04"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for editing exif metadata"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://exiftool.org"
source = f"https://exiftool.org/Image-ExifTool-{pkgver}.tar.gz"
sha256 = "bd14e06a3f2cf167999675e78cbaff396929ec442be0ab86c5cd0599223e6c3a"


@subpackage("exiftool")
def _(self):
    self.depends += [self.parent]
    return ["usr/bin"]
