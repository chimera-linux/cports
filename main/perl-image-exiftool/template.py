pkgname = "perl-image-exiftool"
pkgver = "13.11"
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
sha256 = "b8bb379b8f8d7534792de229f25557a83300d46a2d7c3448f29eb3358998366d"


@subpackage("exiftool")
def _(self):
    self.depends += [self.parent]
    return ["usr/bin"]
