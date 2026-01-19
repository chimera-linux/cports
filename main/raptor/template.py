pkgname = "raptor"
pkgver = "2.0.16"
pkgrel = 9
build_style = "gnu_configure"
configure_args = ["--with-yajl=no"]
# fails tests when regen
configure_gen = []
make_check_args = ["-j1"]  # racey tests
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "curl-devel",
    "icu-devel",
    "libxml2-devel",
    "libxslt-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Raptor RDF syntax library"
license = "Apache-2.0 OR LGPL-2.1-or-later OR GPL-2.0-or-later"
url = "https://librdf.org/raptor"
source = f"https://librdf.org/dist/source/raptor2-{pkgver}.tar.gz"
sha256 = "089db78d7ac982354bdbf39d973baf09581e6904ac4c92a98c5caadb3de44680"


@subpackage("raptor-devel")
def _(self):
    # Requires are not listed
    self.depends += makedepends

    return self.default_devel()


@subpackage("raptor-progs")
def _(self):
    return self.default_progs()
