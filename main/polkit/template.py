pkgname = "polkit"
pkgver = "125"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsession_tracking=elogind",
    "-Dsystemdsystemunitdir=",
    "-Dpolkitd_user=_polkitd",
    "-Djs_engine=duktape",
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
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "perl",
    "pkgconf",
    "xsltproc",
]
makedepends = ["duktape-devel", "elogind-devel", "linux-pam-devel"]
pkgdesc = "Toolkit for defining and handling authorizations"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/polkit"
source = (
    f"https://github.com/polkit-org/polkit/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "ea5cd6e6e2afa6bad938ee770bf0c2cd9317910f37956faeba2869adcf3747d1"
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
