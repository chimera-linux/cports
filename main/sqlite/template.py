pkgname = "sqlite"
pkgver = "3.45.3"
_amalg = "3450300"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-threadsafe",
    "--enable-dynamic-extensions",
    "--enable-fts5",
]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libedit-devel", "zlib-devel"]
pkgdesc = "SQL Database Engine in a C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "blessing"
url = "https://sqlite.org"
source = f"https://sqlite.org/2024/sqlite-autoconf-{_amalg}.tar.gz"
sha256 = "b2809ca53124c19c60f42bf627736eae011afdcc205bb48270a5ee9a38191531"
options = ["!parallel"]

_cflags = [
    "-DSQLITE_ENABLE_DBSTAT_VTAB",
    "-DSQLITE_ENABLE_COLUMN_METADATA",
    "-DSQLITE_ENABLE_UNLOCK_NOTIFY",
    "-DSQLITE_SECURE_DELETE",
    "-DSQLITE_ENABLE_FTS3",
    "-DSQLITE_ENABLE_FTS3_PARENTHESIS",
    "-DSQLITE_ENABLE_FTS4",
    "-DSQLITE_ENABLE_FTS3_TOKENIZER=1",
    "-DSQLITE_ENABLE_BATCH_ATOMIC_WRITE=1",
    "-DSQLITE_ENABLE_DESERIALIZE",
    "-DHAVE_FDATASYNC",
]

if self.profile().endian == "big":
    _cflags += ["-DSHA3_BYTEORDER=4321", "-DSQLITE_BYTEORDER=4321"]
else:
    _cflags += ["-DSHA3_BYTEORDER=1234", "-DSQLITE_BYTEORDER=1234"]

tool_flags = {"CFLAGS": _cflags}


@subpackage("sqlite-devel")
def _devel(self):
    return self.default_devel()
