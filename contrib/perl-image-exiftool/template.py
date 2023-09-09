pkgname = "perl-image-exiftool"
pkgver = "12.60"
pkgrel = 1
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
sha256 = "73dbe06d004c31082a56e78d7f246f2bb0002fbb1835447bc32a2b076f3d32ad"


@subpackage("exiftool")
def _exiftool(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return ["usr/bin"]
