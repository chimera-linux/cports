pkgname = "sqlite"
pkgver = "3.46.1"
_amalg = "3460100"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-dynamic-extensions",
    "--enable-fts3",
    "--enable-fts4",
    "--enable-fts5",
    "--enable-threadsafe",
]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libedit-devel", "zlib-ng-compat-devel"]
pkgdesc = "SQL Database Engine in a C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "blessing"
url = "https://sqlite.org"
source = f"https://sqlite.org/2024/sqlite-autoconf-{_amalg}.tar.gz"
sha256 = "67d3fe6d268e6eaddcae3727fce58fcc8e9c53869bdd07a0c61e38ddf2965071"
options = ["!parallel"]

_cflags = [
    "-DHAVE_FDATASYNC",
    "-DSQLITE_ENABLE_BATCH_ATOMIC_WRITE=1",
    "-DSQLITE_ENABLE_COLUMN_METADATA",
    "-DSQLITE_ENABLE_DBSTAT_VTAB",
    "-DSQLITE_ENABLE_DESERIALIZE",
    "-DSQLITE_ENABLE_FTS3_PARENTHESIS",
    "-DSQLITE_ENABLE_FTS3_TOKENIZER=1",
    "-DSQLITE_ENABLE_STAT4=1",
    "-DSQLITE_ENABLE_UNLOCK_NOTIFY",
    "-DSQLITE_MAX_EXPR_DEPTH=5000",
    "-DSQLITE_MAX_VARIABLE_NUMBER=250000",
    "-DSQLITE_SECURE_DELETE",
]

if self.profile().endian == "big":
    _cflags += ["-DSHA3_BYTEORDER=4321", "-DSQLITE_BYTEORDER=4321"]
else:
    _cflags += ["-DSHA3_BYTEORDER=1234", "-DSQLITE_BYTEORDER=1234"]

tool_flags = {"CFLAGS": _cflags}


@subpackage("sqlite-devel")
def _(self):
    return self.default_devel()
