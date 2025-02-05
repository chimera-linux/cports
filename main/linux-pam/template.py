pkgname = "linux-pam"
pkgver = "1.7.0"
pkgrel = 1
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
    "meson",
    "pkgconf",
    "libxslt-progs",
]
makedepends = ["flex-devel-static", "gettext-devel", "linux-headers"]
checkdepends = ["linux-pam-base"]
depends = ["linux-pam-base"]
pkgdesc = "Pluggable Authentication Modules for Linux"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/linux-pam/linux-pam"
source = f"{url}/releases/download/v{pkgver}/Linux-PAM-{pkgver}.tar.xz"
sha256 = "57dcd7a6b966ecd5bbd95e1d11173734691e16b68692fa59661cdae9b13b1697"
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
