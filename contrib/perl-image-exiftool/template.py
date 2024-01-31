pkgname = "perl-image-exiftool"
pkgver = "12.76"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = [
    "gmake",
    "perl",
]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for editing exif metadata"
maintainer = "psykose <alice@ayaya.dev>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://exiftool.org"
source = f"https://exiftool.org/Image-ExifTool-{pkgver}.tar.gz"
sha256 = "5d3430ec57aa031f7ca43170f7ed6338a66bda99ab95b9e071f1ee27555f515f"


@subpackage("exiftool")
def _exiftool(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return ["usr/bin"]
