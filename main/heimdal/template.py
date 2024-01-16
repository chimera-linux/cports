pkgname = "heimdal"
pkgver = "7.8.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-kcm",
    "--disable-otp",  # needs ndbm
    "--without-openssl",  # FIXME
    "--with-hcrypto-default-backend=hcrypto",  # FIXME: switch back to ossl
    "--without-berkeley-db",
    "--with-db-type-preference=sqlite",
    f"--with-sqlite3={self.profile().sysroot / 'usr'}",
    f"--with-libedit={self.profile().sysroot / 'usr'}",
    f"--with-libintl={self.profile().sysroot / 'usr'}",
]
make_cmd = "gmake"
# install and check are racey
make_install_args = ["-j1"]
make_check_args = ["-j1"]
hostmakedepends = [
    "gmake",
    "pkgconf",
    "flex",
    "byacc",
    "perl",
    "perl-json",
    "python",
    "mandoc",
    "texinfo",
    "gettext",
    "automake",
    "libtool",
    "e2fsprogs-devel",  # for compile_et
]
# TODO: reenable openssl once we've figured out the openssl 3.x regressions
makedepends = [
    "sqlite-devel",
    "libedit-devel",
    "libcap-ng-devel",
    "linux-pam-devel",
    "gettext-devel",
    "ncurses-devel",
    "e2fsprogs-devel",
]
pkgdesc = "Implementation of the Kerberos authentication protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://heimdal.software"
source = f"https://github.com/heimdal/heimdal/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "fd87a207846fa650fd377219adc4b8a8193e55904d8a752c2c3715b4155d8d38"
exec_wrappers = [("/usr/bin/mandoc", "nroff")]

if self.profile().endian == "big":
    configure_args.append("--enable-bigendian")
else:
    configure_args.append("--enable-littleendian")


def post_install(self):
    self.install_license("LICENSE")

    for f in (self.destdir / "usr/share/man").glob("cat*"):
        self.rm(f, recursive=True)
    for f in (self.destdir / "usr/lib").glob("windc*"):
        self.rm(f)

    self.rm(self.destdir / "usr/bin/bsearch")
    self.rm(self.destdir / "usr/bin/idn-lookup")
    self.rm(self.destdir / "usr/share/man/man1/bsearch.1")

    self.mv(self.destdir / "usr/bin/su", self.destdir / "usr/bin/ksu")
    self.mv(self.destdir / "usr/bin/pagsh", self.destdir / "usr/bin/kpagsh")
    self.mv(
        self.destdir / "usr/share/man/man1/su.1",
        self.destdir / "usr/share/man/man1/ksu.1",
    )
    self.mv(
        self.destdir / "usr/share/man/man1/pagsh.1",
        self.destdir / "usr/share/man/man1/kpagsh.1",
    )

    # hardlink resolution
    self.rm(self.destdir / "usr/share/man/man8/ipropd-master.8")
    self.rm(self.destdir / "usr/share/man/man8/ipropd-slave.8")
    self.rm(self.destdir / "usr/share/man/man5/qop.5")
    self.install_link("iprop.8", "usr/share/man/man8/ipropd-master.8")
    self.install_link("iprop.8", "usr/share/man/man8/ipropd-slave.8")
    self.install_link("mech.5", "usr/share/man/man5/qop.5")


def _genlib(pkgn, desc):
    @subpackage(f"lib{pkgn}")
    def _lib(self):
        self.pkgdesc = f"{desc} library from Heimdal Kerberos"

        return [f"usr/lib/lib{pkgn}.so.*"]


for _libn, _ldesc in [
    ("asn1", "ASN.1"),
    ("gssapi", "GSSAPI"),
    ("hcrypto", "Crypto"),
    ("hdb", "Kadmin server"),
    ("heimbase", "Base"),
    ("heimntlm", "NTLM"),
    ("hx509", "X509"),
    ("kadm5clnt", "Kadmin client"),
    ("kadm5srv", "Kadmin server"),
    ("kafs", "KAFS"),
    ("kdc", "KDC"),
    ("krb5", "Kerberos"),
    ("roken", "Roken"),
    ("sl", "SL"),
    ("wind", "Stringprep implementation"),
]:
    _genlib(_libn, _ldesc)


# TODO: add service
@subpackage("heimdal-kcm")
def _kcm(self):
    self.pkgdesc = "Heimdal KCM daemon"

    return ["usr/libexec/kcm", "usr/share/man/man8/kcm.8"]


# TODO: add services
@subpackage("heimdal-kdc")
def _kdc(self):
    self.pkgdesc = "Heimdal Key Distribution Center"

    return [
        "usr/bin/iprop-log",
        "usr/bin/kstash",
        "usr/libexec/digest-service",
        "usr/libexec/hprop",
        "usr/libexec/hpropd",
        "usr/libexec/ipropd*",
        "usr/libexec/kadmind",
        "usr/libexec/kdc",
        "usr/libexec/kpasswdd",
        "usr/share/man/man8/hprop*.8",
        "usr/share/man/man8/iprop*.8",
        "usr/share/man/man8/kadmind.8",
        "usr/share/man/man8/kdc.8",
        "usr/share/man/man8/kpasswdd.8",
        "usr/share/man/man8/kstash.8",
    ]


@subpackage("heimdal-clients")
def _client(self):
    self.pkgdesc = f"{pkgdesc} (clients)"
    self.suid_files = ["usr/bin/ksu"]

    def _install():
        self.take("usr/libexec/kdigest")
        self.take("usr/libexec/kimpersonate")
        self.take("usr/share/man/man8/kdigest.8")
        self.take("usr/share/man/man8/kimpersonate.8")

        for cl in [
            "afslog",
            "gsstool",
            "hxtool",
            "heimtools",
            "kadmin",
            "kdestroy",
            "kf",
            "kgetcred",
            "kinit",
            "klist",
            "kpasswd",
            "kswitch",
            "kpagsh",
            "ksu",
            "ktutil",
            "string2key",
            "verify_krb5_conf",
        ]:
            self.take(f"usr/bin/{cl}")
            self.take(f"usr/share/man/man*/{cl}.*", missing_ok=True)

    return _install


@subpackage("heimdal-devel")
def _devel(self):
    # provides com_err
    self.depends += ["e2fsprogs-devel"]
    # lots of small files as hardlinks in man3, too much to resolve all
    self.options = ["hardlinks"]

    return self.default_devel()
