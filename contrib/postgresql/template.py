pkgname = "postgresql"
pkgver = "16.2"
pkgrel = 0
build_style = "configure"
configure_args = [
    # TODO: review path choices - alpine puts pkgname in a few of these
    "--bindir=/usr/bin",
    "--libdir=/usr/lib",
    "--includedir=/usr/include",
    "--datadir=/usr/share",
    "--disable-rpath",  # TODO: alpine does this but the docs say not to. should we?
    "--with-system-tzdata=/usr/share/zoneinfo",
]
make_cmd = "gmake"
makedepends = [
    "gmake",
    "pkgconf",
    "icu-devel",
    "readline-devel",
    "zlib-devel",
    "linux-headers",
]
depends = ["tzdata"]
pkgdesc = "Sophisticated object-relational DBMS"
maintainer = "mia <mia@mia.jetzt>"
license = "PostgreSQL"
url = "https://www.postgresql.org"
source = [
    f"https://ftp.postgresql.org/pub/source/v{pkgver}/postgresql-{pkgver}.tar.bz2"
]
sha256 = ["446e88294dbc2c9085ab4b7061a646fa604b4bec03521d5ea671c2e5ad9b2952"]
# TODO: checks rely on libpq already being installed
# could maybe makedepend on libpq once it's in the repos?
# note: alpine doesn't do checks either
options = ["!check"]


# NOTE: most of these subpackages are based on whatever alpine is doing, so they might need tweaking


@subpackage("libpq")
def _libpq(self):
    self.pkgdesc = "PostgreSQL client library"
    return ["usr/lib/libpq.so*"]


@subpackage("libpq-devel")
def _libpq_devel(self):
    self.depends += ["libpq"]
    return [
        "usr/bin/pg_config",
        "usr/include/libpq-*.h",
        "usr/include/libpq/*",
        "usr/include/pg_config*.h",
        "usr/include/postgres_ext.h",
        "usr/lib/libpq.*",
        "usr/lib/libpgcommon*.a",
        "usr/lib/libpgport*.a",
        "usr/lib/pkgconfig/libpq.pc",
        # TODO: should this be included here?
        # they aren't on alpine, but i don't see why postgres would need them
        # either way, the file triggers static library lints
        "usr/lib/libpgfeutils.a",
    ]


@subpackage("libecpg")
def _libecpg(self):
    self.pkgdesc = "Embedded SQL in C"
    return [
        "usr/lib/libecpg.so*",
        "usr/lib/libpgtypes.so*",  # TODO: should libpgtypes be it's own package?
    ]


@subpackage("libecpg-devel")
def _libecpg_devel(self):
    self.depends += ["libecpg"]
    return [
        "usr/bin/ecpg",
        "usr/include/ecpg*.h",
        "usr/include/pgtypes*.h",
        "usr/include/sql3types.h",
        "usr/include/sqlca.h",
        "usr/include/sqlda*.h",
        "usr/lib/libecpg.*",
        "usr/lib/libpgtypes.*",
        "usr/lib/pkgconfig/libecpg.pc",
        "usr/lib/pkgconfig/libpgtypes.pc",
    ]


@subpackage("postgresql-devel")
def _postgresql_devel(self):
    self.depends += ["postgresql"]
    return ["usr/lib/postgresql/pgxs"]


# TODO: move contrib stuff to postgres-contrib
# TODO: consider postgres-client
# see: https://git.alpinelinux.org/aports/tree/main/postgresql16/APKBUILD#n114
# TODO: JIT
# see: https://git.alpinelinux.org/aports/tree/main/postgresql16/APKBUILD#n16
# TODO: postgresql-man
# TODO: dinit service
# TODO: tmpfile.d and sysuser.d files (where should databases be by default?)
