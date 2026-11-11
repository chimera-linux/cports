pkgname = "lightdm"
pkgver = "1.33.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-liblightdm-qt5",
    "--disable-liblightdm-qt6",
    "--disable-libaudit",
    "--disable-tests",
    "--with-greeter-user=_lightdm",
]
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "intltool",
    "itstool",
    "libtool",
    "libxml2-progs",
    "pkgconf",
    "vala",
    "yelp-tools",
]
makedepends = [
    "dinit-chimera",
    "dinit-dbus",
    "elogind",
    "glib-devel",
    "libgcrypt-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxdmcp-devel",
    "libxklavier-devel",
    "linux-headers",
    "linux-pam-devel",
    "openrc-settingsd",
]
depends = [
    "dinit-dbus",
    "elogind",
    "openrc-settingsd",
    "turnstile",
    "xrdb",
    "xserver-xorg-minimal",
]
pkgdesc = "Lightweight cross-desktop display manager"
license = "GPL-3.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/canonical/lightdm"
source = f"{url}/releases/download/{pkgver}/lightdm-{pkgver}.tar.xz"
sha256 = "1a3ca2fea2c97065d85d989048a30fc4148fd0eaf94cffd683f0b3f389fe1ed0"
# tests need write access to the root
options = ["etcfiles", "!check", "!cross"]


def post_install(self):
    self.install_bin(self.files_path / "lightdm-session")
    self.install_service(self.files_path / "lightdm")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.uninstall("etc/pam.d")
    for pam in ["lightdm", "lightdm-autologin", "lightdm-greeter"]:
        self.install_file(
            self.files_path / f"{pam}.pam", "usr/lib/pam.d", name=pam
        )
    # upstart job and apparmor profiles
    self.uninstall("etc/init")
    self.uninstall("etc/apparmor.d")


@subpackage("lightdm-devel")
def _(self):
    return self.default_devel()


@subpackage("lightdm-libs")
def _(self):
    return self.default_libs()
