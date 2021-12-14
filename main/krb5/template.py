pkgname = "krb5"
_mver = "1.18"
pkgver = f"{_mver}.4"
pkgrel = 0
build_style = "gnu_configure"
configure_script = "src/configure"
configure_args = [
    "--disable-rpath", "--with-system-et", "--with-system-ss",
    "--without-system-verto", "--without-ldap",
    #"--with-system-db", "--with-ldap", FIXME
    "--without-tcl", "--enable-shared",
    "ac_cv_func_pthread_once=yes",
    "ac_cv_func_pthread_rwlock_init=yes",
    "ac_cv_func_regcomp=yes",
    "ac_cv_printf_positional=yes",
    "acx_pthread_ok=yes",
    "krb5_cv_attr_constructor_destructor=yes,yes",
]
hostmakedepends = ["e2fsprogs-devel", "flex", "perl", "pkgconf"]
makedepends = ["e2fsprogs-devel", "openssl-devel"]
pkgdesc = "MIT Kerberos 5 implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://web.mit.edu/kerberos"
source = f"{url}/dist/{pkgname}/{_mver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "66085e2f594751e77e82e0dbf7bbc344320fb48a9df2a633cfdd8f7d6da99fc8"
# libdb2 tests fail, check again once we have a libdb
options = ["!check"]

def post_install(self):
    self.install_license("NOTICE")
    self.install_service(self.files_path / "kadmind")
    self.install_service(self.files_path / "krb5kdc")

@subpackage("krb5-client")
def _client(self):
    self.pkgdesc = f"{pkgdesc} (client programs)"
    self.suid_files = ["usr/bin/ksu"]

    def _install():
        for f in [
            "uuclient", "ktutil", "kswitch", "gss-client", "kvno", "kinit",
            "kpasswd", "kdestroy", "sclient", "kadmin", "k5srvutil",
            "sim_client", "klist", "ksu"
        ]:
            self.take(f"usr/bin/{f}")
            self.take(f"usr/share/man/man1/{f}.1", missing_ok = True)

    return _install

@subpackage("krb5-libs")
def _libs(self):
    return self.default_libs()

@subpackage("krb5-devel")
def _devel(self):
    self.depends += ["e2fsprogs-devel"]

    return self.default_devel(man = True)
