pkgname = "perl-image-exiftool"
pkgver = "12.99"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for editing exif metadata"
maintainer = "psykose <alice@ayaya.dev>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://exiftool.org"
source = f"https://exiftool.org/Image-ExifTool-{pkgver}.tar.gz"
sha256 = "267d86c13c28bb3546d30b4ba93c0b249f72e57e51bcc56062e1926d367f6e3e"


@subpackage("exiftool")
def _(self):
    self.depends += [self.parent]
    return ["usr/bin"]
