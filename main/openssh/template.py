pkgname = "openssh"
pkgver = "9.0p1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--datadir=/usr/share/openssh",
    "--sysconfdir=/etc/ssh",
    "--disable-wtmp",
    "--disable-utmp",
    "--without-selinux",
    "--without-rpath",
    "--with-mantype=doc",
    "--with-pam",
    "--with-libedit",
    "--with-pid-dir=/run",
    "--with-privsep-user=nobody",
    "--with-privsep-path=/var/chroot/ssh",
    "--with-xauth=/usr/bin/xauth",
    "--with-ssl-engine",
    "--disable-strip",
    "ac_cv_header_sys_cdefs_h=false"
]
make_check_target = "tests"
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "libedit-devel", "linux-pam-devel", "zlib-devel", "libldns-devel",
    "openssl-devel"
]
pkgdesc = "OpenSSH free Secure Shell (SSH) client and server implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND ISC"
url = "https://www.openssh.com"
source = f"https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/{pkgname}-{pkgver}.tar.gz"
sha256 = "03974302161e9ecce32153cfa10012f1e65c8f3750f573a73ab1befd5972a28a"
suid_files = ["usr/libexec/ssh-keysign"]
# portable openssh is not very portable
options = ["!check"]

def init_configure(self):
    self.configure_args += [
        "--with-ldns=" + str(self.profile().sysroot / "usr")
    ]

def post_install(self):
    self.install_license("LICENCE")

    self.install_file(self.files_path / "sshd.pam", "etc/pam.d", name = "sshd")

    self.install_bin("contrib/ssh-copy-id")
    self.install_man("contrib/ssh-copy-id.1")

    self.install_dir("var/chroot/ssh", empty = True)

    self.install_service(self.files_path / "ssh-keygen")
    self.install_service(self.files_path / "sshd")
