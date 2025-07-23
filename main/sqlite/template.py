pkgname = "sqlite"
pkgver = "3.50.3"
_amalg = "3500300"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--enable-fts3",
    "--enable-fts4",
    "--enable-fts5",
    "--enable-shared",
    "--enable-threadsafe",
    "--editline",
    "--soname=legacy",
]
hostmakedepends = ["pkgconf"]
makedepends = ["libedit-readline-devel", "zlib-ng-compat-devel"]
pkgdesc = "SQL Database Engine in a C library"
license = "blessing"
url = "https://sqlite.org"
source = f"https://sqlite.org/2025/sqlite-autoconf-{_amalg}.tar.gz"
sha256 = "ec5496cdffbc2a4adb59317fd2bf0e582bf0e6acd8f4aae7e97bc723ddba7233"
# no tests
options = ["!parallel", "!check"]

if self.profile().cross:
    configure_args += [
        f"--host={self.profile().triplet}",
        f"--sysroot={self.profile().sysroot}",
        f"--with-readline-cflags=-I{self.profile().sysroot}",
    ]

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
