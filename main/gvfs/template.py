pkgname = "gvfs"
pkgver = "1.48.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemduserunitdir=no", "-Dtmpfilesdir=no", "-Dlogind=true",
    "-Dman=true",
    # TODOs
    "-Dafc=false", # libplist, libimobiledevice
    "-Ddnssd=false", # avahi-glib
    "-Dgoogle=false", # libgdata
    "-Dhttp=false", # libsoup2
    "-Dmtp=false", # libmtp
    "-Dnfs=false", # libnfs
    "-Dsmb=false", # smbclient
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "xsltproc", "openssh", "polkit-devel",
    "docbook-xsl-nons", "gettext-tiny",
]
makedepends = [
    "dbus-devel", "libglib-devel", "fuse-devel", "libarchive-devel",
    "bluez-devel", "libbluray-devel", "libcap-devel", "gcr-devel",
    "libcdio-paranoia-devel", "libgcrypt-devel", "libgphoto2-devel",
    "libgudev-devel", "libsecret-devel", "libxml2-devel", "polkit-devel",
    "udisks-devel", "gsettings-desktop-schemas-devel", "elogind-devel",
    "libusb-devel", "gnome-online-accounts-devel",
]
# some shared libs that modules depend on
provides = ["so:libgvfscommon.so=0", "so:libgvfsdaemon.so=0"]
pkgdesc = "GNOME virtual file system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/gvfs"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b2ea4f271aad2711f16b43c03151e2ec5a9874ff1a21142ef6d6406486a19dc2"

@subpackage("gvfs-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()

@subpackage("gvfs-afp")
def _afp(self):
    self.pkgdesc = f"{pkgdesc} (Apple Filing Protocol backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfsd-afp*",
        "usr/share/gvfs/mounts/afp*",
    ]

@subpackage("gvfs-cdda")
def _afp(self):
    self.pkgdesc = f"{pkgdesc} (CD-ROM backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfsd-cd*",
        "usr/share/gvfs/mounts/cd*",
    ]

@subpackage("gvfs-goa")
def _afp(self):
    self.pkgdesc = f"{pkgdesc} (Gnome Online Accounts backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfs-goa*",
        #"usr/libexec/gvfsd-google", TODO: for libgdata
        #"usr/share/gvfs/mounts/google.mount",
        "usr/share/dbus-1/services/org.gtk.vfs.GoaVolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/goa.monitor",
    ]

@subpackage("gvfs-gphoto2")
def _afp(self):
    self.pkgdesc = f"{pkgdesc} (gphoto2 backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfs*-gphoto*",
        "usr/share/dbus-1/services/org.gtk.vfs.GPhoto2VolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/gphoto2.monitor",
    ]
