# TODO: service files, cleanup
pkgname = "samba"
pkgver = "4.21.0"
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
    "--bundled-libraries=NONE",
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
    "perl",
    "perl-parse-yapp",
    "pkgconf",
    "python",
    "rpcsvc-proto",
    "tdb-python",
    "tevent-python",
    "xsltproc",
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
    "musl-bsd-headers",
    "musl-nscd",
    "ncurses-devel",
    "openldap-devel",
    "popt-devel",
    "python-devel",
    "talloc-devel",
    "tdb-devel",
    "tevent-devel",
    "zlib-ng-compat-devel",
]
self.depends = [
    self.with_pkgver("samba-common"),
    self.with_pkgver("samba-libs"),
    "tdb-progs",
]
pkgdesc = "SMB/CIFS file, print, and login server for Unix"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.samba.org"
source = f"https://download.samba.org/pub/samba/stable/samba-{pkgver}.tar.gz"
sha256 = "09bb56db4ce003cafdbebe9bad368c4f4ff1945f732d18077d52f36ab20cef88"
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
    self.install_dir("var/lib/samba/private", mode=0o750, empty=True)


@subpackage("samba-common")
def _(self):
    self.subdesc = "common files and programs"
    self.depends = [self.with_pkgver("samba-libs")]

    return [
        "usr/lib/pam.d",
        "cmd:dbwrap_tool",
        "cmd:net",
        "cmd:nmblookup",
        "cmd:samba-regedit",
        "cmd:samba-tool",
        "cmd:smbpasswd",
        "cmd:testparm",
        "usr/libexec/samba/rpcd_*",
        "usr/libexec/samba/samba-dcerpcd",
        "man:lmhosts.5",
        "man:smb.conf.5",
        "man:smbpasswd.5",
        "man:samba.7",
        "man:samba-dcerpcd.8",
    ]


@subpackage("samba-registry-progs")
def _(self):
    self.pkgdesc = "Tools for viewing and manipulating the Windows registry"
    self.depends = [self.with_pkgver("samba-libs")]

    return ["cmd:reg*"]


@subpackage("libsmbclient")
def _(self):
    self.subdesc = "client library"
    self.depends = [self.with_pkgver("samba-libs")]

    return [
        "usr/lib/libsmbclient.so.*",
        "man:libsmbclient.7",
    ]


@subpackage("libsmbclient-devel")
def _(self):
    self.subdesc = "client library development files"

    return [
        "usr/include/samba-4.0/libsmbclient.h",
        "usr/lib/libsmbclient.so",
        "usr/lib/pkgconfig/smbclient.pc",
    ]


@subpackage("libwbclient")
def _(self):
    self.subdesc = "winbind client library"
    self.depends = [self.with_pkgver("samba-libs")]

    return ["usr/lib/libwbclient.so.*"]


@subpackage("libwbclient-devel")
def _(self):
    self.subdesc = "winbind library development files"

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
        self.with_pkgver("libwbclient"),
    ]
    return [
        "cmd:ntlm_auth",
        "cmd:wbinfo",
        "cmd:winbindd",
        "usr/lib/samba/idmap",
        "usr/lib/samba/krb5",
        "usr/lib/samba/nss_info",
        "usr/lib/libidmap-private-samba.so",
        "usr/lib/libnss-info-private-samba.so",
        "man:idmap_*.8",
        "man:winbind_krb5_locator.8",
    ]


@subpackage("pam_winbind")
def _(self):
    self.pkgdesc = "Windows domain authentication integration plugin"
    self.depends = [self.with_pkgver("samba-winbind")]
    self.install_if = [self.with_pkgver("libnss_winbind")]

    return [
        "usr/lib/security/pam_winbind.so",
        "man:bind.conf.5",
        "man:pam_winbind.8",
    ]


@subpackage("libnss_winbind")
def _(self):
    self.pkgdesc = "Samba nameservice integration plugins"
    self.depends = [self.with_pkgver("samba-winbind")]

    return ["usr/lib/libnss_win*.so.*"]


@subpackage("samba-client")
def _(self):
    self.subdesc = "client utilities"
    self.depends = [
        self.with_pkgver("samba-libs"),
        self.with_pkgver("samba-common"),
    ]

    return [
        "cmd:cifsdd",
        "cmd:mdsearch",
        "cmd:rpcclient",
        "cmd:smbcacls",
        "cmd:smbclient",
        "cmd:smbcquotas",
        "cmd:smbget",
        "cmd:smbspool",
        "cmd:smbtar",
        "cmd:smbtree",
        "cmd:wspsearch",
        "usr/lib/cups/backend/smb",
        "usr/libexec/samba/smbspool_krb5_wrapper",
        "man:smbspool_krb5_wrapper.8",
    ]


@subpackage("samba-vfs-modules")
def _(self):
    self.subdesc = "virtual filesystem plugins"
    self.depends = [self.with_pkgver("samba-libs")]
    self.install_if = [self.parent]

    return [
        "usr/lib/samba/vfs",
        "man:vfs_*.8",
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
        "cmd:gentest",
        "cmd:locktest",
        "cmd:masktest",
        "cmd:ndrdump",
        "cmd:smbtorture",
        "usr/lib/libprinter-driver-private-samba.so",
        "usr/lib/libtorture-private-samba.so",
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
        "cmd:ctdb*",
        "cmd:ltdbtool",
        "cmd:onnode",
        "cmd:ping_pong",
        "usr/lib/libctdb-event-client-private-samba.so",
        "usr/lib/libtalloc-report-private-samba.so",
        "usr/libexec/ctdb",
        "usr/share/ctdb",
        "man:ctdb*.5",
        "man:ctdb*.7",
    ]


@subpackage("samba-devel")
def _(self):
    return self.default_devel()


@subpackage("ldb-progs")
def _(self):
    self.pkgdesc = "LDAP-like database"
    self.subdesc = "programs"
    return ["cmd:ldb*"]


@subpackage("samba-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends = ["python", self.with_pkgver("samba-libs")]

    return ["usr/lib/python3*"]


@subpackage("samba-libs")
def _(self):
    return ["usr/lib"]
