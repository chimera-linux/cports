pkgname = "libpipeline"
pkgver = "1.5.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["check-devel"]
pkgdesc = "Pipeline manipulation library"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://libpipeline.gitlab.io/libpipeline"
source = f"https://download.savannah.nongnu.org/releases/libpipeline/libpipeline-{pkgver}.tar.gz"
sha256 = "1b1203ca152ccd63983c3f2112f7fe6fa5afd453218ede5153d1b31e11bb8405"


@subpackage("libpipeline-devel")
def _(self):
    return self.default_devel()
