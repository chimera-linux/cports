pkgname = "perl-image-exiftool"
pkgver = "12.86"
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
sha256 = "7f6a8090f1831783d4b3045847d9c13a229393dd6366e0eab46c44a400b86914"


@subpackage("exiftool")
def _exiftool(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return ["usr/bin"]
