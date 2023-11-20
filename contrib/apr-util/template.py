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
make_cmd = "gmake"
hostmakedepends = ["apr-devel", "gmake", "libtool", "pkgconf"]
makedepends = [
    "apr-devel",
    "libexpat-devel",
    "openssl-devel",
    "sqlite-devel",
    "unixodbc-devel",
    "zlib-devel",
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
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({desc} module)"
        self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
        self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", iif]

        return [f"usr/lib/apr-util-1/*{name}*"]


for _pname, _pdesc, _piif in [
    ("odbc", "ODBC", "unixodbc-libs"),
    ("sqlite", "SQLite", "sqlite"),
]:
    _gen_subp(_pname, _pdesc, _piif)


@subpackage("apr-util-devel")
def _devel(self):
    self.depends += ["libexpat-devel"]

    return self.default_devel()
