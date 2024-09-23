pkgname = "elogind"
pkgver = "255.5"
pkgrel = 3
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/libexec/elogind",
    "-Dman=enabled",
    "-Dpamconfdir=/usr/lib/pam.d",
    "-Dpamlibdir=/usr/lib/security",
    "-Dhalt-path=/usr/bin/halt",
    "-Dreboot-path=/usr/bin/reboot",
    "-Dcgroup-controller=elogind",
    "-Ddefault-hierarchy=unified",
    "-Ddefault-kill-user-processes=false",
    "-Dutmp=false",
    "-Dpolkit=enabled",
]
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext",
    "gperf",
    "meson",
    "pkgconf",
    "python-jinja2",
    "shadow",
    "xsltproc",
]
makedepends = [
    "acl-devel",
    "gettext-devel",
    "libcap-devel",
    "libmount-devel",
    "libseccomp-devel",
    "linux-pam-devel",
    "udev-devel",
]
checkdepends = ["bash", "python-lxml"]
depends = ["dbus", "turnstile"]
install_if = [self.with_pkgver("elogind-meta")]
pkgdesc = "Standalone version of logind"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/elogind/elogind"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "ef83beb381064516c29290f0fedcbbe36de052f313d72d120eade69ab26b82fe"
# crashes in find_suitable_hibernation_device_full -> btrfs_get_file_physical_offset_fd
# when logging into plasma from gdm
tool_flags = {"CFLAGS": ["-U_FORTIFY_SOURCE"]}


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
def _(self):
    return self.default_devel()


@subpackage("elogind-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []


@subpackage("elogind-polkit")
def _(self):
    self.subdesc = "polkit"
    self.install_if = [self.parent]
    # break cycle (polkit depends on elogind)
    self.depends = [f"virtual:polkit!{pkgname}"]
    self.options = ["empty"]

    return []


@subpackage("libelogind")
def _(self):
    self.subdesc = "library"
    return self.default_libs()


@subpackage("pam_elogind")
def _(self):
    self.subdesc = "PAM"
    self.depends = [self.parent, "linux-pam"]
    self.install_if = [self.parent, "linux-pam"]
    return [
        "usr/lib/pam.d",
        "usr/lib/security",
        "man:pam_elogind.8",
    ]
