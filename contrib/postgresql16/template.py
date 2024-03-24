_major = "16"
_default_ver = True  # should this version provide -libs?
pkgname = f"postgresql{_major}"
pkgver = f"{_major}.2"
pkgrel = 0
# NOTE: version 16 doesn't work with meson + tarball
# switch to meson for version 17
build_style = "gnu_configure"
_bindir = f"usr/libexec/{pkgname}"
_datadir = f"usr/share/{pkgname}"
_includedir = "usr/include/postgresql"
_srvlibdir = f"usr/lib/{pkgname}"
configure_args = [
    # TODO: review path choices - alpine puts pkgname in a few of these
    f"--bindir=/{_bindir}",
    "--libdir=/usr/lib",
    f"--includedir=/{_includedir}",
    f"--datadir=/{_datadir}",
    "--disable-rpath",  # TODO: alpine does this but the docs say not to. should we?
    "--with-system-tzdata=/usr/share/zoneinfo",
]
configure_gen = []
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
]
makedepends = [
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


@subpackage(f"postgresql{_major}-devel")
def _postgresql_devel(self):
    return [f"usr/lib/{pkgname}/pgxs"]


@subpackage("postgresql-libs", _default_ver)
def _libs(self):
    return [
        "usr/lib/libpq.so.*",
        "usr/lib/libecpg.so.*",
        "usr/lib/libpgtypes.so*",
    ]


# TODO: a lot of this could probably be done using the default subpackage functions
@subpackage("postgresql-libs-devel", _default_ver)
def _libs_devel(self):
    return [
        # libpq
        f"{_bindir}/pg_config",
        f"{_includedir}/libpq-*.h",
        f"{_includedir}/libpq/*",
        f"{_includedir}/pg_config*.h",
        f"{_includedir}/postgres_ext.h",
        "usr/lib/libpq.*",
        "usr/lib/libpgcommon*.a",
        "usr/lib/libpgport*.a",
        "usr/lib/pkgconfig/libpq.pc",
        # libecpg
        f"{_bindir}/ecpg",
        f"{_includedir}/ecpg*.h",
        f"{_includedir}/sqlca.h",
        f"{_includedir}/sqlda*.h",
        "usr/lib/libecpg.*",
        "usr/lib/pkgconfig/libecpg.pc",
        # libpgtypes
        f"{_includedir}/pgtypes*.h",
        f"{_includedir}/sql3types.h",
        "usr/lib/libpgtypes.*",
        "usr/lib/pkgconfig/libpgtypes.pc",
        # misc
        "usr/lib/libpgfeutils.a",
    ]


# TODO: move contrib stuff to postgres-contrib
# TODO: consider postgres-client
# see: https://git.alpinelinux.org/aports/tree/main/postgresql16/APKBUILD#n114
# TODO: JIT
# see: https://git.alpinelinux.org/aports/tree/main/postgresql16/APKBUILD#n16
# TODO: postgresql-man
# TODO: dinit service
# TODO: tmpfile.d and sysuser.d files (where should databases be by default?)
# TODO: read more about postgresql-common stuff from alpine
