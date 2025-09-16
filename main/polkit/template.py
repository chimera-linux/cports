pkgname = "polkit"
pkgver = "126"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsession_tracking=elogind",
    "-Dsystemdsystemunitdir=",
    "-Dpolkitd_user=_polkitd",
    "-Dauthfw=pam",
    "-Dpam_include=dummy",
    "-Dos_type=redhat",  # dummy value
    "-Dman=true",
    "-Dintrospection=true",
    "-Dtests=false",  # tests need mocklibc
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "docbook-xsl-nons",
    "dinit-chimera",
    "dinit-dbus",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxslt-progs",
    "meson",
    "perl",
    "pkgconf",
]
makedepends = ["duktape-devel", "elogind-devel", "linux-pam-devel"]
depends = ["dinit-dbus"]
pkgdesc = "Toolkit for defining and handling authorizations"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/polkit"
source = (
    f"https://github.com/polkit-org/polkit/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "2814a7281989f6baa9e57bd33bbc5e148827e2721ccef22aaf28ab2b376068e8"
file_modes = {
    "usr/lib/polkit-1/polkit-agent-helper-1": ("root", "root", 0o4755),
    "usr/bin/pkexec": ("root", "root", 0o4755),
}
# tests are broken on musl
options = ["!check", "!cross"]


def post_install(self):
    # use our own
    self.uninstall("usr/lib/pam.d/polkit-1")
    self.uninstall("usr/lib/sysusers.d")
    self.uninstall("usr/lib/tmpfiles.d")
    self.uninstall("usr/lib/systemd/system")
    self.install_file(
        self.files_path / "polkit-1.pam", "usr/lib/pam.d", name="polkit-1"
    )
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "polkitd")


@subpackage("polkit-devel")
def _(self):
    return self.default_devel()
