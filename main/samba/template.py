# TODO: service files, cleanup
pkgname = "samba"
pkgver = "4.19.6"
pkgrel = 1
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
    "--without-ads",  # needs ldap
    "--without-ldap",  # don't depend on shit software
    "--without-ad-dc",
]
hostmakedepends = [
    "pkgconf",
    "python",
    "perl",
    "perl-parse-yapp",
    "gettext-devel",
    "libtasn1-progs",
    "docbook-xsl-nons",
    "xsltproc",
    "rpcsvc-proto",
    "flex",
    "bison",
    "tdb-python",
    "tevent-python",
    "ldb-python",
    "heimdal",
]
makedepends = [
    "gettext-devel",
    "python-devel",
    "libtirpc-devel",
    "popt-devel",
    "e2fsprogs-devel",
    "zlib-devel",
    "ncurses-devel",
    "libarchive-devel",
    "musl-bsd-headers",
    "linux-pam-devel",
    "heimdal-devel",
    "acl-devel",
    "attr-devel",
    "cups-devel",
    "jansson-devel",
    "avahi-devel",
    "fuse-devel",
    "dbus-devel",
    "tdb-devel",
    "talloc-devel",
    "ldb-devel",
    "tevent-devel",
    "gnutls-devel",
    "cmocka-devel",
    "icu-devel",
    "musl-nscd",
    "glib-devel",
    "gpgme-devel",
    "libedit-readline-devel",
]
self.depends = [
    f"samba-libs={pkgver}-r{pkgrel}",
    f"samba-common={pkgver}-r{pkgrel}",
    "tdb-progs",
]
pkgdesc = "SMB/CIFS file, print, and login server for Unix"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.samba.org"
source = (
    f"https://download.samba.org/pub/samba/stable/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "653b52095554dbc223c63b96af5cdf9e98c3e048549c5f56143d3b33dce1cef1"
env = {"PYTHONHASHSEED": "1"}
# check needs --enable-selftest, which needs extra system dependencies
options = ["!cross", "!check", "!installroot", "linkundefver"]

# idmap_ad should go here if active directory is enabled
configure_args.append(
    "--with-shared-modules="
    + ",".join(
        [
            "idmap_rid",
            "idmap_adex",
            "idmap_hash",
            "idmap_ldap",
            "idmap_tdb2",
            "vfs_nfs4acl_xattr",
        ]
    )
)

tool_flags = {"CFLAGS": ["-D_BSD_SOURCE"], "LDFLAGS": []}


def post_install(self):
    self.install_file("examples/smb.conf.default", "etc/samba", name="smb.conf")
    self.install_file(self.files_path / "samba.pam", "etc/pam.d", name="samba")
    self.rm(self.destdir / "etc/sudoers.d", recursive=True)
    self.rm(self.destdir / "usr/share/man/man7/traffic_learner.7")
    self.rm(self.destdir / "usr/share/man/man7/traffic_replay.7")
    # symlink cups backend
    self.install_dir("usr/lib/cups/backend")
    self.install_link("usr/lib/cups/backend/smb", "../../../bin/smbspool")
    # private dir
    self.install_dir("var/lib/samba/private", mode=0o750, empty=True)


@subpackage("samba-common")
def _common(self):
    self.pkgdesc = f"{pkgdesc} (common files and programs)"
    self.depends = [f"samba-libs={pkgver}-r{pkgrel}"]

    return [
        "etc/pam.d",
        "usr/bin/dbwrap_tool",
        "usr/bin/net",
        "usr/bin/nmblookup",
        "usr/bin/samba-regedit",
        # "usr/bin/samba-tool", not present without AD
        "usr/bin/smbpasswd",
        "usr/bin/testparm",
        "usr/libexec/samba/rpcd_*",
        "usr/libexec/samba/samba-dcerpcd",
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
def _registry(self):
    self.pkgdesc = "Tools for viewing and manipulating the Windows registry"
    self.depends = [f"samba-libs={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/reg*",
        "usr/share/man/man1/reg*.1",
    ]


@subpackage("libsmbclient")
def _clib(self):
    self.pkgdesc = f"{pkgdesc} (client library)"
    self.depends = [f"samba-libs={pkgver}-r{pkgrel}"]

    return [
        "usr/lib/libsmbclient.so.*",
        "usr/share/man/man7/libsmbclient.7",
    ]


@subpackage("libsmbclient-devel")
def _clib_dev(self):
    self.pkgdesc = f"{pkgdesc} (client library development files)"

    return [
        "usr/include/samba-4.0/libsmbclient.h",
        "usr/lib/libsmbclient.so",
        "usr/lib/pkgconfig/smbclient.pc",
    ]


@subpackage("libwbclient")
def _wlib(self):
    self.pkgdesc = f"{pkgdesc} (winbind client library)"
    self.depends = [f"samba-libs={pkgver}-r{pkgrel}"]

    return ["usr/lib/libwbclient.so.*"]


@subpackage("libwbclient-devel")
def _wlib_dev(self):
    self.pkgdesc = f"{pkgdesc} (winbind library development files)"

    return [
        "usr/include/samba-4.0/wbclient.h",
        "usr/lib/libwbclient.so",
        "usr/lib/pkgconfig/samba-util.pc",
        "usr/lib/pkgconfig/wbclient.pc",
    ]


@subpackage("samba-winbind")
def _winbind(self):
    self.pkgdesc = "Windows user and group information service"
    self.depends = [
        f"samba-libs={pkgver}-r{pkgrel}",
        f"samba-common={pkgver}-r{pkgrel}",
        f"libwbclient={pkgver}-r{pkgrel}",
    ]
    return [
        "usr/bin/ntlm_auth",
        "usr/bin/wbinfo",
        "usr/bin/winbindd",
        "usr/lib/samba/idmap",
        "usr/lib/samba/krb5",
        "usr/lib/samba/nss_info",
        "usr/lib/libidmap-samba4.so",
        "usr/lib/libnss-info-samba4.so",
        "usr/share/man/man1/ntlm_auth.1",
        "usr/share/man/man1/wbinfo.1",
        "usr/share/man/man8/idmap_*.8",
        "usr/share/man/man8/winbind_krb5_locator.8",
        "usr/share/man/man8/winbindd.8",
    ]


@subpackage("pam_winbind")
def _pam_winbind(self):
    self.pkgdesc = "Windows domain authentication integration plugin"
    self.depends = [f"samba-winbind={pkgver}-r{pkgrel}"]
    self.install_if = [f"libnss_winbind={pkgver}-r{pkgrel}"]

    return [
        "usr/lib/security/pam_winbind.so",
        "usr/share/man/man5/pam_winbind.conf.5",
        "usr/share/man/man8/pam_winbind.8",
    ]


@subpackage("libnss_winbind")
def _nss_winbind(self):
    self.pkgdesc = "Samba nameservice integration plugins"
    self.depends = [f"samba-winbind={pkgver}-r{pkgrel}"]

    return ["usr/lib/libnss_win*.so.*"]


@subpackage("samba-client")
def _smbclient(self):
    self.pkgdesc = f"{pkgdesc} (client utilities)"
    self.depends = [
        f"samba-libs={pkgver}-r{pkgrel}",
        f"samba-common={pkgver}-r{pkgrel}",
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
        "usr/lib/cups/backend/smb",
        "usr/libexec/samba/smbspool_krb5_wrapper",
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
def _vfs(self):
    self.pkgdesc = f"{pkgdesc} (virtual filesystem plugins)"
    self.depends = [f"samba-libs={pkgver}-r{pkgrel}"]
    self.install_if = [f"samba={pkgver}-r{pkgrel}"]

    return [
        "usr/lib/samba/vfs",
        "usr/share/man/man8/vfs_*.8",
    ]


@subpackage("samba-testsuite")
def _test(self):
    self.pkgdesc = f"{pkgdesc} (test suite)"
    self.depends = [
        f"samba-libs={pkgver}-r{pkgrel}",
        f"samba-common={pkgver}-r{pkgrel}",
        f"samba-python={pkgver}-r{pkgrel}",
    ]

    return [
        "usr/bin/gentest",
        "usr/bin/locktest",
        "usr/bin/masktest",
        "usr/bin/ndrdump",
        "usr/bin/smbtorture",
        "usr/lib/libprinter-driver-samba4.so",
        "usr/lib/libtorture-samba4.so",
        "usr/share/man/man1/gentest.1",
        "usr/share/man/man1/locktest.1",
        "usr/share/man/man1/masktest.1",
        "usr/share/man/man1/ndrdump.1",
        "usr/share/man/man1/smbtorture.1",
    ]


@subpackage("samba-ctdb")
def _ctdb(self):
    self.pkgdesc = f"{pkgdesc} (clustered TDB support)"
    self.depends = [
        f"samba-libs={pkgver}-r{pkgrel}",
        "tdb-progs",
        "iproute2",
    ]

    return [
        "etc/ctdb",
        "usr/bin/ctdb*",
        "usr/bin/ltdbtool",
        "usr/bin/onnode",
        "usr/bin/ping_pong",
        "usr/lib/libctdb-event-client-samba4.so",
        "usr/lib/libtalloc-report-samba4.so",
        "usr/libexec/ctdb",
        "usr/share/ctdb",
        "usr/share/man/man1/ctdb*.1",
        "usr/share/man/man1/ltdbtool.1",
        "usr/share/man/man1/onnode.1",
        "usr/share/man/man1/ping_pong.1",
        "usr/share/man/man5/ctdb*.5",
        "usr/share/man/man7/ctdb*.7",
    ]


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
    self.depends = [f"samba-libs={pkgver}-r{pkgrel}"]

    return ["usr/lib/python3*"]


@subpackage("samba-libs")
def _libs(self):
    return ["usr/lib"]
