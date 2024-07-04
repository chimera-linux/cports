pkgname = "postgresql16"
_major = pkgname.removeprefix("postgresql")
pkgver = f"{_major}.3"
pkgrel = 2
# NOTE: version 16 doesn't work with meson + tarball
# switch to meson for version 17
build_style = "gnu_configure"
configure_args = [
    f"--bindir=/usr/libexec/{pkgname}",
    f"--datadir=/usr/share/{pkgname}",
    "--includedir=/usr/include/postgresql",
    f"--sysconfdir=/etc/{pkgname}",
    "--disable-rpath",
    # "--with-llvm", # NOTE: postgresql 16 doesn't support llvm 16+
    "--with-libxml",
    "--with-lz4",
    "--with-perl",
    "--with-python",
    "--with-ssl=openssl",
    "--with-tcl",
    "--with-uuid=e2fs",
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
    "e2fsprogs-devel",
    "icu-devel",
    "libxml2-devel",
    "linux-headers",
    "lz4-devel",
    "openssl-devel",
    "perl",
    "python-devel",
    "readline-devel",
    "tcl-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = ["postgresql-common", "tzdata"]
provides = ["postgresql-runtime"]
pkgdesc = f"Sophisticated object-relational DBMS ({_major}.x)"
maintainer = "mia <mia@mia.jetzt>"
license = "PostgreSQL"
url = "https://www.postgresql.org"
source = [
    f"https://ftp.postgresql.org/pub/source/v{pkgver}/postgresql-{pkgver}.tar.bz2"
]
sha256 = ["331963d5d3dc4caf4216a049fa40b66d6bcb8c730615859411b9518764e60585"]
# checks depend on libpq already being installed
options = ["!check"]

_default_ver = True  # should this version provide non-versioned resources?

# complete list of contribs, must match what is built (checked)
# ones to skip can be prefixed with an exclamation mark
_contrib_list = [
    "adminpack",
    "amcheck",
    "auth_delay",
    "auto_explain",
    "basebackup_to_shell",
    "basic_archive",
    "bloom",
    "bool_plperl",
    "btree_gin",
    "btree_gist",
    "citext",
    "cube",
    "dblink",
    "dict_int",
    "dict_xsyn",
    "earthdistance",
    "file_fdw",
    "fuzzystrmatch",
    "hstore",
    "hstore_plperl",
    "hstore_plpython",
    "intagg",
    "intarray",
    "isn",
    "jsonb_plperl",
    "jsonb_plpython",
    "lo",
    "ltree",
    "ltree_plpython",
    "oid2name",
    "old_snapshot",
    "pageinspect",
    "passwordcheck",
    "pg_buffercache",
    "pg_freespacemap",
    "pg_prewarm",
    "pg_stat_statements",
    "pg_surgery",
    "pg_trgm",
    "pg_visibility",
    "pg_walinspect",
    "pgcrypto",
    "pgrowlocks",
    "pgstattuple",
    "postgres_fdw",
    "seg",
    "!sepgsql",  # selinux
    "spi",
    "sslinfo",
    "!start-scripts",  # mac only
    "tablefunc",
    "tcn",
    "test_decoding",
    "tsm_system_rows",
    "tsm_system_time",
    "unaccent",
    "uuid-ossp",
    "vacuumlo",
    "xml2",
]

# some contribs install extra commands, we need to link the providers
# occasionally check and update as needed...
_extra_cmds = {
    "oid2name": ["oid2name"],
    "vacuumlo": ["vacuumlo"],
}


def post_install(self):
    self.install_file(
        self.files_path / "pltcl_create_tables.sql",
        f"usr/share/{pkgname}",
    )
    # manpages; TODO man3 devel alternatives provider later
    for cat in [1, 3, 7]:
        for f in (self.cwd / f"doc/src/sgml/man{cat}").glob(f"*.{cat}"):
            self.install_file(f, f"usr/share/{pkgname}/man/man{cat}")
    # collect contrib list
    clist = set()
    for f in (self.cwd / "build/contrib").iterdir():
        if f.name == "Makefile":
            continue
        clist.add(f.name)
    for cont in _contrib_list:
        if cont.startswith("!"):
            clist.remove(cont.removeprefix("!"))
            continue
        clist.remove(cont)
        # install to a separate location to make up the file list
        self.do(
            "gmake",
            "-C",
            f"build/contrib/{cont}",
            f"DESTDIR={self.chroot_cwd}/tmp-contrib-{cont}",
            "install",
        )
        # capture file list and then install to where it should be
        with open(self.cwd / f"subpkg-list-{cont}.txt", "w") as flist:
            relp = self.cwd / f"tmp-contrib-{cont}"
            for f in relp.rglob("*"):
                if f.is_dir():
                    continue
                flist.write(f"{f.relative_to(relp)}\n")
        # and remove the temps
        self.rm(self.cwd / f"tmp-contrib-{cont}", recursive=True)
    # install all contrib in the destdir
    self.do(
        "gmake",
        "-C",
        "build/contrib",
        f"DESTDIR={self.chroot_destdir}",
        "install",
    )
    # check if there is anything left in the set
    if len(clist) > 0:
        self.error(f"leftover contribs: {clist}")
    # move some stuff not meant to be multiversioned
    if _default_ver:
        self.rename(
            f"usr/libexec/{pkgname}/pg_config",
            "usr/bin/pg_config",
            relative=False,
        )
    # service
    self.install_service(self.files_path / pkgname)


def _take_list(self, pn):
    lcwd = self.parent.cwd
    with open(lcwd / f"subpkg-list-{pn}.txt") as fl:
        for f in fl:
            self.take(f.strip())


def _contrib_pkg(pn):
    # build a subpackage for each contrib item
    @subpackage(f"{pkgname}-contrib-{pn}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} (contrib-{pn})"
        self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
        # autoinstalls
        if pn != "":
            self.install_if = [f"{pkgname}-contrib={pkgver}-r{pkgrel}"]
            # plperl, plpython, pltcl is special (more conditions)
            if pn.endswith("_plperl"):
                self.depends += [f"{pkgname}-plperl={pkgver}-r{pkgrel}"]
                self.install_if += [f"{pkgname}-plperl={pkgver}-r{pkgrel}"]
            elif pn.endswith("_plpython"):
                self.depends += [f"{pkgname}-plpython={pkgver}-r{pkgrel}"]
                self.install_if += [f"{pkgname}-plpython={pkgver}-r{pkgrel}"]
            elif pn.endswith("_pltcl"):
                self.depends += [f"{pkgname}-pltcl={pkgver}-r{pkgrel}"]
                self.install_if += [f"{pkgname}-pltcl={pkgver}-r{pkgrel}"]

        # contents are read from the file
        def inst():
            _take_list(self, pn)

        return inst


for _cont in _contrib_list:
    if _cont.startswith("!"):
        continue
    _contrib_pkg(_cont)


@subpackage(pkgname, alternative="postgresql")
def _default(self):
    # the default version
    if _default_ver:
        self.provider_priority = 100

    def _links():
        # executables
        for f in (self.parent.destdir / f"usr/libexec/{pkgname}").iterdir():
            self.make_link(
                f"usr/bin/{f.name}", f"../libexec/{pkgname}/{f.name}"
            )
        # manpages
        for f in (
            self.parent.destdir / f"usr/share/{pkgname}/man/man1"
        ).iterdir():
            self.make_link(
                f"usr/share/man/man1/{f.name}",
                f"../../{pkgname}/man/man1/{f.name}",
            )
        for f in (
            self.parent.destdir / f"usr/share/{pkgname}/man/man7"
        ).iterdir():
            self.make_link(
                f"usr/share/man/man7/{f.name}",
                f"../../{pkgname}/man/man7/{f.name}",
            )
        # service
        self.make_link("etc/dinit.d/postgresql", pkgname)

    return _links


# these are provided by contribs, can't put them in the default alt
# nor should we make them actual alternatives (autoinstall instead)
def _contrib_alt(pn, pl):
    @subpackage(f"postgresql-{pkgname}-{pn}-default")
    def _sp(self):
        self.pkgdesc = f"{pkgdesc} (default links for {pn})"
        self.depends = [f"postgresql-{pkgname}-default={pkgver}-r{pkgrel}"]
        self.install_if = [
            f"postgresql-{pkgname}-default={pkgver}-r{pkgrel}",
            f"{pkgname}-contrib-{pn}={pkgver}-r{pkgrel}",
        ]

        def inst():
            for lnk in pl:
                self.make_link(f"usr/bin/{lnk}", f"../libexec/{pkgname}/{lnk}")

        return inst


for _pn in _extra_cmds:
    _contrib_alt(_pn, _extra_cmds[_pn])


@subpackage(f"{pkgname}-contrib")
def _contrib(self):
    self.pkgdesc = f"{pkgname} (contrib)"
    self.options = ["empty"]

    return []


@subpackage("libpq", _default_ver)
def _libpq(self):
    self.pkgdesc = f"{pkgname} (client library)"

    return [
        "usr/lib/libpq.so.*",
    ]


@subpackage("libpq-devel", _default_ver)
def _libpq_devel(self):
    self.pkgdesc = f"{pkgname} (client library development files)"

    return [
        "usr/bin/pg_config",
        "usr/include/postgresql/libpq-*.h",
        "usr/include/postgresql/libpq/*",
        "usr/include/postgresql/pg_config*.h",
        "usr/include/postgresql/postgres_ext.h",
        "usr/lib/libpq.*",
        "usr/lib/libpgcommon*.a",
        "usr/lib/libpgport*.a",
        "usr/lib/pkgconfig/libpq.pc",
        "usr/lib/libpgfeutils.a",
    ]


@subpackage("libecpg", _default_ver)
def _libecpg(self):
    self.pkgdesc = f"{pkgname} (embedded PostgreSQL for C)"

    return ["usr/lib/libecpg.so.*", "usr/lib/libpgtypes.so*"]


@subpackage("libecpg-devel", _default_ver)
def _libecpg_devel(self):
    self.pkgdesc = f"{pkgname} (embedded PostgreSQL for C development files)"

    return [
        f"usr/libexec/{pkgname}/ecpg",
        "usr/include/postgresql/ecpg*.h",
        "usr/include/postgresql/sqlca.h",
        "usr/include/postgresql/sqlda*.h",
        "usr/include/postgresql/pgtypes*.h",
        "usr/include/postgresql/sql3types.h",
        "usr/lib/libecpg.*",
        "usr/lib/libpgtypes.*",
        "usr/lib/pkgconfig/libecpg.pc",
        "usr/lib/pkgconfig/libpgtypes.pc",
    ]


@subpackage(f"{pkgname}-pltcl")
def _pltcl(self):
    self.pkgdesc = f"{pkgdesc} (PL/Tcl)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        f"usr/lib/{pkgname}/pltcl.so",
        f"usr/share/{pkgname}/extension/pltcl*",
        f"usr/share/{pkgname}/pltcl_create_tables.sql",
    ]


@subpackage(f"{pkgname}-plperl")
def _plperl(self):
    self.pkgdesc = f"{pkgdesc} (PL/Perl)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        f"usr/lib/{pkgname}/plperl.so",
        f"usr/share/{pkgname}/extension/plperl*",
    ]


@subpackage(f"{pkgname}-plpython")
def _plpython(self):
    self.pkgdesc = f"{pkgdesc} (PL/Python)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        f"usr/lib/{pkgname}/plpython3.so",
        f"usr/share/{pkgname}/extension/plpython3*",
    ]


@subpackage(f"{pkgname}-devel")
def _devel(self):
    return self.default_devel(extra=[f"usr/lib/{pkgname}/pgxs"])
