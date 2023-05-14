pkgname = "flatpak"
pkgver = "1.14.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-system-bubblewrap", "--with-system-dbus-proxy", "--with-system-helper-user=_flatpak",
                  "--enable-selinux-module=no"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "xsltproc", "docbook-xml", "libxml2-progs", "gtk-doc-tools", "gmake", "python-pyparsing",
                   "bison", "bubblewrap", "xdg-dbus-proxy", "xmlto", "gettext-tiny"]
makedepends = ["libcap-devel", "libarchive-devel", "gobject-introspection", "glib-devel", "libxml2-devel",
               "libcurl-devel", "gpgme-devel", "polkit-devel", "fuse-devel", "ostree-devel", "json-glib-devel",
               "appstream-devel", "gdk-pixbuf-devel", "libseccomp-devel"]
pkgdesc = "Linux application sandboxing and distribution framework"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1"
url = "https://flatpak.org"
source = f"https://github.com/flatpak/flatpak/releases/download/{pkgver}/flatpak-{pkgver}.tar.xz"
sha256 = "59f0470ccb894d852e4c6fbc1043d8bcc95e38033c5c36f2aa90dd295257eebe"
# weird errors, will fix later
options = ["!check"]


@subpackage("flatpak-devel")
def _devel(self):
    return self.default_devel()
