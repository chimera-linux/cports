pkgname = "gvfs"
pkgver = "1.56.1"
pkgrel = 3
build_style = "meson"
configure_args = [
    "-Dsystemduserunitdir=no",
    "-Dtmpfilesdir=no",
    "-Dlogind=true",
    "-Dman=true",
    "-Dgoogle=false",  # TODO libgdata
]
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "libxslt-progs",
    "meson",
    "openssh",
    "pkgconf",
    "polkit-devel",
]
makedepends = [
    "avahi-glib-devel",
    "bluez-devel",
    "dbus-devel",
    "elogind-devel",
    "fuse-devel",
    "gcr-devel",
    "glib-devel",
    "gnome-online-accounts-devel",
    "gsettings-desktop-schemas-devel",
    "libarchive-devel",
    "libbluray-devel",
    "libcap-devel",
    "libcdio-paranoia-devel",
    "libgcrypt-devel",
    "libgphoto2-devel",
    "libgudev-devel",
    "libimobiledevice-devel",
    "libmtp-devel",
    "libnfs-devel",
    "libplist-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libusb-devel",
    "libxml2-devel",
    "msgraph-devel",
    "polkit-devel",
    "samba-client-devel",
    "udisks-devel",
]
depends = ["desktop-file-utils"]
# some shared libs that modules depend on
provides = ["so:libgvfscommon.so=0", "so:libgvfsdaemon.so=0"]
pkgdesc = "GNOME virtual file system"
license = "LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/gvfs"
source = f"$(GNOME_SITE)/gvfs/{pkgver[:-2]}/gvfs-{pkgver}.tar.xz"
sha256 = "86731ccec679648f8734e237b1de190ebdee6e4c8c0f56f454c31588e509aa10"


@subpackage("gvfs-afc")
def _(self):
    self.subdesc = "Apple mobile device backend"
    self.depends += [self.parent]
    self.install_if = [self.parent]

    return [
        "usr/libexec/gvfsd-afc*",
        "usr/libexec/gvfs-afc-volume-monitor",
        "usr/share/dbus-1/services/org.gtk.vfs.AfcVolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/afc.monitor",
    ]


@subpackage("gvfs-afp")
def _(self):
    self.subdesc = "Apple Filing Protocol backend"
    self.depends += [self.parent]
    self.install_if = [self.parent]

    return [
        "usr/libexec/gvfsd-afp*",
        "usr/share/gvfs/mounts/afp*",
    ]


@subpackage("gvfs-cdda")
def _(self):
    self.subdesc = "CD-ROM backend"
    self.depends += [self.parent]
    self.install_if = [self.parent]

    return [
        "usr/libexec/gvfsd-cd*",
        "usr/share/gvfs/mounts/cd*",
    ]


@subpackage("gvfs-goa")
def _(self):
    self.subdesc = "Gnome Online Accounts backend"
    self.depends += [self.parent]
    self.install_if = [self.parent]

    return [
        "usr/libexec/gvfs-goa*",
        "usr/libexec/gvfsd-onedrive",
        "usr/share/gvfs/mounts/onedrive.mount",
        # "usr/libexec/gvfsd-google", TODO: for libgdata
        # "usr/share/gvfs/mounts/google.mount",
        "usr/share/dbus-1/services/org.gtk.vfs.GoaVolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/goa.monitor",
    ]


@subpackage("gvfs-gphoto2")
def _(self):
    self.subdesc = "gphoto2 backend"
    self.depends += [self.parent]
    self.install_if = [self.parent]

    return [
        "usr/libexec/gvfs*-gphoto*",
        "usr/share/dbus-1/services/org.gtk.vfs.GPhoto2VolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/gphoto2.monitor",
    ]


@subpackage("gvfs-mtp")
def _(self):
    self.subdesc = "MTP backend"
    self.depends += [self.parent]
    self.install_if = [self.parent]

    return [
        "usr/libexec/gvfs*-mtp*",
        "usr/share/dbus-1/services/org.gtk.vfs.MTPVolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/mtp.monitor",
        "usr/share/gvfs/mounts/mtp.mount",
    ]


@subpackage("gvfs-smb")
def _(self):
    self.subdesc = "SMB/CIFS backend"
    self.depends += [self.parent]
    self.install_if = [self.parent]

    return [
        "usr/libexec/gvfs*-smb*",
        "usr/share/GConf/gsettings/gvfs-smb.convert",
        "usr/share/glib-2.0/schemas/org.gnome.system.smb.gschema.xml",
        "usr/share/gvfs/mounts/smb*.mount",
    ]
