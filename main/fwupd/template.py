pkgname = "fwupd"
pkgver = "2.0.0"
pkgrel = 1
build_style = "meson"
configure_args = [
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
    "elogind-devel",
    "flashrom-devel",
    "gcab-devel",
    "gnutls-devel",
    "gpgme-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libcbor-devel",
    "libcurl-devel",
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/fwupd/fwupd"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "6957160bd6fb8f4e126f538d387f3b5fe8a591440fae3ec7a793fee31ffd5e81"
options = ["!cross"]

_have_uefi = False
_have_uefi_capsule = False
_have_msr = self.profile().arch == "x86_64"

match self.profile().arch:
    case "x86_64" | "aarch64" | "riscv64":
        _have_uefi = True

if _have_uefi:
    makedepends += ["efivar-devel"]
    if self.profile().arch != "riscv64":
        depends += ["fwupd-efi"]
        _have_uefi_capsule = True
    else:
        configure_args += ["-Dplugin_uefi_capsule=disabled"]
else:
    configure_args += [
        "-Dplugin_redfish=disabled",
        "-Dplugin_uefi_capsule=disabled",
        "-Dplugin_uefi_pk=disabled",
    ]

if not _have_msr:
    configure_args += ["-Dplugin_msr=disabled"]


def post_install(self):
    self.install_completion(
        "data/bash-completion/fwupdmgr", "bash", name="fwupdmgr"
    )
    self.install_completion(
        "data/bash-completion/fwupdtool", "bash", name="fwupdtool"
    )
    # nuke installed tests
    self.uninstall("usr/share/fwupd/remotes.d/fwupd-tests.conf")
    self.uninstall("usr/libexec/installed-tests")
    self.uninstall("usr/share/fwupd/device-tests")
    self.uninstall("usr/share/installed-tests")


@subpackage("fwupd-devel")
def _(self):
    return self.default_devel()
