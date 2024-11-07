pkgname = "iwd"
pkgver = "3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    # junk cflags that redefine FORTIFY
    "--disable-optimization",
    "--disable-systemd-service",
    "--enable-dbus-policy",
    "--enable-wired",
    "--enable-pie",
]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["pkgconf", "python-docutils", "automake", "libtool"]
# TODO: look into porting to libedit later
# iwd's usage of readline is very fucky and we don't wanna break it
makedepends = ["readline-devel", "dbus-devel", "linux-headers"]
checkdepends = ["python", "dbus"]
depends = ["dinit-dbus", "resolvconf"]
pkgdesc = "Wireless daemon that replaces wpa_supplicant"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://iwd.wiki.kernel.org"
source = f"$(KERNEL_SITE)/network/wireless/iwd-{pkgver}.tar.xz"
sha256 = "a2b6d21315fdd0e060d5f75f5a0cc55018ea9d112a080f2ccd6dae2e1d923ac5"
tool_flags = {
    "CFLAGS": ["-Wno-unknown-warning-option", "-Wno-duplicate-decl-specifier"]
}
# CFI: tests fail
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_service(self.files_path / "iwd")
    self.install_service(self.files_path / "ead")
    self.install_tmpfiles(self.files_path / "iwd.conf")
