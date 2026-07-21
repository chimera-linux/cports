pkgname = "networkmanager"
pkgver = "1.58.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd_journal=false",
    "-Dselinux=false",
    "-Dovs=false",
    "-Dqt=false",
    "-Dsession_tracking_consolekit=false",
    "-Diwd=true",
    "-Ddhcpcd=/usr/bin/dhcpcd",
    "-Diptables=/usr/bin/iptables",
    "-Dmodprobe=/usr/bin/modprobe",
    "-Dnft=/usr/bin/nft",
    "-Dresolvconf=/usr/bin/resolvconf",
    "-Ddnsmasq=/usr/bin/dnsmasq",
    "-Dpppd=/usr/bin/pppd",
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
    "-Dpppd_plugin_dir=/usr/lib/pppd/2.5.2",
    "-Dsession_tracking=elogind",
    "-Dsuspend_resume=elogind",
    "-Dvapi=true",
    "-Dintrospection=true",
    "-Ddocs=true",
    "-Dcrypto=nss",
    "-Dreadline=libedit",
    "-Dtests=no",  # not ran
    "-Dsystemdsystemgeneratordir=no",
]
hostmakedepends = [
    "bash",
    "bpftool",
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "jansson-devel",
    "libxslt-progs",
    "meson",
    "perl",
    "pkgconf",
    "python-gobject",
    "vala",
]
makedepends = [
    "curl-devel",
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "elogind-devel",
    "gobject-introspection-devel",
    "jansson-devel",
    "libbpf-devel",
    "libedit-devel",
    "libgudev-devel",
    "libndp-devel",
    "libnl-devel",
    "libnvme-devel",
    "libpsl-devel",
    "linux-headers",
    "mobile-broadband-provider-info",
    "modemmanager-devel",
    "newt-devel",
    "nss-devel",
    "polkit-devel",
    "ppp-devel",
    "python-gobject",
    "udev-devel",
    "util-linux-uuid-devel",
]
depends = [
    "dinit-dbus",
    "iproute2",
    "mobile-broadband-provider-info",
    "resolvconf",
    "wpa_supplicant",
]
checkdepends = ["python-dbus"]
pkgdesc = "Network management daemon"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/NetworkManager/NetworkManager"
source = f"{url}/-/archive/{pkgver}/NetworkManager-{pkgver}.tar.gz"
sha256 = "b564614be46fafe6654a497836c48bdbd411ed14d34a525dbf0cd549e33b4cda"
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# some tests use sysfs, + LD_BIND_NOW in tests does not work with our musl env
options = ["etcfiles", "!check", "!cross", "linkundefver"]


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


@subpackage("networkmanager-libs")
def _(self):
    self.renames = ["libnm"]

    return self.default_libs()


@subpackage("networkmanager-devel")
def _(self):
    return self.default_devel()
