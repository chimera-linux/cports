pkgname = "linux-pam"
pkgver = "1.5.3"
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
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext-tiny"]
makedepends = ["gettext-tiny-devel", "libfl-devel-static", "linux-headers"]
checkdepends = ["linux-pam-base"]
depends = ["linux-pam-base"]
pkgdesc = "Pluggable Authentication Modules for Linux"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = f"https://github.com/{pkgname}/{pkgname}"
source = f"{url}/releases/download/v{pkgver}/Linux-PAM-{pkgver}.tar.xz"
sha256 = "7ac4b50feee004a9fa88f1dfd2d2fa738a82896763050cd773b3c54b0a818283"
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
