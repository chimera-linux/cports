pkgname = "nux"
pkgver = "4.0.8"
pkgrel = 0
build_style = "gnu_configure"
# GLEW MX has been discontinued
configure_args = [
    "--enable-opengles-20",
    "--enable-documentation",
]
# += operator (used in the configure script) requires bash
configure_env = {"CONFIG_SHELL": "/usr/bin/bash", "NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
# .o files are built in the source tree
make_dir = "."
# graphviz not included; documentation graphics requires the FreeSans font
hostmakedepends = ["bash", "doxygen", "gnome-common", "pkgconf", "libtool"]
makedepends = [
    "boost-devel",
    "cairo-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "ibus-devel",
    "libpng-devel",
    "libsigc++2-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxinerama-devel",
    "libxxf86vm-devel",
    "mesa-devel",
    "pango-devel",
    "pciutils-devel",
    "pcre2-devel",
]
pkgdesc = "OpenGL toolkit"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "LGPL-2.1-or-later AND GPL-3.0-or-later"
url = "https://launchpad.net/nux"
source = [
    "https://gitlab.com/ubuntu-unity/unity-x/nux/-/archive/main/nux-main.tar.gz",
    "https://launchpad.net/nux/4.0/4.0.8/+download/nux-4.0.8.tar.gz",
]
source_paths = [".", "original-nux"]
sha256 = [
    "02a201fe8ddc8ebca55e742a18e373a276cb399d16fad50abb1466586b308f15",
    "3534ad4becd064f62e7393ef5b8f9bbb71bd1cd4830f859aea341b6f15877077",
]
hardening = ["vis", "cfi"]
# Tests require gmock-all.cc
options = ["!check", "keeplibtool"]


def post_extract(self):
    # Copy the necessary M4 macros
    self.cp("original-nux/m4", ".", recursive=True)


def post_install(self):
    self.uninstall("usr/share/nux/gputests")
