pkgname = "elogind"
pkgver = "255.5"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/libexec/elogind",
    "-Dman=true",
    "-Dpamconfdir=/usr/lib/pam.d",
    "-Dpamlibdir=/usr/lib/security",
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
checkdepends = ["bash", "python-lxml"]
depends = ["dbus", "turnstile"]
install_if = [f"elogind-meta={pkgver}-r{pkgrel}"]
pkgdesc = "Standalone version of logind"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/elogind/elogind"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "ef83beb381064516c29290f0fedcbbe36de052f313d72d120eade69ab26b82fe"


def post_install(self):
    # compat symlinks
    self.install_link("usr/lib/pkgconfig/libsystemd.pc", "libelogind.pc")
    self.install_link("usr/lib/pkgconfig/libsystemd-logind.pc", "libelogind.pc")
    self.install_link("usr/include/systemd", "elogind")
    # extra includes
    self.install_file("src/systemd/sd-id128.h", "usr/include")
    self.install_file("src/systemd/_sd-common.h", "usr/include")
    # service file
    self.install_tmpfiles(self.files_path / "elogind.conf")
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
        "usr/lib/pam.d",
        "usr/lib/security",
        "usr/share/man/man8/pam_elogind.8",
    ]
