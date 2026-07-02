pkgname = "linux-pam"
pkgver = "1.7.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocdir=/usr/share/doc/pam",
    "-Dnis=disabled",
    "-Daudit=disabled",
    "-Dselinux=disabled",
    "-Dvendordir=/usr/share/pam",
]
hostmakedepends = [
    "docbook-xsl",
    "gettext-devel",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = ["flex-devel-static", "gettext-devel", "linux-headers"]
checkdepends = ["linux-pam-base"]
depends = ["linux-pam-base"]
pkgdesc = "Pluggable Authentication Modules for Linux"
license = "BSD-3-Clause"
url = "https://github.com/linux-pam/linux-pam"
source = f"{url}/releases/download/v{pkgver}/Linux-PAM-{pkgver}.tar.xz"
sha256 = "3d86b6383fb5fd9eb9578d2cd47d92801191f4bf3f9bc61419bfefc8aa1e531a"
file_modes = {
    "usr/bin/unix_chkpwd": ("root", "root", 0o4755),
    # other stuff in there is owned by the package so...
    "+usr/share/pam/security/limits.d": ("root", "root", 0o755),
    "+usr/share/pam/security/namespace.d": ("root", "root", 0o755),
}
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")

    self.chmod(self.destdir / "usr/bin/unix_chkpwd", 0o4755)
    self.uninstall("usr/lib/systemd")


@subpackage("linux-pam-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc"])


@subpackage("linux-pam-libs")
def _(self):
    return self.default_libs()
