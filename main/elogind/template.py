pkgname = "elogind"
pkgver = "252.9"
pkgrel = 4
build_style = "meson"
configure_args = [
    "-Dman=true",
    "-Dpamconfdir=/etc/pam.d",
    "-Dpamlibdir=/usr/lib/security",
    "-Drootlibdir=/usr/lib",
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
    "gettext",
    "gperf",
    "xsltproc",
    "pkgconf",
    "shadow",
    "python-jinja2",
]
makedepends = [
    "acl-devel",
    "udev-devel",
    "gettext-devel",
    "libcap-devel",
    "libseccomp-devel",
    "linux-pam-devel",
    "libmount-devel",
]
checkdepends = ["bash"]
depends = ["turnstile"]
install_if = [f"elogind-meta={pkgver}-r{pkgrel}"]
pkgdesc = "Standalone version of logind"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/elogind/elogind"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "7af8caa8225a406e77fb99c9f33dba5e1f0a94f0e1277c9d91dcfc016f116d85"


def post_install(self):
    # compat symlinks
    self.install_link("libelogind.pc", "usr/lib/pkgconfig/libsystemd.pc")
    self.install_link("libelogind.pc", "usr/lib/pkgconfig/libsystemd-logind.pc")
    self.install_link("elogind", "usr/include/systemd")
    # extra includes
    self.install_file("src/systemd/sd-id128.h", "usr/include")
    self.install_file("src/systemd/_sd-common.h", "usr/include")
    # service file
    self.install_file(self.files_path / "elogind.conf", "usr/lib/tmpfiles.d")
    self.install_service(self.files_path / "elogind", enable=True)


@subpackage("elogind-devel")
def _devel(self):
    return self.default_devel()


@subpackage("elogind-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.options = ["empty"]
    return []


@subpackage("elogind-polkit")
def _polkit(self):
    self.pkgdesc = f"{pkgdesc} (polkit)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    # break cycle (polkit depends on elogind)
    self.depends = [f"virtual:polkit!{pkgname}"]
    self.options = ["empty"]

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
        "usr/share/man/man8/pam_elogind.8",
    ]
