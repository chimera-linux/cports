pkgname = "redland"
pkgver = "1.0.17"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-release",
    "--with-raptor=system",
    "--with-rasqal=system",
    "--with-sqlite=3",
]
hostmakedepends = ["pkgconf", "automake", "libtool", "perl", "gtk-doc-tools"]
makedepends = [
    "libltdl-devel",
    "rasqal-devel",
    "sqlite-devel",
    "unixodbc-devel",
]
pkgdesc = "Redlang Resource Description Framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later OR LGPL-2.1-or-later OR Apache-2.0"
url = "https://librdf.org"
source = f"{url}/dist/source/redland-{pkgver}.tar.gz"
sha256 = "de1847f7b59021c16bdc72abb4d8e2d9187cd6124d69156f3326dd34ee043681"


@subpackage("redland-storage-virtuoso")
def _virtuoso(self):
    self.subdesc = "virtuoso storage backend"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "unixodbc-libs"]

    return ["usr/lib/redland/librdf_storage_virtuoso.so"]


@subpackage("redland-storage-sqlite")
def _sqlite(self):
    self.subdesc = "SQLite storage backend"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "sqlite"]

    return ["usr/lib/redland/librdf_storage_sqlite.so"]


@subpackage("redland-devel")
def _devel(self):
    return self.default_devel()
