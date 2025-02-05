# AGPL: forbidden from being a dependency except in special unambiguous cases
pkgname = "ghostscript"
pkgver = "10.04.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-dynamic",
    "--enable-fontconfig",
    "--enable-freetype",
    "--enable-openjpeg",
    "--enable-cups",
    "--disable-compile-inits",
    "--with-ijs",
    "--with-system-libtiff",
    "--with-libpaper",
    "--with-x",
    "--with-jbig2dec",
    "--with-drivers=ALL",
    "--with-fontpath=/usr/share/fonts/Type1:/usr/share/fonts",
]
configure_env = {
    "CUPSCONFIG": "/usr/bin/cups-config",
    "CCAUX": "cc",
}
configure_gen = []
make_dir = "."  # bad build system
make_build_args = ["all", "so"]
make_install_args = ["install", "install-so"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "cups-devel",
    "dbus-devel",
    "fontconfig-devel",
    "jasper-devel",
    "jbig2dec-devel",
    "openjpeg-devel",
    "lcms2-devel",
    "libxext-devel",
    "libxt-devel",
    "libpaper-devel",
    "ijs-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "PostScript and PDF language interpreter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "AGPL-3.0-or-later"
url = "https://www.ghostscript.com"
source = f"https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs{pkgver.replace('.', '')}/ghostscript-{pkgver}.tar.xz"
sha256 = "527eef0b6cd04ecf1c8d7a11796c69a52d34ffe36afca86a400729a2fc01c887"
# breaks ps2pdf
hardening = ["!int"]
# busted; undefined references
options = ["!lto"]

if self.profile().cross:
    hostmakedepends += makedepends


def post_patch(self):
    for f in [
        "cups/libs",
        "freetype",
        "ijs",
        "jbig2dec",
        "jpeg",
        "lcms2mt",
        "libpng",
        "openjpeg",
        "tiff",
        "zlib",
    ]:
        self.rm(f, recursive=True)


def init_configure(self):
    self.configure_env["CFLAGSAUX"] = self.get_cflags(target="host", shell=True)
    # work around terrible build system
    self.configure_env["LDFLAGS"] = (
        self.get_cflags(shell=True) + " " + self.get_ldflags(shell=True)
    )


def init_install(self):
    self.make_install_args += [
        "cups_serverroot=" + str(self.chroot_destdir / "etc/cups"),
        "cups_serverbin=" + str(self.chroot_destdir / "usr/lib/cups"),
    ]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("ghostscript-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libgs")]

    return self.default_libs()


@subpackage("ghostscript-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libgs-devel")]

    return self.default_devel()
