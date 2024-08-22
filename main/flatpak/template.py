pkgname = "flatpak"
pkgver = "1.14.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-system-bubblewrap",
    "--with-system-dbus-proxy",
    "--with-system-helper-user=_flatpak",
    "--enable-selinux-module=no",
    "--enable-gdm-env-file",
    "--disable-static",
    "--disable-documentation",
    "--with-curl",
    "--with-priv-mode=none",
    "--with-dbus-config-dir=/usr/share/dbus-1/system.d",
]
hostmakedepends = [
    "automake",
    "bison",
    "bubblewrap",
    "docbook-xml",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "libxml2-progs",
    "pkgconf",
    "python-pyparsing",
    "xdg-dbus-proxy",
    "xmlto",
    "xsltproc",
]
makedepends = [
    "appstream-devel",
    "appstream-glib-devel",
    "fuse-devel",
    "gcab-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gpgme-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libcap-devel",
    "libcurl-devel",
    "libseccomp-devel",
    "libxau-devel",
    "libxml2-devel",
    "ostree-devel",
    "polkit-devel",
    "zstd-devel",
]
checkdepends = ["bash", "dbus", "socat"]
depends = [
    "bubblewrap",
    "desktop-file-utils",
    "gtk-update-icon-cache",
    "kmod",
    "shared-mime-info",
    "xdg-dbus-proxy",
]
# invoke the trigger on self
triggers = ["/usr/share/flatpak"]
pkgdesc = "Linux application sandboxing and distribution framework"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://flatpak.org"
source = f"https://github.com/flatpak/flatpak/releases/download/{pkgver}/flatpak-{pkgver}.tar.xz"
sha256 = "6bbdc7908127350ad85a4a47d70292ca2f4c46e977b32b1fd231c2a719d821cd"
# test runner expects a different env (possible FIXME?)
options = ["!check", "!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.uninstall("usr/lib/tmpfiles.d/flatpak.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(
        self.files_path / "modules-load.conf",
        "usr/lib/modules-load.d",
        name="flatpak.conf",
    )


@subpackage("flatpak-devel")
def _(self):
    return self.default_devel()
