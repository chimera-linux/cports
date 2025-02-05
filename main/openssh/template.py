pkgname = "openssh"
pkgver = "9.9_p1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--datadir=/usr/share/openssh",
    "--sysconfdir=/etc/ssh",
    "--disable-wtmp",
    "--disable-utmp",
    "--without-selinux",
    "--without-rpath",
    "--without-zlib-version-check",
    "--with-mantype=doc",
    "--with-pam",
    "--with-libedit",
    "--with-kerberos5",
    "--with-pid-dir=/run",
    "--with-privsep-user=nobody",
    "--with-privsep-path=/var/chroot/ssh",
    "--with-xauth=/usr/bin/xauth",
    "--with-security-key-builtin",
    "--with-ssl-engine",
    "--disable-strip",
    "ac_cv_header_sys_cdefs_h=false",
]
make_check_target = "tests"
make_check_args = ["-j1"]
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "heimdal-devel",
    "libedit-devel",
    "libfido2-devel",
    "libldns-devel",
    "linux-pam-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "OpenSSH free Secure Shell (SSH) client and server implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "SSH-OpenSSH"
url = "https://www.openssh.com"
source = f"https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-{pkgver.replace('_', '')}.tar.gz"
sha256 = "b343fbcdbff87f15b1986e6e15d6d4fc9a7d36066be6b7fb507087ba8f966c02"
file_modes = {"usr/libexec/ssh-keysign": ("root", "root", 0o4755)}
# CFI: does not work; maybe make testsuite work first
hardening = ["vis", "!cfi"]
# portable openssh is not very portable
options = ["!check"]


def init_configure(self):
    self.configure_args += [
        "--with-ldns=" + str(self.profile().sysroot / "usr")
    ]


def post_install(self):
    self.install_license("LICENCE")

    self.install_file(
        self.files_path / "sshd.pam", "usr/lib/pam.d", name="sshd"
    )

    self.install_bin("contrib/ssh-copy-id")
    self.install_man("contrib/ssh-copy-id.1")

    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    self.install_service(self.files_path / "ssh-keygen")
    self.install_service(self.files_path / "sshd")
