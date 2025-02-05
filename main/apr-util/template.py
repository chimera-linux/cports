pkgname = "apr-util"
pkgver = "1.6.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-apr=/usr",
    "--with-crypto",
    "--with-openssl",
    "--without-ldap",
    "--without-gdbm",
    "--without-berkeley-db",
]
configure_gen = []  # stupid broken autotools
hostmakedepends = ["apr-devel", "libtool", "pkgconf"]
makedepends = [
    "apr-devel",
    "libexpat-devel",
    "openssl3-devel",
    "sqlite-devel",
    "unixodbc-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Apache Portable Runtime utility library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://apr.apache.org"
source = f"https://archive.apache.org/dist/apr/apr-util-{pkgver}.tar.gz"
sha256 = "2b74d8932703826862ca305b094eef2983c27b39d5c9414442e9976a9acf1983"
# not even once
options = ["!cross"]


def post_install(self):
    # static module junk
    for slib in self.find(self.destdir, "*.a"):
        self.rm(slib)


def _gen_subp(name, desc, iif):
    @subpackage(f"apr-util-{name}")
    def _(self):
        self.subdesc = f"{desc} module"
        self.depends = [self.parent]
        self.install_if = [self.parent, iif]

        return [f"usr/lib/apr-util-1/*{name}*"]


for _pname, _pdesc, _piif in [
    ("odbc", "ODBC", "unixodbc-libs"),
    ("sqlite", "SQLite", "sqlite"),
]:
    _gen_subp(_pname, _pdesc, _piif)


@subpackage("apr-util-devel")
def _(self):
    self.depends += ["libexpat-devel"]

    return self.default_devel()
