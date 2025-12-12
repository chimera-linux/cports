pkgname = "systemd"
pkgver = "259_rc3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dlibc=musl",
    "-Dbootloader=enabled",
    "-Defi=true",
    "-Dman=enabled",
    "-Dukify=enabled",
    "-Dbpf-compiler=clang",
    "-Dsplit-bin=false",
    "-Dsysvinit-path=",
    # features that can't work for now
    "-Dhomed=disabled",
    "-Dnss-mymachines=disabled",
    "-Dnss-resolve=disabled",
    "-Dgshadow=false",
    "-Dmachined=false",
    "-Dnsresourced=false",
    "-Dnss-myhostname=false",
    "-Dnss-systemd=false",
    "-Dresolve=false",
    "-Duserdb=false",
    "-Dutmp=false",
    # features we don't care about
    "-Dkernel-install=false",
    # secure boot
    "-Dsbat-distro=chimera",
    "-Dsbat-distro-summary=Chimera Linux",
    "-Dsbat-distro-pkgname=systemd-boot",
    "-Dsbat-distro-url=https://chimera-linux.org",
    f"-Dsbat-distro-version={self.full_pkgver}",
]
hostmakedepends = [
    "bash",
    "bpftool",
    "docbook-xsl-nons",
    "gperf",
    "libxslt-progs",
    "meson",
    "perl",
    "pkgconf",
    "python-jinja2",
    "python-pefile",
    "python-pyelftools",
    "python-zstandard",
    "rsync",
]
makedepends = [
    "acl-devel",
    "cryptsetup-devel",
    "curl-devel",
    "dbus-devel",
    "elfutils-devel",
    "kmod-devel",
    "libarchive-devel",
    "libbpf-devel",
    "libcap-devel",
    "libfido2-devel",
    "libgcrypt-devel",
    "libidn2-devel",
    "libmicrohttpd-devel",
    "libpwquality-devel",
    "libseccomp-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "linux-pam-devel",
    "lz4-devel",
    "p11-kit-devel",
    "pcre2-devel",
    "qrencode-devel",
    "tpm2-tss-devel",
    "util-linux-blkid-devel",
    "util-linux-fdisk-devel",
    "util-linux-mount-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["xz", "perl"]
depends = [
    self.with_pkgver("systemd-measure"),
    self.with_pkgver("systemd-sysusers"),
    self.with_pkgver("systemd-tmpfiles"),
    self.with_pkgver("systemd-udev"),
]
pkgdesc = "System and service manager"
license = "LGPL-2.1-or-later"
url = "https://github.com/systemd/systemd"
source = f"{url}/archive/refs/tags/v{pkgver.replace('_', '-')}.tar.gz"
sha256 = "89241b11eca4ea5019f75ea5794d356d153c541c166844550d11f140891d6993"


def init_configure(self):
    # bypass some ugly configure checks
    self.configure_args.append(f"-Dtime-epoch={self.source_date_epoch}")


def post_install(self):
    self.uninstall("usr/share/factory")
    # rename for upgrade from sd-tools
    # apk symlink replacement is wonky
    self.rename("usr/bin/systemd-sysusers", "sd-sysusers")
    self.rename("usr/bin/systemd-tmpfiles", "sd-tmpfiles")
    self.install_link("usr/bin/systemd-sysusers", "sd-sysusers")
    self.install_link("usr/bin/systemd-tmpfiles", "sd-tmpfiles")
    # udev initramfs-tools
    self.install_initramfs(self.files_path / "udev.hook", name="udev")
    self.install_initramfs(self.files_path / "udev.init-top", "init-top", name="udev")
    self.install_initramfs(self.files_path / "udev.init-bottom", "init-bottom", name="udev")
    # misc udev stuff
    self.install_tmpfiles(self.files_path / "udev-tmpfiles.conf", name="udev")
    # systemd-boot stuff
    self.install_file(
        self.files_path / "99-gen-systemd-boot.sh",
        "usr/lib/kernel.d",
        mode=0o755,
    )
    self.install_bin(
        self.files_path / "gen-systemd-boot.sh", name="gen-systemd-boot"
    )
    self.install_file(self.files_path / "systemd-boot", "usr/lib/systemd/boot")



@subpackage("systemd-udev-devel")
def _(self):
    self.subdesc = "udev development files"
    self.renames = ["udev-devel"]

    return [
        "usr/include/libudev.h",
        "usr/lib/libudev.so",
        "usr/lib/pkgconfig/libudev.pc",
        "usr/share/man/man3/*udev*",
        "usr/share/pkgconfig/udev.pc",
    ]


@subpackage("systemd-udev-libs")
def _(self):
    self.subdesc = "udev libraries"
    self.renames = ["udev-libs"]

    return ["usr/lib/libudev.*"]


@subpackage("systemd-udev")
def _(self):
    self.subdesc = "device manager"
    self.renames = ["udev"]

    return [
        "etc/udev",
        "usr/bin/systemd-hwdb",
        "usr/bin/udevadm",
        "usr/lib/systemd/network/99-default.link",
        "usr/lib/systemd/systemd-udevd",
        "usr/lib/tmpfiles.d/udev.conf",
        "usr/lib/udev",
        "usr/share/initramfs-tools/hooks/udev",
        "usr/share/initramfs-tools/scripts/init-*/udev",
        "usr/share/man/man*/*hwdb*",
        "usr/share/man/man*/*udev*",
    ]


@subpackage("systemd-udev-meta")
def _(self):
    self.pkgdesc = "Base package for udev configs"
    self.depends = [self.with_pkgver("systemd-udev")]
    self.install_if = [self.with_pkgver("systemd-udev")]
    # base-udev is transitional
    self.provides = [
        self.with_pkgver("udev-meta"),
        self.with_pkgver("base-udev"),
    ]
    self.options = ["empty"]

    return []


@subpackage("systemd-sysusers")
def _(self):
    self.subdesc = "sysusers tool"
    self.replaces = ["sd-tools<1"]

    return ["cmd:sd-sysusers", "cmd:systemd-sysusers"]


@subpackage("systemd-tmpfiles")
def _(self):
    self.subdesc = "tmpfiles tool"
    self.replaces = ["sd-tools<1"]

    return ["cmd:sd-tmpfiles", "cmd:systemd-tmpfiles"]


@subpackage("systemd-measure")
def _(self):
    self.subdesc = "measure tool"
    self.replaces = ["systemd-boot-ukify<257"]

    return ["usr/lib/systemd/systemd-measure", "usr/share/man/man1/systemd-measure.*"]


# only practical for efi so we constrain it by sd-boot
@subpackage("systemd-ukify")
def _(self):
    self.pkgdesc = "Tool to generate Unified Kernel Images"
    self.renames = ["ukify", "systemd-boot-ukify"]
    self.depends = [
        self.with_pkgver("systemd-boot-efi"),
        self.with_pkgver("systemd-measure"),
        "cmd:readelf!llvm-binutils",
        "python-pefile",
        "python-zstandard",
        "tpm2-tss",  # dlopened
    ]

    return ["cmd:ukify", "usr/lib/systemd/ukify"]


@subpackage("systemd-boot-efi")
def _(self):
    self.pkgdesc = "UEFI boot manager"
    self.subdesc = "EFI binaries"

    return [
        "usr/lib/systemd/boot/efi",
        "usr/share/man/man7/linux*.efi.stub.7",
        "usr/share/man/man7/systemd-stub.7",
        "usr/share/man/man7/sd-stub.7",
    ]


@subpackage("systemd-boot")
def _(self):
    self.subdesc = "bootloader"

    return [
        "cmd:bootctl",
        "cmd:gen-systemd-boot",
        "usr/lib/kernel.d/*systemd*",
        "usr/lib/systemd/boot",
    ]


@subpackage("systemd-devel")
def _(self):
    return self.default_devel()


@subpackage("systemd-shared-libs")
def _(self):
    return ["usr/lib/systemd/libsystemd-*.so"]


@subpackage("systemd-libs")
def _(self):
    return self.default_libs()
