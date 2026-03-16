pkgname = "iwd"
pkgver = "3.12"
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
makedepends = [
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "linux-headers",
    "readline-devel",
]
checkdepends = ["python", "dbus"]
depends = ["dinit-dbus", "resolvconf"]
pkgdesc = "Wireless daemon that replaces wpa_supplicant"
license = "LGPL-2.1-or-later"
url = "https://iwd.wiki.kernel.org"
source = f"$(KERNEL_SITE)/network/wireless/iwd-{pkgver}.tar.xz"
sha256 = "d89a5e45c7180170e19be828f9e944a768c593758094fc57a358d0e7c4cb1a49"
tool_flags = {
    "CFLAGS": ["-Wno-unknown-warning-option", "-Wno-duplicate-decl-specifier"]
}
# CFI: tests fail
hardening = ["vis", "!cfi"]
# check may be disabled
options = []

if self.profile().arch == "loongarch64":
    # uuid cmp fail in test-wsc
    # 3 memcmp fails in test-eap-sim
    options += ["!check"]


def post_install(self):
    self.install_service(self.files_path / "iwd")
    self.install_service(self.files_path / "ead")
    self.install_tmpfiles(self.files_path / "iwd.conf")
