# TODO: service files, also probably needs overall cleanup/fixup
# for now it's enough to get us libsmbclient
pkgname = "samba"
pkgver = "4.15.9"
pkgrel = 0
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--enable-fhs",
    "--sbindir=/usr/bin",
    "--localstatedir=/var",
    "--sysconfdir=/etc",
    "--with-piddir=/run/samba",
    "--with-sockets-dir=/run/samba",
    "--with-privatelibdir=/usr/lib",
    "--with-lockdir=/run/lock/samba",
    "--with-modulesdir=/usr/lib/samba",
    "--with-privatedir=/etc/samba/private",
    "--with-pammodulesdir=/usr/lib/security",
    "--disable-rpath",
    "--disable-rpath-install",
    "--without-systemd",
    "--bundled-libraries=NONE",
    "--with-system-heimdalkrb5",
    "--with-cluster-support",
    "--without-ad-dc",
]
hostmakedepends = [
    "pkgconf", "python", "perl", "perl-parse-yapp", "gettext-tiny-devel",
    "libtasn1-progs", "docbook-xsl-nons", "xsltproc", "rpcsvc-proto",
    "flex", "bison", "tdb-python", "tevent-python", "ldb-python",
]
makedepends = [
    "gettext-tiny-devel", "python-devel", "libtirpc-devel", "popt-devel",
    "e2fsprogs-devel", "zlib-devel", "ncurses-devel", "libarchive-devel",
    "musl-bsd-headers", "linux-pam-devel", "heimdal-devel", "acl-devel",
    "attr-devel", "cups-devel", "jansson-devel", "avahi-devel",
    "dbus-devel", "openldap-devel", "tdb-devel", "talloc-devel",
    "tevent-devel", "ldb-devel", "gnutls-devel", "cmocka-devel", "musl-nscd",
]
pkgdesc = "SMB/CIFS file, print, and login server for Unix"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.samba.org"
source = f"https://download.samba.org/pub/samba/stable/{pkgname}-{pkgver}.tar.gz"
sha256 = "9682a2c71c2ff253aa27cbb01260eac897ff625cf39db20ee32073e5386fe219"
# we don't want their makefile
env = {"PYTHONHASHSEED": "1", "WAF_MAKE": "1"}
# check needs --enable-selftest, which needs extra system dependencies
options = ["!cross", "!check"]

_idmap_modules = ["ad", "rid", "adex", "hash", "tdb2"]
_pdb_modules = ["tdbsam", "ldap", "ads", "smbpasswd", "wbc_sam", "samba4"]
_auth_modules = ["unix", "wbc", "server", "netlogond", "script", "samba4"]

configure_args.append("--with-shared-modules=" + ",".join(
    list(map(lambda v: f"idmap_{v}", _idmap_modules)) +
    list(map(lambda v: f"pdb_{v}", _pdb_modules)) +
    list(map(lambda v: f"auth_{v}", _auth_modules))
))

# adding secrets3 causes undefined references
configure_args.append("--builtin-libraries=" + ",".join([
    "CHARSET3", "MESSAGING_SEND", "MESSAGING", "LIBWBCLIENT_OLD", "addns",
    "ads", "asn1util", "auth", "authkrb5", "cmdline_contexts",
    "cmdline-credentials", "cli_cldap", "cli-ldap-common", "cli-nbt",
    "cli_smb_common", "cli_spoolss", "clidns", "common-auth",
    "ctdb-event-client", "dbwrap", "dcerpc-pkt-auth", "events", "genrand",
    "gensec", "gse", "http", "interfaces", "krb5samba", "ldbsamba",
    "libcli_lsa3", "libcli_netlogon3", "libsmb", "messages_dgm",
    "messages_util", "mscat", "msghdr", "msrpc3", "netif", "npa_tstream",
    "popt_samba3", "popt_samba3_cmdline", "registry", "replace",
    "samba-cluster-support", "samba-debug", "samba-modules",
    "samba-security", "samba-sockets", "samba3-util", "samdb-common",
    "server_id_db", "server-role", "smbclient-raw", "smbd_shim",
    "socket-blocking", "sys_rw", "talloc_report_printf", "talloc_report",
    "tevent-util", "time-basic", "trusts_util", "util_reg", "util_setid",
    "util_tdb"
]))

def post_install(self):
    self.install_file(
        "examples/smb.conf.default", "etc/samba", name = "smb.conf"
    )
    self.install_file(
        self.files_path / "samba.pam", "etc/pam.d", name = "samba"
    )
    self.rm(self.destdir / "etc/sudoers.d", recursive = True)
    # symlink cups backend
    self.install_dir("usr/lib/cups/backend")
    self.install_link("/usr/bin/smbspool", "usr/lib/cups/backend/smb")
    # private dir
    self.install_dir("etc/samba/private", mode = 0o750, empty = True)

@subpackage("samba-client")
def _smbclient(self):
    self.pkgdesc = f"{pkgdesc} (client utilities)"

    def install():
        for f in [
            "dbwrap_tool", "mdsearch", "mvxattr", "nmblookup", "ntlm_auth",
            "oLschema2ldif", "regdiff", "regpatch", "regshell", "regtree",
            "rpcclient", "sharesec", "smbcacls", "smbclient", "smbcquotas",
            "smbget", "smbtar", "smbtree", "wbinfo",
        ]:
            self.take(f"usr/bin/{f}")
            self.take(f"usr/share/man/man1/{f}.1")

        for f in [
            "cifsdd", "samba-regedit", "smbspool"
        ]:
            self.take(f"usr/bin/{f}")
            self.take(f"usr/share/man/man8/{f}.8")

        self.take("usr/bin/dumpmscat")
        self.take("usr/share/man/man5/smbgetrc.5")
        self.take("usr/libexec/samba/smbspool_krb5_wrapper")
        self.take("usr/share/man/man8/smbspool_krb5_wrapper.8")
        self.take("usr/lib/cups/backend/smb")

    return install

@subpackage("samba-ctdb")
def _ctdb(self):
    self.pkgdesc = f"{pkgdesc} (clustered TDB support)"

    def install():
        self.take("usr/bin/ctdb*")

        for f in [1, 5, 7]:
            self.take(f"usr/share/man/man{f}/ctdb*")

        for f in ["ltdbtool", "onnode", "ping_pong"]:
            self.take(f"usr/bin/{f}")
            self.take(f"usr/share/man/man1/{f}.1")

        self.take("usr/libexec/ctdb")
        self.take("usr/share/ctdb")
        self.take("etc/ctdb")

    return install

@subpackage("samba-libs")
def _libs(self):
    def install():
        for f in [
            "dcerpc", "dcerpc-binding", "ndr-krb5pac", "ndr-standard",
            "ndr-nbt", "ndr", "samba-credentials", "samba-errors",
            "samba-hostconfig", "samba-passdb", "samba-util", "samdb",
            "smbclient", "smbconf", "smbldap", "wbclient",
        ]:
            self.take(f"usr/lib/lib{f}.so.*")

        for f in [
            "cli-ldap", "cliauth", "cluster", "cmdline", "common-auth",
            "dcerpc-samba", "flag-mapping", "gpo", "iov-buf", "ndr-samba",
            "ndr", "printer-driver", "secrets3", "smb-transport", "tdb-wrap",
            "winbind-client"
        ]:
            self.take(f"usr/lib/lib{f}-samba4.so")

        self.take("usr/share/man/man7/libsmbclient.7")

    return install

@subpackage("samba-devel")
def _devel(self):
    def install():
        self.take("usr/include")
        self.take("usr/lib/pkgconfig")
        # prevent private libraries from being moved
        for f in (self.parent.destdir / "usr/lib").glob("*.so"):
            if f.is_symlink():
                self.take(f"usr/lib/{f.name}")

    return install

@subpackage("samba-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python3*"]
