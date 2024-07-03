pkgname = "gvfs"
pkgver = "1.54.2"
pkgrel = 1
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
    "meson",
    "openssh",
    "pkgconf",
    "polkit-devel",
    "xsltproc",
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
    "libsmbclient-devel",
    "libsoup-devel",
    "libusb-devel",
    "libxml2-devel",
    "msgraph-devel",
    "polkit-devel",
    "udisks-devel",
]
depends = ["desktop-file-utils"]
# some shared libs that modules depend on
provides = ["so:libgvfscommon.so=0", "so:libgvfsdaemon.so=0"]
pkgdesc = "GNOME virtual file system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/gvfs"
source = f"$(GNOME_SITE)/gvfs/{pkgver[:-2]}/gvfs-{pkgver}.tar.xz"
sha256 = "54908f4e10b5f1c231e90330c8c15b7f21f2bb610f194c034b338e379c508e3c"


@subpackage("gvfs-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()


@subpackage("gvfs-afc")
def _afc(self):
    self.pkgdesc = f"{pkgdesc} (Apple mobile device backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfsd-afc*",
        "usr/libexec/gvfs-afc-volume-monitor",
        "usr/share/dbus-1/services/org.gtk.vfs.AfcVolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/afc.monitor",
    ]


@subpackage("gvfs-afp")
def _afp(self):
    self.pkgdesc = f"{pkgdesc} (Apple Filing Protocol backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfsd-afp*",
        "usr/share/gvfs/mounts/afp*",
    ]


@subpackage("gvfs-cdda")
def _cdda(self):
    self.pkgdesc = f"{pkgdesc} (CD-ROM backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfsd-cd*",
        "usr/share/gvfs/mounts/cd*",
    ]


@subpackage("gvfs-goa")
def _goa(self):
    self.pkgdesc = f"{pkgdesc} (Gnome Online Accounts backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

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
def _gphoto2(self):
    self.pkgdesc = f"{pkgdesc} (gphoto2 backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfs*-gphoto*",
        "usr/share/dbus-1/services/org.gtk.vfs.GPhoto2VolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/gphoto2.monitor",
    ]


@subpackage("gvfs-mtp")
def _mtp(self):
    self.pkgdesc = f"{pkgdesc} (MTP backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfs*-mtp*",
        "usr/share/dbus-1/services/org.gtk.vfs.MTPVolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/mtp.monitor",
        "usr/share/gvfs/mounts/mtp.mount",
    ]


@subpackage("gvfs-smb")
def _smb(self):
    self.pkgdesc = f"{pkgdesc} (SMB/CIFS backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfs*-smb*",
        "usr/share/GConf/gsettings/gvfs-smb.convert",
        "usr/share/glib-2.0/schemas/org.gnome.system.smb.gschema.xml",
        "usr/share/gvfs/mounts/smb*.mount",
    ]
