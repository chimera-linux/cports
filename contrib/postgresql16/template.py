_major = "16"
_default_ver = True  # should this version provide non-versioned resources?
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
    f"--bindir=/{_bindir}",
    f"--includedir=/{_includedir}",
    f"--datadir=/{_datadir}",
    "--disable-rpath",
    # "--with-llvm", # NOTE: postgresql 16 doesn't support llvm 16+
    "--with-libxml",
    "--with-ssl=openssl",
    "--with-uuid=e2fs",
    "--with-perl",
    "--with-python",
    "--with-tcl",
    "--with-lz4",
    "--with-zstd",
    "--with-system-tzdata=/usr/share/zoneinfo",
]
configure_gen = []
make_cmd = "gmake"
make_build_target = "world"
hostmakedepends = [
    "gmake",
    "pkgconf",
]
makedepends = [
    "icu-devel",
    "readline-devel",
    "zlib-devel",
    "linux-headers",
    "lz4-devel",
    "zstd-devel",
    "perl",
    "python-devel",
    "tcl-devel",
    "openssl-devel",
    "libxml2-devel",
    "e2fsprogs-devel",
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
# checks depend on libpq already being installed
options = ["!check"]


def post_install(self):
    if _default_ver:
        self.install_man("doc/src/sgml/man*/*", glob=True)
    self.install_file(self.files_path / "pltcl_create_tables.sql", "usr/share")


@subpackage(f"{pkgname}-devel")
def _devel(self):
    return [f"usr/lib/{pkgname}/pgxs"]


def _contrib_search(self, check):
    return filter(
        check,
        map(lambda p: p.name, (self.parent.cwd / "build/contrib").iterdir()),
    )


def _subpackage_install(self, path):
    self.parent.do(
        "gmake",
        "-C",
        f"build/{path}",
        f"DESTDIR={self.chroot_destdir}",
        "install",
    )


@subpackage(f"{pkgname}-contrib")
def _contrib(self):
    def subpackage():
        _subpackage_install(self, "contrib")
        for subdir in _contrib_search(
            self,
            lambda name: name.endswith("_plperl") or name.endswith("_plpython"),
        ):
            self.parent.do(
                "gmake",
                "-C",
                f"build/contrib/{subdir}",
                f"DESTDIR={self.chroot_destdir}",
                "uninstall",
            )

    return subpackage


@subpackage("libpq", _default_ver)
def _libpq(self):
    return ["usr/lib/libpq.so.*"]


@subpackage("libpq-devel", _default_ver)
def _libpq_devel(self):
    return [
        f"{_bindir}/pg_config",
        f"{_includedir}/libpq-*.h",
        f"{_includedir}/libpq/*",
        f"{_includedir}/pg_config*.h",
        f"{_includedir}/postgres_ext.h",
        "usr/lib/libpq.*",
        "usr/lib/libpgcommon*.a",
        "usr/lib/libpgport*.a",
        "usr/lib/pkgconfig/libpq.pc",
        "usr/lib/libpgfeutils.a",
    ]


@subpackage("libecpg", _default_ver)
def _libecpg(self):
    return ["usr/lib/libecpg.so.*", "usr/lib/libpgtypes.so*"]


@subpackage("libecpg-devel", _default_ver)
def _libecpg_devel(self):
    return [
        f"{_bindir}/ecpg",
        f"{_includedir}/ecpg*.h",
        f"{_includedir}/sqlca.h",
        f"{_includedir}/sqlda*.h",
        f"{_includedir}/pgtypes*.h",
        f"{_includedir}/sql3types.h",
        "usr/lib/libecpg.*",
        "usr/lib/libpgtypes.*",
        "usr/lib/pkgconfig/libecpg.pc",
        "usr/lib/pkgconfig/libpgtypes.pc",
    ]


@subpackage(f"{pkgname}-pltcl")
def _pltcl(self):
    return [
        f"{_srvlibdir}/pltcl.so",
        f"{_datadir}/extension/pltcl*",
        "usr/share/pltcl_create_tables.sql",
    ]


@subpackage(f"{pkgname}-plperl")
def _plperl(self):
    return [
        f"{_srvlibdir}/plperl.so",
        f"{_datadir}/extension/plperl*",
    ]


@subpackage(f"{pkgname}-plperl-contrib")
def _plperl_contrib(self):
    def subpackage():
        for subdir in _contrib_search(
            self, lambda name: name.endswith("_plperl")
        ):
            _subpackage_install(self, f"contrib/{subdir}")

    return subpackage


@subpackage(f"{pkgname}-plpython")
def _plpython(self):
    return [
        f"{_srvlibdir}/plpython3.so",
        f"{_datadir}/extension/plpython3*",
    ]


@subpackage(f"{pkgname}-plpython-contrib")
def _plpython_contrib(self):
    def subpackage():
        for subdir in _contrib_search(
            self, lambda name: name.endswith("_plpython")
        ):
            _subpackage_install(self, f"contrib/{subdir}")

    return subpackage


# TODO: read more about postgresql-common stuff from alpine
# TODO: dinit service
# TODO: tmpfile.d and sysuser.d files (where should databases be by default?)
