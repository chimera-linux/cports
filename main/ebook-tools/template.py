pkgname = "ebook-tools"
pkgver = "0.2.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "libxml2-devel",
    "libzip-devel",
]
pkgdesc = "Tools for accessing and converting ebook formats"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://sourceforge.net/projects/ebook-tools"
source = f"$(SOURCEFORGE_SITE)/ebook-tools/ebook-tools-{pkgver}.tar.gz"
sha256 = "cbc35996e911144fa62925366ad6a6212d6af2588f1e39075954973bbee627ae"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("ebook-tools-devel")
def _(self):
    return self.default_devel()
