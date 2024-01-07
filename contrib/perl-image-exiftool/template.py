pkgname = "perl-image-exiftool"
pkgver = "12.70"
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
sha256 = "4cb2522445cc3e3f3bd13904c6aeaeada5fc5a5e2498d7abad2957dcb42caffe"


@subpackage("exiftool")
def _exiftool(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return ["usr/bin"]
