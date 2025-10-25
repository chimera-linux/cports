pkgname = "cowsql"
pkgver = "1.15.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = ["libuv-devel", "raft-devel", "sqlite-devel"]
pkgdesc = "Embeddable, replicated and fault tolerant SQL engine"
license = "LGPL-3.0-only"
url = "https://github.com/cowsql/cowsql"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "257aee775f68fd145bfae012dc394fdf62c2f97f0360b0bcf6bd1f66bc58ca04"


@subpackage("cowsql-devel")
def _(self):
    return self.default_devel()
