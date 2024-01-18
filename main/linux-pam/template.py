pkgname = "linux-pam"
pkgver = "1.6.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--docdir=/usr/share/doc/pam",
    "--disable-nis",
    "--disable-audit",
    "--disable-selinux",
    "--disable-regenerate-docu",
    "--disable-db",
    "BUILD_CFLAGS=-Os",
    "BUILD_LDFLAGS=",
    "ac_cv_search_crypt=no",
]
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext"]
makedepends = ["gettext-devel", "libfl-devel-static", "linux-headers"]
checkdepends = ["linux-pam-base"]
depends = ["linux-pam-base"]
pkgdesc = "Pluggable Authentication Modules for Linux"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/linux-pam/linux-pam"
source = f"{url}/releases/download/v{pkgver}/Linux-PAM-{pkgver}.tar.xz"
sha256 = "fff4a34e5bbee77e2e8f1992f27631e2329bcbf8a0563ddeb5c3389b4e3169ad"
suid_files = ["usr/bin/unix_chkpwd"]


def post_install(self):
    self.install_license("COPYING")

    self.chmod(self.destdir / "usr/bin/unix_chkpwd", 0o4755)
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)

    for f in ["limits.d", "namespace.d"]:
        self.install_dir(f"etc/security/{f}", empty=True)


@subpackage("linux-pam-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])


@subpackage("linux-pam-libs")
def _libs(self):
    return self.default_libs()
