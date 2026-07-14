# mirrors changes in main/sqlite
pkgname = "sqlcipher"
pkgver = "4.17.0"
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
    "--editline",
    "--dll-basename=libsqlcipher",
    "--soname=legacy",
]
make_build_args = ["libsqlcipher.so", "lib"]
make_check_target = "testfixture"
hostmakedepends = ["pkgconf"]
makedepends = [
    "libedit-readline-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["tcl-devel"]
pkgdesc = "SQLite fork with encryption support"
license = "BSD-3-Clause"
url = "https://github.com/sqlcipher/sqlcipher"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "79c0e164b9c059e7487bf8f29272f601cca5f3312cc267461f81e349962a5058"

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

tool_flags = {"CFLAGS": _cflags, "LDFLAGS": ["-lssl", "-lcrypto"]}


def post_build(self):
    # compile with extra flag to get .recover command
    # this is security-sensitive so it should not be in the library
    self.make.build(["sqlite3", "CFLAGS=-DSQLITE_ENABLE_DBPAGE_VTAB"])


def post_check(self):
    self.do("./testfixture", "test/sqlcipher.test")


def post_install(self):
    self.install_license("LICENSE.txt")
    # renames not handled by the patch
    self.rename("usr/bin/sqlite3", "usr/bin/sqlcipher")
    self.rename("usr/share/man/man1/sqlite3.1", "sqlcipher.1")
    self.rename("usr/lib/libsqlite3.a", "libsqlcipher.a")
    # we don't need the extension, but we have to build it to get tests
    self.uninstall("usr/lib/tcl*", glob=True)


@subpackage("sqlcipher-devel")
def _(self):
    return self.default_devel()
