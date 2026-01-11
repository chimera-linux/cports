pkgname = "postgresql16"
pkgver = "16.10"
pkgrel = 1
# NOTE: version 16 doesn't work with meson + tarball
# switch to meson for version 17
build_style = "gnu_configure"
configure_args = [
    f"--bindir=/usr/lib/{pkgname}",
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
make_build_target = "world"
hostmakedepends = ["pkgconf"]
makedepends = [
    "dinit-chimera",
    "e2fsprogs-devel",
    "icu-devel",
    "libxml2-devel",
    "linux-headers",
    "lz4-devel",
    "openssl3-devel",
    "perl",
    "python-devel",
    "readline-devel",
    "tcl-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = ["postgresql-common", "tzdb"]
provides = ["postgresql-runtime"]
pkgdesc = "Sophisticated object-relational DBMS, version 16.x"
license = "PostgreSQL"
url = "https://www.postgresql.org"
source = f"https://ftp.postgresql.org/pub/source/v{pkgver}/postgresql-{pkgver}.tar.bz2"
sha256 = ["de8485f4ce9c32e3ddfeef0b7c261eed1cecb54c9bcd170e437ff454cb292b42"]
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
            "make",
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
        "make",
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
            f"usr/lib/{pkgname}/pg_config",
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
    @subpackage(f"postgresql16-contrib-{pn}")
    def _(self):
        self.subdesc = f"contrib-{pn}"
        self.depends += [self.parent]
        # autoinstalls
        if pn != "":
            self.install_if = [self.with_pkgver(f"{pkgname}-contrib")]
            # plperl, plpython, pltcl is special (more conditions)
            if pn.endswith("_plperl"):
                self.depends += [self.with_pkgver(f"{pkgname}-plperl")]
                self.install_if += [self.with_pkgver(f"{pkgname}-plperl")]
            elif pn.endswith("_plpython"):
                self.depends += [self.with_pkgver(f"{pkgname}-plpython")]
                self.install_if += [self.with_pkgver(f"{pkgname}-plpython")]
            elif pn.endswith("_pltcl"):
                self.depends += [self.with_pkgver(f"{pkgname}-pltcl")]
                self.install_if += [self.with_pkgver(f"{pkgname}-pltcl")]

        # contents are read from the file
        def inst():
            _take_list(self, pn)

        return inst


for _cont in _contrib_list:
    if _cont.startswith("!"):
        continue
    _contrib_pkg(_cont)


@subpackage(pkgname, alternative="postgresql")
def _(self):
    # the default version
    if _default_ver:
        self.provider_priority = 100

    def _links():
        # executables
        for f in (self.parent.destdir / f"usr/lib/{pkgname}").iterdir():
            self.make_link(f"usr/bin/{f.name}", f"../lib/{pkgname}/{f.name}")
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
        self.make_link("usr/lib/dinit.d/postgresql", pkgname)

    return _links


# these are provided by contribs, can't put them in the default alt
# nor should we make them actual alternatives (autoinstall instead)
def _contrib_alt(pn, pl):
    @subpackage(f"{pkgname}-{pn}", alternative="!postgresql")
    def _(self):
        self.subdesc = f"default links for {pn}"
        self.depends = [self.with_pkgver(f"postgresql-{pkgname}-default")]
        self.install_if = [
            self.with_pkgver(f"postgresql-{pkgname}-default"),
            self.with_pkgver(f"{pkgname}-contrib-{pn}"),
        ]

        def inst():
            for lnk in pl:
                self.make_link(f"usr/bin/{lnk}", f"../lib/{pkgname}/{lnk}")

        return inst


for _pn in _extra_cmds:
    _contrib_alt(_pn, _extra_cmds[_pn])


@subpackage("postgresql16-contrib")
def _(self):
    self.subdesc = "contrib"
    self.options = ["empty"]

    return []


@subpackage("postgresql16-client-libs", _default_ver)
def _(self):
    self.subdesc = "client library"
    # transitional
    self.provides = [self.with_pkgver("libpq")]

    return [
        "usr/lib/libpq.so.*",
    ]


@subpackage("postgresql16-client-devel", _default_ver)
def _(self):
    self.subdesc = "client library development files"
    # transitional
    self.provides = [self.with_pkgver("libpq-devel")]

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


@subpackage("postgresql16-ecpg-libs", _default_ver)
def _(self):
    self.subdesc = "embedded PostgreSQL for C"
    # transitional
    self.provides = [self.with_pkgver("libecpg")]

    return ["usr/lib/libecpg.so.*", "usr/lib/libpgtypes.so*"]


@subpackage("postgresql16-ecpg-devel", _default_ver)
def _(self):
    self.subdesc = "embedded PostgreSQL for C development files"
    # transitional
    self.provides = [self.with_pkgver("libecpg-devel")]

    return [
        f"usr/lib/{pkgname}/ecpg",
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


@subpackage("postgresql16-pltcl")
def _(self):
    self.subdesc = "PL/Tcl"
    self.depends = [self.parent]

    return [
        f"usr/lib/{pkgname}/pltcl.so",
        f"usr/share/{pkgname}/extension/pltcl*",
        f"usr/share/{pkgname}/pltcl_create_tables.sql",
    ]


@subpackage("postgresql16-plperl")
def _(self):
    self.subdesc = "PL/Perl"
    self.depends = [self.parent]

    return [
        f"usr/lib/{pkgname}/plperl.so",
        f"usr/share/{pkgname}/extension/plperl*",
    ]


@subpackage("postgresql16-plpython")
def _(self):
    self.subdesc = "PL/Python"
    self.depends = [self.parent]

    return [
        f"usr/lib/{pkgname}/plpython3.so",
        f"usr/share/{pkgname}/extension/plpython3*",
    ]


@subpackage("postgresql16-devel")
def _(self):
    return self.default_devel(extra=[f"usr/lib/{pkgname}/pgxs"])
