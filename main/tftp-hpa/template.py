pkgname = "tftp-hpa"
pkgver = "5.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--without-tcpwrappers",
]
make_dir = "."
hostmakedepends = ["automake"]
makedepends = ["dinit-chimera", "libedit-readline-devel"]
pkgdesc = "TFTP client and server"
license = "BSD-3-Clause"
url = "https://www.kernel.org"
source = f"{url}/pub/software/network/tftp/tftp-hpa/tftp-hpa-{pkgver}.tar.gz"
sha256 = "acc04dde662491e3092565ecf9bde504c47dbb1bb0408366009b138fe7754cab"
tool_flags = {"CFLAGS": ["-fcommon"]}
# no license file, no tests
options = ["!distlicense", "!check"]


def init_install(self):
    self.make_install_args += [f"INSTALLROOT={self.chroot_destdir}"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "tftpd-hpa")
