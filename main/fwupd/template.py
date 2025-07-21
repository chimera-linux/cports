pkgname = "fwupd"
pkgver = "2.0.8"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Ddefault_library=shared",
    "-Ddocs=disabled",
    "-Defi_binary=false",
    "-Delogind=enabled",
    "-Dintrospection=enabled",
    "-Dsupported_build=enabled",
    "-Dsystemd=disabled",
]
hostmakedepends = [
    "fonts-dejavu",
    "gcab",
    "gettext",
    "gnutls-progs",
    "gobject-introspection",
    "hwdata",
    "meson",
    "pkgconf",
    "protobuf-c",
    "python-gobject",
    "python-jinja2",
    "vala",
]
makedepends = [
    "cairo-devel",
    "curl-devel",
    "elogind-devel",
    "flashrom-devel",
    "gcab-devel",
    "gnutls-devel",
    "gpgme-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libcbor-devel",
    "libdrm-devel",
    "libjcat-devel",
    "libmbim-devel",
    "libqmi-devel",
    "libusb-devel",
    "libxmlb-devel",
    "linux-headers",
    "modemmanager-devel",
    "pango-devel",
    "polkit-devel",
    "protobuf-c-devel",
    "sqlite-devel",
    "tpm2-tss-devel",
]
depends = ["hwdata-usb", "shared-mime-info", "udisks"]
pkgdesc = "Firmware updater"
license = "LGPL-2.1-or-later"
url = "https://github.com/fwupd/fwupd"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "354f2e217a5e87bb153815268430d7407c59a27f56acbfa8a3c7f34e6c5fd2da"
options = ["!cross"]

_have_uefi = False

match self.profile().arch:
    case "x86_64" | "aarch64" | "loongarch64" | "riscv64":
        _have_uefi = True

if _have_uefi:
    makedepends += ["efivar-devel"]
    if self.profile().arch not in ["loongarch64", "riscv64"]:
        depends += ["fwupd-efi"]


def post_install(self):
    self.install_completion(
        "data/bash-completion/fwupdmgr", "bash", name="fwupdmgr"
    )
    self.install_completion(
        "data/bash-completion/fwupdtool", "bash", name="fwupdtool"
    )
    # nuke installed tests
    self.uninstall("usr/share/fwupd/remotes.d/fwupd-tests.conf")
    self.uninstall("usr/lib/installed-tests")
    self.uninstall("usr/share/installed-tests")


@subpackage("fwupd-devel")
def _(self):
    return self.default_devel()
