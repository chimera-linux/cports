pkgname = "cowsql"
pkgver = "1.15.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = ["libuv-devel", "raft-devel", "sqlite-devel"]
pkgdesc = "Embeddable, replicated and fault tolerant SQL engine"
maintainer = "tj <tjheeta@gmail.com>"
license = "LGPL-3.0-only"
url = "https://github.com/cowsql/cowsql"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "723f7f8ede3bcb19c10a6c85c18a23ee34c6874cb4cf104c434bd69d6a916882"


@subpackage("cowsql-devel")
def _(self):
    return self.default_devel()
