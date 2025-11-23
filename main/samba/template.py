# TODO: service files, cleanup
pkgname = "samba"
pkgver = "4.23.3"
pkgrel = 0
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--enable-fhs",
    "--sbindir=/usr/bin",
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "--localstatedir=/var",
    "--sysconfdir=/etc",
    "--with-piddir=/run/samba",
    "--with-sockets-dir=/run/samba",
    "--with-privatelibdir=/usr/lib",
    "--with-lockdir=/run/lock/samba",
    "--with-modulesdir=/usr/lib/samba",
    "--with-statedir=/var/lib/samba",
    "--with-cachedir=/var/cache/samba",
    "--with-privatedir=/var/lib/samba/private",
    "--with-pammodulesdir=/usr/lib/security",
    "--with-smbpasswd-file=/etc/samba/smbpasswd",
    "--with-socketpath=/run/ctdb/ctdbd.socket",
    "--with-logdir=/var/log/ctdb",
    "--enable-avahi",
    "--enable-spotlight",
    "--disable-rpath",
    "--disable-rpath-install",
    "--disable-fault-handling",
    "--without-systemd",
    "--bundled-libraries=libquic,NONE",
    "--with-system-heimdalkrb5",
    "--with-cluster-support",
    "--with-automount",
    "--with-winbind",
    "--with-syslog",
    "--with-quota",
    "--with-pam",
    "--without-ad-dc",
]
hostmakedepends = [
    "bison",
    "docbook-xsl-nons",
    "flex",
    "gettext-devel",
    "heimdal",
    "libtasn1-progs",
    "libxslt-progs",
    "perl",
    "perl-parse-yapp",
    "pkgconf",
    "python",
    "rpcsvc-proto",
    "tdb-python",
    "tevent-python",
]
makedepends = [
    "acl-devel",
    "attr-devel",
    "avahi-devel",
    "cmocka-devel",
    "cups-devel",
    "dbus-devel",
    "e2fsprogs-devel",
    "fuse-devel",
    "gettext-devel",
    "glib-devel",
    "gnutls-devel",
    "gpgme-devel",
    "heimdal-devel",
    "icu-devel",
    "jansson-devel",
    "libarchive-devel",
    "libedit-readline-devel",
    "libtirpc-devel",
    "linux-pam-devel",
    "lmdb-devel",
    "musl-bsd-headers",
    "musl-nscd",
    "ncurses-devel",
    "ngtcp2-devel",
    "openldap-devel",
    "popt-devel",
    "python-devel",
    "talloc-devel",
    "tdb-devel",
    "tevent-devel",
    "zlib-ng-compat-devel",
]
depends = [
    "tdb-progs",
    self.with_pkgver("samba-common"),
    self.with_pkgver("samba-libs"),
]
pkgdesc = "SMB/CIFS file, print, and login server for Unix"
license = "GPL-3.0-or-later"
url = "https://www.samba.org"
source = f"https://download.samba.org/pub/samba/stable/samba-{pkgver}.tar.gz"
sha256 = "06cdbb27a6956978b045455fe0696d998ffbac8d24ba24de87a4ef8200813320"
tool_flags = {"CFLAGS": ["-D_BSD_SOURCE"]}
env = {"PYTHONHASHSEED": "1"}
# check needs --enable-selftest, which needs extra system dependencies
options = ["!cross", "!check", "!installroot", "linkundefver"]

# idmap_ad should go here if active directory is enabled
configure_args.append(
    "--with-shared-modules="
    + ",".join(
        [
            "idmap_ad",
            "idmap_rid",
            "idmap_adex",
            "idmap_hash",
            "idmap_ldap",
            "idmap_tdb2",
            "vfs_nfs4acl_xattr",
        ]
    )
)


def post_install(self):
    self.install_file("examples/smb.conf.default", "etc/samba", name="smb.conf")
    self.install_file(
        self.files_path / "samba.pam", "usr/lib/pam.d", name="samba"
    )
    self.uninstall("usr/share/man/man7/traffic_learner.7")
    self.uninstall("usr/share/man/man7/traffic_replay.7")
    # symlink cups backend
    self.install_dir("usr/lib/cups/backend")
    self.install_link("usr/lib/cups/backend/smb", "../../../bin/smbspool")
    # private dir
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("samba-common")
def _(self):
    self.subdesc = "common files and programs"
    self.depends = [self.with_pkgver("samba-libs")]

    return [
        "usr/lib/pam.d",
        "usr/bin/dbwrap_tool",
        "usr/bin/net",
        "usr/bin/nmblookup",
        "usr/bin/samba-regedit",
        "usr/bin/samba-tool",
        "usr/bin/smbpasswd",
        "usr/bin/testparm",
        "usr/lib/samba/rpcd_*",
        "usr/lib/samba/samba-dcerpcd",
        "usr/share/man/man1/dbwrap_tool.1",
        "usr/share/man/man1/nmblookup.1",
        "usr/share/man/man1/testparm.1",
        "usr/share/man/man5/lmhosts.5",
        "usr/share/man/man5/smb.conf.5",
        "usr/share/man/man5/smbpasswd.5",
        "usr/share/man/man7/samba.7",
        "usr/share/man/man8/net.8",
        "usr/share/man/man8/samba-dcerpcd.8",
        "usr/share/man/man8/samba-regedit.8",
        "usr/share/man/man8/samba-tool.8",
        "usr/share/man/man8/smbpasswd.8",
    ]


@subpackage("samba-registry-progs")
def _(self):
    self.pkgdesc = "Tools for viewing and manipulating the Windows registry"
    self.depends = [self.with_pkgver("samba-libs")]

    return [
        "usr/bin/reg*",
        "usr/share/man/man1/reg*.1",
    ]


@subpackage("samba-client-libs")
def _(self):
    self.subdesc = "client library"
    self.depends = [self.with_pkgver("samba-libs")]
    # transitional
    self.provides = [self.with_pkgver("libsmbclient")]

    return [
        "usr/lib/libsmbclient.so.*",
        "usr/share/man/man7/libsmbclient.7",
    ]


@subpackage("samba-client-devel")
def _(self):
    self.subdesc = "client library development files"
    # transitional
    self.provides = [self.with_pkgver("libsmbclient-devel")]

    return [
        "usr/include/samba-4.0/libsmbclient.h",
        "usr/lib/libsmbclient.so",
        "usr/lib/pkgconfig/smbclient.pc",
    ]


@subpackage("samba-winbind-libs")
def _(self):
    self.subdesc = "winbind client library"
    self.depends = [self.with_pkgver("samba-libs")]
    # transitional
    self.provides = [self.with_pkgver("libwbclient")]

    return ["usr/lib/libwbclient.so.*"]


@subpackage("samba-winbind-devel")
def _(self):
    self.subdesc = "winbind library development files"
    # transitional
    self.provides = [self.with_pkgver("libwbclient-devel")]

    return [
        "usr/include/samba-4.0/wbclient.h",
        "usr/lib/libwbclient.so",
        "usr/lib/pkgconfig/samba-util.pc",
        "usr/lib/pkgconfig/wbclient.pc",
    ]


@subpackage("samba-winbind")
def _(self):
    self.pkgdesc = "Windows user and group information service"
    self.depends = [
        self.with_pkgver("samba-libs"),
        self.with_pkgver("samba-common"),
        self.with_pkgver("samba-winbind-libs"),
    ]
    return [
        "usr/bin/ntlm_auth",
        "usr/bin/wbinfo",
        "usr/bin/winbindd",
        "usr/lib/samba/idmap",
        "usr/lib/samba/krb5",
        "usr/lib/samba/nss_info",
        "usr/lib/libidmap-private-samba.so",
        "usr/lib/libnss-info-private-samba.so",
        "usr/share/man/man1/ntlm_auth.1",
        "usr/share/man/man1/wbinfo.1",
        "usr/share/man/man8/idmap_*.8",
        "usr/share/man/man8/winbind_krb5_locator.8",
        "usr/share/man/man8/winbindd.8",
    ]


@subpackage("samba-winbind-pam")
def _(self):
    self.pkgdesc = "Windows domain authentication integration plugin"
    self.depends = [self.with_pkgver("samba-winbind")]
    self.install_if = [self.with_pkgver("samba-winbind-nss")]
    # transitional
    self.provides = [self.with_pkgver("pam_winbind")]

    return [
        "usr/lib/security/pam_winbind.so",
        "usr/share/man/man5/pam_winbind.conf.5",
        "usr/share/man/man8/pam_winbind.8",
    ]


@subpackage("samba-winbind-nss")
def _(self):
    self.pkgdesc = "Samba nameservice integration plugins"
    self.depends = [self.with_pkgver("samba-winbind")]
    # transitional
    self.provides = [self.with_pkgver("libnss_winbind")]

    return ["usr/lib/libnss_win*.so.*"]


@subpackage("samba-client")
def _(self):
    self.subdesc = "client utilities"
    self.depends = [
        self.with_pkgver("samba-libs"),
        self.with_pkgver("samba-common"),
    ]

    return [
        "usr/bin/cifsdd",
        "usr/bin/mdsearch",
        "usr/bin/rpcclient",
        "usr/bin/smbcacls",
        "usr/bin/smbclient",
        "usr/bin/smbcquotas",
        "usr/bin/smbget",
        "usr/bin/smbspool",
        "usr/bin/smbtar",
        "usr/bin/smbtree",
        "usr/bin/wspsearch",
        "usr/lib/cups/backend/smb",
        "usr/lib/samba/smbspool_krb5_wrapper",
        "usr/share/man/man1/mdsearch.1",
        "usr/share/man/man1/rpcclient.1",
        "usr/share/man/man1/smbcacls.1",
        "usr/share/man/man1/smbclient.1",
        "usr/share/man/man1/smbcquotas.1",
        "usr/share/man/man1/smbget.1",
        "usr/share/man/man1/smbtar.1",
        "usr/share/man/man1/smbtree.1",
        "usr/share/man/man8/cifsdd.8",
        "usr/share/man/man8/smbspool.8",
        "usr/share/man/man8/smbspool_krb5_wrapper.8",
    ]


@subpackage("samba-vfs-modules")
def _(self):
    self.subdesc = "virtual filesystem plugins"
    self.depends = [self.with_pkgver("samba-libs")]
    self.install_if = [self.parent]

    return [
        "usr/lib/samba/vfs",
        "usr/share/man/man8/vfs_*.8",
    ]


@subpackage("samba-testsuite")
def _(self):
    self.subdesc = "test suite"
    self.depends = [
        self.with_pkgver("samba-libs"),
        self.with_pkgver("samba-common"),
        self.with_pkgver("samba-python"),
    ]

    return [
        "usr/bin/gentest",
        "usr/bin/locktest",
        "usr/bin/masktest",
        "usr/bin/ndrdump",
        "usr/bin/smbtorture",
        "usr/lib/libprinter-driver-private-samba.so",
        "usr/lib/libtorture-private-samba.so",
        "usr/share/man/man1/gentest.1",
        "usr/share/man/man1/locktest.1",
        "usr/share/man/man1/masktest.1",
        "usr/share/man/man1/ndrdump.1",
        "usr/share/man/man1/smbtorture.1",
    ]


@subpackage("samba-ctdb")
def _(self):
    self.subdesc = "clustered TDB support"
    self.depends = [
        self.with_pkgver("samba-libs"),
        "tdb-progs",
        "iproute2",
    ]

    return [
        "etc/ctdb",
        "usr/bin/ctdb*",
        "usr/bin/ltdbtool",
        "usr/bin/onnode",
        "usr/bin/ping_pong",
        "usr/lib/libctdb-event-client-private-samba.so",
        "usr/lib/libtalloc-report-private-samba.so",
        "usr/lib/ctdb",
        "usr/share/ctdb",
        "usr/share/man/man1/ctdb*.1",
        "usr/share/man/man1/ltdbtool.1",
        "usr/share/man/man1/onnode.1",
        "usr/share/man/man1/ping_pong.1",
        "usr/share/man/man5/ctdb*.5",
        "usr/share/man/man7/ctdb*.7",
    ]


@subpackage("samba-devel")
def _(self):
    return self.default_devel()


@subpackage("samba-ldb-progs")
def _(self):
    self.pkgdesc = "LDAP-like database"
    # transitional
    self.provides = [self.with_pkgver("ldb-progs")]

    return ["cmd:ldb*"]


@subpackage("samba-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends = ["python", self.with_pkgver("samba-libs")]

    return ["usr/lib/python3*"]


@subpackage("samba-libs")
def _(self):
    return ["usr/lib"]
