pkgname = "xapian-core"
pkgver = "1.4.29"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "zlib-ng-compat-devel",
]
pkgdesc = "Open source search engine library"
license = "GPL-2.0-or-later"
url = "https://xapian.org"
source = f"https://oligarchy.co.uk/xapian/{pkgver}/xapian-core-{pkgver}.tar.xz"
sha256 = "c55c9bc8613ad3ec2c218eafca088c218ab7cddcba7ef08f3af0e542f4e521bc"
hardening = ["vis", "cfi"]
# see below
options = []

if self.profile().arch == "ppc":
    # FIXME: hangs (or takes eons? idk) due to a load of "NetworkTimeoutError"
    options += ["!check"]

if self.profile().arch == "ppc64":
    # FIXME: hangs after replacedoc9
    options += ["!check"]


@subpackage("xapian-core-devel")
def _(self):
    return self.default_devel()


@subpackage("xapian-core-libs")
def _(self):
    return self.default_libs()
