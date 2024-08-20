pkgname = "libmusicbrainz"
pkgver = "5.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["neon-devel", "libxml2-devel"]
pkgdesc = "MusicBrainz client library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-or-later"
url = "https://musicbrainz.org/doc/libmusicbrainz"
source = f"https://github.com/metabrainz/libmusicbrainz/releases/download/release-{pkgver}/libmusicbrainz-{pkgver}.tar.gz"
sha256 = "6749259e89bbb273f3f5ad7acdffb7c47a2cf8fcaeab4c4695484cef5f4c6b46"


@subpackage("libmusicbrainz-devel")
def _(self):
    return self.default_devel()
