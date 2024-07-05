pkgname = "networkmanager"
pkgver = "1.48.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd_journal=false",
    "-Dselinux=false",
    "-Dovs=false",
    "-Dqt=false",
    "-Dsession_tracking_consolekit=false",
    "-Dmodify_system=true",
    "-Diwd=true",
    # we only support dhcpcd here
    "-Ddhclient=/usr/bin/dhclient",
    "-Ddhcpcd=/usr/bin/dhcpcd",
    "-Diptables=/usr/bin/iptables",
    "-Dnft=/usr/bin/nft",
    "-Dresolvconf=/usr/bin/resolvconf",
    "-Ddnsmasq=/usr/bin/dnsmasq",
    "-Dpppd=/usr/bin/pppd",
    "-Ddhcpcanon=no",
    "-Dlibaudit=no",
    "-Dsystemdsystemunitdir=no",
    "-Dconfig_logging_backend_default=syslog",
    "-Dconfig_dns_rc_manager_default=resolvconf",
    # we might want to switch to iwd at some point, but not now
    "-Dconfig_wifi_backend_default=wpa_supplicant",
    "-Dconfig_dhcp_default=internal",
    "-Dkernel_firmware_dir=/usr/lib/firmware",
    "-Ddbus_conf_dir=/usr/share/dbus-1/system.d",
    "-Dudev_dir=/usr/lib/udev",
    "-Dpppd_plugin_dir=/usr/lib/pppd/2.5.0",
    "-Dsession_tracking=elogind",
    "-Dsuspend_resume=elogind",
    "-Dvapi=true",
    "-Dintrospection=true",
    "-Ddocs=true",
    "-Dcrypto=nss",
    "-Dreadline=libedit",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "vala",
    "glib-devel",
    "gettext",
    "xsltproc",
    "docbook-xsl-nons",
    "gtk-doc-tools",
    "python-gobject",
    "jansson-devel",
    "perl",
    "bash",
]
makedepends = [
    "libuuid-devel",
    "nss-devel",
    "dbus-devel",
    "libgudev-devel",
    "libnl-devel",
    "polkit-devel",
    "libcurl-devel",
    "libedit-devel",
    "jansson-devel",
    "libpsl-devel",
    "udev-devel",
    "elogind-devel",
    "libgirepository-devel",
    "libndp-devel",
    "newt-devel",
    "python-gobject",
    "linux-headers",
    "modemmanager-devel",
    "ppp-devel",
    "mobile-broadband-provider-info",
]
depends = [
    "wpa_supplicant",
    "resolvconf",
    "iproute2",
    "mobile-broadband-provider-info",
]
checkdepends = ["python-dbus"]
pkgdesc = "Network management daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/NetworkManager"
source = (
    f"$(GNOME_SITE)/NetworkManager/{pkgver[:-2]}/NetworkManager-{pkgver}.tar.xz"
)
sha256 = "f25f35fe2ea1a473f7d184ccc72c8d4adc9705926fe4f3a7a3c8549941f56b03"
# some tests use sysfs, + LD_BIND_NOW in tests does not work with our musl env
options = ["!check", "!cross", "linkundefver"]

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}


def post_install(self):
    self.install_service(self.files_path / "networkmanager")
    self.install_file(
        self.files_path / "NetworkManager.conf", "etc/NetworkManager"
    )
    self.install_file(
        self.files_path / "50-org.freedesktop.NetworkManager.rules",
        "usr/share/polkit-1/rules.d",
    )
    self.install_tmpfiles(self.files_path / "networkmanager.conf")
    # kill hardlinks
    for f in ["nmtui-connect", "nmtui-hostname", "nmtui-edit"]:
        self.uninstall(f"usr/share/man/man1/{f}.1")
        self.install_link(f"usr/share/man/man1/{f}.1", "nmtui.1")

    self.uninstall("usr/share/man/man5/nm-settings.5")
    self.install_link("usr/share/man/man5/nm-settings.5", "nm-settings-nmcli.5")
    self.uninstall("usr/share/man/man5/nm-system-settings.conf.5")
    self.install_link(
        "usr/share/man/man5/nm-system-settings.conf.5", "NetworkManager.conf.5"
    )


@subpackage("libnm")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("networkmanager-devel")
def _devel(self):
    return self.default_devel()
