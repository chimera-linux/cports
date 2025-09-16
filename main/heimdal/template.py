pkgname = "heimdal"
pkgver = "7.8.0"
pkgrel = 2
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
    f"--with-openldap={self.profile().sysroot / 'usr'}",
]
# install and check are racey
make_install_args = ["-j1"]
make_check_args = ["-j1"]
hostmakedepends = [
    "automake",
    "byacc",
    "e2fsprogs-devel",  # for compile_et
    "flex",
    "gettext",
    "libtool",
    "mandoc",
    "perl",
    "perl-json",
    "pkgconf",
    "python",
    "texinfo",
]
# TODO: reenable openssl once we've figured out the openssl 3.x regressions
makedepends = [
    "dinit-chimera",
    "e2fsprogs-devel",
    "gettext-devel",
    "libcap-ng-devel",
    "libedit-devel",
    "linux-pam-devel",
    "ncurses-devel",
    "openldap-devel",
    "sqlite-devel",
]
pkgdesc = "Implementation of the Kerberos authentication protocol"
license = "BSD-3-Clause"
url = "https://heimdal.software"
source = f"https://github.com/heimdal/heimdal/releases/download/heimdal-{pkgver}/heimdal-{pkgver}.tar.gz"
sha256 = "fd87a207846fa650fd377219adc4b8a8193e55904d8a752c2c3715b4155d8d38"
options = ["linkundefver"]
exec_wrappers = [("/usr/bin/mandoc", "nroff")]

if self.profile().endian == "big":
    configure_args.append("--enable-bigendian")
else:
    configure_args.append("--enable-littleendian")


def post_install(self):
    self.install_license("LICENSE")

    self.uninstall("usr/share/man/cat*", glob=True)
    self.uninstall("usr/lib/windc*", glob=True)

    self.uninstall("usr/bin/bsearch")
    self.uninstall("usr/bin/idn-lookup")
    self.uninstall("usr/share/man/man1/bsearch.1")

    self.rename("usr/bin/su", "ksu")
    self.rename("usr/bin/pagsh", "kpagsh")
    self.rename("usr/share/man/man1/su.1", "ksu.1")
    self.rename("usr/share/man/man1/pagsh.1", "kpagsh.1")

    # hardlink resolution
    self.uninstall("usr/share/man/man8/ipropd-master.8")
    self.uninstall("usr/share/man/man8/ipropd-slave.8")
    self.uninstall("usr/share/man/man5/qop.5")
    self.install_link("usr/share/man/man8/ipropd-master.8", "iprop.8")
    self.install_link("usr/share/man/man8/ipropd-slave.8", "iprop.8")
    self.install_link("usr/share/man/man5/qop.5", "mech.5")

    self.install_service(self.files_path / "heimdal-kdc")
    self.install_service(self.files_path / "heimdal-kadmind")
    self.install_service(self.files_path / "heimdal-kpasswdd")


def _genlib(pkgn, desc):
    @subpackage(f"heimdal-{pkgn}-libs")
    def _(self):
        self.pkgdesc = f"{desc} library from Heimdal Kerberos"
        # transitional
        self.provides = [self.with_pkgver(f"lib{pkgn}")]

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
def _(self):
    self.pkgdesc = "Heimdal KCM daemon"

    return ["usr/libexec/kcm", "usr/share/man/man8/kcm.8"]


@subpackage("heimdal-kdc")
def _(self):
    self.pkgdesc = "Heimdal Key Distribution Center"

    return [
        "usr/bin/iprop-log",
        "usr/bin/kstash",
        "usr/lib/dinit.d/heimdal-kadmind",
        "usr/lib/dinit.d/heimdal-kdc",
        "usr/lib/dinit.d/heimdal-kpasswdd",
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
def _(self):
    self.subdesc = "clients"
    self.file_modes = {"usr/bin/ksu": ("root", "root", 0o4755)}

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
            self.take(f"cmd:{cl}")

    return _install


@subpackage("heimdal-devel")
def _(self):
    # provides com_err
    self.depends += ["e2fsprogs-devel"]
    # lots of small files as hardlinks in man3, too much to resolve all
    self.options = ["hardlinks"]

    return self.default_devel()
