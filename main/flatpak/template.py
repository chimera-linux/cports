pkgname = "flatpak"
pkgver = "1.14.8"
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
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "bison",
    "bubblewrap",
    "docbook-xml",
    "gettext-devel",
    "gmake",
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
sha256 = "1016b7327f7af87896f95465f7e5813750d3b7049a3740a1a4ddcb5fa8c5348e"
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
def _devel(self):
    return self.default_devel()
