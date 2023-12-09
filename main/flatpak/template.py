pkgname = "flatpak"
pkgver = "1.14.5"
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
    "gmake",
    "pkgconf",
    "automake",
    "libtool",
    "xsltproc",
    "docbook-xml",
    "libxml2-progs",
    "bison",
    "python-pyparsing",
    "bubblewrap",
    "xdg-dbus-proxy",
    "gobject-introspection",
    "xmlto",
    "gtk-doc-tools",
    "gettext-devel",
]
makedepends = [
    "libcap-devel",
    "libarchive-devel",
    "glib-devel",
    "libxml2-devel",
    "libcurl-devel",
    "gpgme-devel",
    "polkit-devel",
    "fuse-devel",
    "ostree-devel",
    "json-glib-devel",
    "appstream-devel",
    "appstream-glib-devel",
    "gdk-pixbuf-devel",
    "libseccomp-devel",
    "gcab-devel",
    "libxau-devel",
    "zstd-devel",
]
checkdepends = ["bash"]
depends = [
    "bubblewrap",
    "desktop-file-utils",
    "gtk-update-icon-cache",
    "shared-mime-info",
    "xdg-dbus-proxy",
    "kmod",
]
pkgdesc = "Linux application sandboxing and distribution framework"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://flatpak.org"
source = f"https://github.com/flatpak/flatpak/releases/download/{pkgver}/flatpak-{pkgver}.tar.xz"
sha256 = "5b70c64ce7ac134e1ea08011256e423ae5c54f277297441583f77d013f27ffac"
file_modes = {
    "var/lib/flatpak": ("_flatpak", "_flatpak", 0o755),
}
# test runner expects a different env (possible FIXME?)
options = ["!check", "!cross"]

system_users = [
    {
        "name": "_flatpak",
        "id": None,
        "home": "/var/lib/flatpak",
    }
]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True),
    self.rm(self.destdir / "usr/lib/sysusers.d", recursive=True)

    self.install_dir("var/lib/flatpak", empty=True)

    self.install_file(
        self.files_path / "modules-load.conf",
        "usr/lib/modules-load.d",
        name="flatpak.conf",
    )


@subpackage("flatpak-devel")
def _devel(self):
    return self.default_devel()
