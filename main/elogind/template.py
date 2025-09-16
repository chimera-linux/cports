pkgname = "elogind"
pkgver = "255.17"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib/elogind",
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
    "libxslt-progs",
    "meson",
    "pkgconf",
    "python-jinja2",
    "shadow",
]
makedepends = [
    "acl-devel",
    "gettext-devel",
    "libcap-devel",
    "libseccomp-devel",
    "linux-pam-devel",
    "udev-devel",
    "util-linux-mount-devel",
]
checkdepends = ["bash", "python-lxml"]
depends = ["dinit-dbus", "tangle-progs", "turnstile"]
install_if = [self.with_pkgver("elogind-meta")]
pkgdesc = "Standalone version of logind"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/elogind/elogind"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a9725ae3f73f8d910de84c108bc11bfd4c782bef6a4190b2ec70c5d2f22344db"
# crashes in find_suitable_hibernation_device_full -> btrfs_get_file_physical_offset_fd
# when logging into plasma from gdm
tool_flags = {"CFLAGS": ["-U_FORTIFY_SOURCE"]}
# skip cycle with polkit... providers are ok of course
skip_dependencies = ["usr/lib/dinit.d/*"]


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
    # busctl provided by tangle
    self.uninstall("usr/bin/busctl")
    self.uninstall("usr/share/man/man1/busctl.1")
    self.uninstall("usr/share/bash-completion/completions/busctl")
    self.uninstall("usr/share/zsh/site-functions/_busctl")


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


@subpackage("elogind-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libelogind")]

    return self.default_libs()


@subpackage("elogind-pam")
def _(self):
    self.subdesc = "PAM"
    self.depends = [self.parent, "linux-pam"]
    self.install_if = [self.parent, "linux-pam"]
    # transitional
    self.provides = [self.with_pkgver("pam_elogind")]

    return [
        "usr/lib/pam.d",
        "usr/lib/security",
        "usr/share/man/man8/pam_elogind.8",
    ]
