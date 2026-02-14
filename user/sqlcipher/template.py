pkgname = "sqlcipher"
pkgver = "4.13.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--enable-fts3",
    "--enable-fts4",
    "--enable-fts5",
    "--enable-shared",
    "--enable-threadsafe",
    "--with-tempstore=yes",
    "--dll-basename=libsqlcipher",
    "--soname=libsqlcipher.so.0",
]
make_check_target = "testfixture"
hostmakedepends = ["pkgconf"]
makedepends = [
    "openssl3-devel",
    "tcl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "SQLite fork featuring encrypted database files"
license = "BSD-3-Clause"
url = "https://github.com/sqlcipher/sqlcipher"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7ca5c11f70e460d6537844185621d5b3d683a001e6bad223d15bdf8eff322efa"
options = ["!parallel"]

if self.profile().cross:
    configure_args += [
        f"--host={self.profile().triplet}",
        f"--sysroot={self.profile().sysroot}",
        f"--with-readline-cflags=-I{self.profile().sysroot}",
    ]

_cflags = [
    "-DSQLITE_HAS_CODEC",
    "-DHAVE_FDATASYNC",
    "-DSQLITE_EXTRA_INIT=sqlcipher_extra_init",
    "-DSQLITE_EXTRA_SHUTDOWN=sqlcipher_extra_shutdown",
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
    "-DSQLCIPHER_TEST",
]

if self.profile().endian == "big":
    _cflags += ["-DSHA3_BYTEORDER=4321", "-DSQLITE_BYTEORDER=4321"]
else:
    _cflags += ["-DSHA3_BYTEORDER=1234", "-DSQLITE_BYTEORDER=1234"]

tool_flags = {"CFLAGS": _cflags, "LDFLAGS": ["-lcrypto"]}


def check(self):
    self.make.check()
    self.do("./testfixture", "test/sqlcipher.test")


def post_install(self):
    self.install_license("LICENSE.txt")

    self.mv(">/usr/bin/sqlite3", ">/usr/bin/sqlcipher")
    self.mv(
        ">/usr/share/man/man1/sqlite3.1", ">/usr/share/man/man1/sqlcipher.1"
    )

    self.mv(">/usr/lib/libsqlite3.a", ">/usr/lib/libsqlcipher.a")


@subpackage("sqlcipher-devel")
def _(self):
    return self.default_devel()
