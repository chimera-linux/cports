pkgname = "soxr"
pkgver = "0.1.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "High quality, one-dimensional sample-rate conversion library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://sourceforge.net/projects/soxr"
source = f"$(SOURCEFORGE_SITE)/soxr/soxr-{pkgver}-Source.tar.xz"
sha256 = "b111c15fdc8c029989330ff559184198c161100a59312f5dc19ddeb9b5a15889"
# FIXME: cfi, int test failures
hardening = ["vis", "!int"]


@subpackage("soxr-devel")
def _(self):
    return self.default_devel()
