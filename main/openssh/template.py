pkgname = "openssh"
pkgver = "9.1p1"
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
sha256 = "19f85009c7e3e23787f0236fbb1578392ab4d4bf9f8ec5fe6bc1cd7e8bfdd288"
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

# FIXME visibility
hardening = ["!vis"]
