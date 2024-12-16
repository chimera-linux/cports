pkgname = "perl-image-exiftool"
pkgver = "13.08"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for editing exif metadata"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://exiftool.org"
source = f"{url}/Image-ExifTool-{pkgver}.tar.gz"
sha256 = "72b3734ea308d09cfec7e9a1442dd0fc6af4d8879f06a1c845021b43cb5b4ef4"


@subpackage("exiftool")
def _(self):
    self.depends += [self.parent]
    return ["usr/bin"]
