pkgname = "networkmanager"
pkgver = "1.42.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd_journal=false", "-Dselinux=false", "-Dovs=false", "-Dqt=false",
    "-Dsession_tracking_consolekit=false",
    "-Dmodify_system=true", "-Diwd=true",
    # we only support dhcpcd here
    "-Ddhclient=/usr/bin/dhclient", "-Ddhcpcd=/usr/bin/dhcpcd",
    "-Diptables=/usr/bin/iptables", "-Dnft=/usr/bin/nft",
    "-Dresolvconf=/usr/bin/resolvconf", "-Ddnsmasq=/usr/bin/dnsmasq",
    "-Dpppd=/usr/bin/pppd", "-Ddhcpcanon=no",
    "-Dlibaudit=no", "-Dsystemdsystemunitdir=no",
    "-Dconfig_logging_backend_default=syslog",
    "-Dconfig_dns_rc_manager_default=resolvconf",
    # we might want to switch to iwd at some point, but not now
    "-Dconfig_wifi_backend_default=wpa_supplicant",
    "-Dconfig_dhcp_default=internal",
    "-Dkernel_firmware_dir=/usr/lib/firmware",
    "-Ddbus_conf_dir=/etc/dbus-1/system.d",
    "-Dudev_dir=/usr/lib/udev",
    "-Dpppd_plugin_dir=/usr/lib/pppd/2.4.9",
    "-Dsession_tracking=elogind", "-Dsuspend_resume=elogind",
    "-Dvapi=true", "-Dintrospection=true", "-Ddocs=true",
    "-Dcrypto=nss", "-Dreadline=libedit",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "vala", "glib-devel",
    "gettext-tiny", "xsltproc", "docbook-xsl-nons", "gtk-doc-tools",
    "python-gobject", "jansson-devel", "perl", "bash",
]
makedepends = [
    "libuuid-devel", "nss-devel", "dbus-devel", "libgudev-devel",
    "libnl-devel", "polkit-devel", "libcurl-devel", "libedit-devel",
    "jansson-devel", "libpsl-devel", "udev-devel", "elogind-devel",
    "libgirepository-devel", "libndp-devel", "newt-devel", "python-gobject",
    "linux-headers", "modemmanager-devel", "ppp-devel",
    "mobile-broadband-provider-info",
]
depends = [
    "dbus", "wpa_supplicant", "openresolv", "iproute2",
    "mobile-broadband-provider-info",
]
checkdepends = ["python-dbus"]
pkgdesc = "Network management daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/NetworkManager"
source = f"$(GNOME_SITE)/NetworkManager/{pkgver[:-2]}/NetworkManager-{pkgver}.tar.xz"
sha256 = "86ee16a2f7f525629133fa0c3dc060caf96ae4f34084eda1c24551951abe5a3c"
# some tests use sysfs, + LD_BIND_NOW in tests does not work with our musl env
options = ["!check", "!cross"]

def post_install(self):
    self.install_service(self.files_path / "networkmanager")
    self.install_file(
        self.files_path / "NetworkManager.conf", "etc/NetworkManager"
    )
    self.install_file(
        self.files_path / "50-org.freedesktop.NetworkManager.rules",
        "usr/share/polkit-1/rules.d"
    )
    # default dirs
    self.install_dir("etc/NetworkManager/system-connections", empty = True)
    self.install_dir(
        "etc/NetworkManager/dispatcher.d/pre-up.d", empty = True,
        mode = 0o750
    )
    self.install_dir(
        "etc/NetworkManager/dispatcher.d/pre-down.d", empty = True,
        mode = 0o750
    )
    self.install_dir("etc/NetworkManager/VPN", empty = True)
    self.install_dir("var/lib/NetworkManager", empty = True)
    # kill hardlinks
    for f in ["nmtui-connect", "nmtui-hostname", "nmtui-edit"]:
        self.rm(self.destdir / f"usr/share/man/man1/{f}.1")
        self.install_link("nmtui.1", f"usr/share/man/man1/{f}.1")

    self.rm(self.destdir / "usr/share/man/man5/nm-settings.5")
    self.install_link(
        "nm-settings-nmcli.5", "usr/share/man/man5/nm-settings.5"
    )
    self.rm(self.destdir / "usr/share/man/man5/nm-system-settings.conf.5")
    self.install_link(
        "NetworkManager.conf.5", "usr/share/man/man5/nm-system-settings.conf.5"
    )

@subpackage("libnm")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("networkmanager-devel")
def _devel(self):
    return self.default_devel()
