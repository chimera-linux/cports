pkgname = "lightdm"
pkgver = "1.32.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX: drop libexec
    "--enable-gtk-doc",
    "--disable-tests",
]
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
make_install_args = ["pamdir=/usr/lib/pam.d"]
hostmakedepends = [
    "automake",
    "gettext-devel",
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
    "audit-devel",
    "glib-devel",
    "libgcrypt-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxdmcp-devel",
    "libxklavier-devel",
    "linux-pam-devel",
]
depends = ["setxkbmap", "xinit", "xmodmap", "xrdb"]
pkgdesc = "Lightweight, cross-desktop display manager"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/canonical/lightdm"
source = f"{url}/releases/download/{pkgver}/lightdm-{pkgver}.tar.xz"
sha256 = "12f5ab432748f0387c7cf8b94430495a558a035a4f8465e5181af6faff133e4b"
# Test suite requires write access to the cbuild container's root
options = ["!check", "!cross"]


def post_install(self):
    # Required for slick-greeter to work
    self.install_bin("^/lightdm-session")

    # Uninstall Upstart-related directory
    self.uninstall("etc/init")

    self.install_service("^/lightdm")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")


@subpackage("lightdm-devel")
def _(self):
    return self.default_devel()


@subpackage("lightdm-libs")
def _(self):
    return self.default_libs()
