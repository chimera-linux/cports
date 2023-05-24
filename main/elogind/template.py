pkgname = "elogind"
pkgver = "246.10"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dman=true",
    "-Drootlibexecdir=/usr/libexec/elogind",
    "-Dhalt-path=/usr/bin/halt",
    "-Dreboot-path=/usr/bin/reboot",
    "-Dcgroup-controller=elogind",
    "-Ddefault-hierarchy=unified",
    "-Ddefault-kill-user-processes=false",
    "-Dutmp=false",
    "-Dpolkit=true",
]
hostmakedepends = [
    "meson",
    "docbook-xsl-nons",
    "gettext-tiny",
    "gperf",
    "xsltproc",
    "pkgconf",
    "shadow",
]
makedepends = [
    "acl-devel",
    "udev-devel",
    "gettext-tiny-devel",
    "libcap-devel",
    "libseccomp-devel",
    "linux-pam-devel",
]
checkdepends = ["bash"]
depends = ["dbus", "turnstile"]
install_if = [f"elogind-meta={pkgver}-r{pkgrel}"]
pkgdesc = "Standalone version of logind"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/elogind/elogind"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "c490dc158c8f5bca8d00ecfcc7ad5af24d1c7b9e59990a0b3b1323996221a922"


def post_install(self):
    # compat symlinks
    self.install_link("libelogind.pc", "usr/lib/pkgconfig/libsystemd.pc")
    self.install_link("libelogind.pc", "usr/lib/pkgconfig/libsystemd-logind.pc")
    self.install_link("elogind", "usr/include/systemd")
    # extra includes
    self.install_file("src/systemd/sd-id128.h", "usr/include")
    self.install_file("src/systemd/_sd-common.h", "usr/include")
    # service file
    self.install_file(
        self.files_path / "elogind.wrapper", "usr/libexec/elogind", mode=0o755
    )
    self.install_service(self.files_path / "elogind", enable=True)


@subpackage("elogind-devel")
def _devel(self):
    return self.default_devel()


@subpackage("elogind-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.build_style = "meta"
    return []


@subpackage("elogind-polkit")
def _polkit(self):
    self.pkgdesc = f"{pkgdesc} (polkit)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    # break cycle (polkit depends on elogind)
    self.depends = [f"virtual:polkit!{pkgname}"]
    self.build_style = "meta"

    return []


@subpackage("libelogind")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (library)"
    return self.default_libs()


@subpackage("pam_elogind")
def _pam(self):
    self.pkgdesc = f"{pkgdesc} (PAM)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "linux-pam"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "linux-pam"]
    return [
        "etc/pam.d",
        "usr/lib/security",
        "usr/share/factory",
        "usr/share/man/man8/pam_elogind.8",
    ]
