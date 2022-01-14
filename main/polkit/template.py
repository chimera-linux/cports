pkgname = "polkit"
pkgver = "0.120"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsession_tracking=libelogind",
    "-Dsystemdsystemunitdir=/tmp",
    "-Dpolkitd_user=_polkitd",
    "-Djs_engine=duktape",
    "-Dauthfw=pam",
    "-Dpam_include=dummy",
    "-Dos_type=redhat", # dummy value
    "-Dman=true",
    "-Dintrospection=true",
    "-Dtests=false", # tests need mocklibc
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "gettext-tiny", "glib-devel",
    "perl", "xsltproc", "docbook-xsl-nons",
]
makedepends = ["elogind-devel", "duktape-devel", "linux-pam-devel"]
pkgdesc = "Toolkit for defining and handling authorizations"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/polkit"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "ee7a599a853117bf273548725719fa92fabd2f136915c7a4906cee98567aee03"
suid_files = [
    "usr/lib/polkit-1/polkit-agent-helper-1",
    "usr/bin/pkexec",
]
file_modes = {
    "etc/polkit-1/rules.d": ("_polkitd:0", "_polkitd:0", 0o700),
    "usr/share/polkit-1/rules.d": ("_polkitd:0", "_polkitd:0", 0o700),
}
# tests are broken on musl
options = ["!check"]

system_users = ["_polkitd"]

def post_install(self):
    self.rm(self.destdir / "tmp", recursive = True)
    self.rm(self.destdir / "etc/pam.d/polkit-1")
    self.install_file(
        self.files_path / "polkit-1.pam", "etc/pam.d", name = "polkit-1"
    )
    self.install_dir("usr/share/polkit-1/rules.d", mode = 0o700, empty = True)
    self.install_service(self.files_path / "polkitd")

@subpackage("polkit-devel")
def _devel(self):
    return self.default_devel()
