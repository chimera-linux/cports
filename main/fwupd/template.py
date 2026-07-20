pkgname = "fwupd"
pkgver = "2.1.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Ddocs=disabled",
    "-Defi_binary=false",
    "-Dlogind=enabled",
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
    "libdrm-devel",
    "libmbim-devel",
    "libqmi-devel",
    "libusb-devel",
    "libxmlb-devel",
    "linux-headers",
    "modemmanager-devel",
    "pango-devel",
    "polkit-devel",
    "sqlite-devel",
    "tpm2-tss-devel",
]
depends = ["hwdata-usb", "polkit", "shared-mime-info", "udisks"]
pkgdesc = "Firmware updater"
license = "LGPL-2.1-or-later"
url = "https://github.com/fwupd/fwupd"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "03f45f637a7178839f9f4894f86f4cb0ff4e2fc8d04a9a4da5af3157404ac369"
options = ["etcfiles", "!cross"]

if self.profile().arch == "x86_64":
    configure_args += ["-Dhsi=enabled"]
else:
    configure_args += ["-Dhsi=disabled"]

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
