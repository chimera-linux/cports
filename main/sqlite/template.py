pkgname = "sqlite"
pkgver = "3.53.0"
_amalg = "3530000"
pkgrel = 1
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
make_build_args = ["libsqlite3.so", "libsqlite3.a"]
hostmakedepends = ["pkgconf"]
makedepends = ["libedit-readline-devel", "zlib-ng-compat-devel"]
pkgdesc = "SQL Database Engine in a C library"
license = "blessing"
url = "https://sqlite.org"
source = f"https://sqlite.org/2026/sqlite-autoconf-{_amalg}.tar.gz"
sha256 = "851e9b38192fe2ceaa65e0baa665e7fa06230c3d9bd1a6a9662d02380d73365a"
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


def post_build(self):
    # compile with extra flag to get .recover command
    # this is security-sensitive so it should not be in the librar
    self.make.build(["sqlite3", "CFLAGS=-DSQLITE_ENABLE_DBPAGE_VTAB"])


@subpackage("sqlite-devel")
def _(self):
    return self.default_devel()
