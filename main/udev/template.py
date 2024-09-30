pkgname = "udev"
pkgver = "256.6"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dacl=enabled",
    "-Dadm-group=false",
    "-Danalyze=false",
    "-Dapparmor=disabled",
    "-Daudit=disabled",
    "-Dbacklight=false",
    "-Dbinfmt=false",
    "-Dbpf-framework=disabled",
    "-Dbzip2=disabled",
    "-Dcoredump=false",
    "-Ddbus=disabled",
    "-Defi=false",
    "-Delfutils=disabled",
    "-Denvironment-d=false",
    "-Dfdisk=disabled",
    "-Dgcrypt=disabled",
    "-Dglib=disabled",
    "-Dgshadow=false",
    "-Dgnutls=disabled",
    "-Dhibernate=false",
    "-Dhostnamed=false",
    "-Didn=false",
    "-Dima=false",
    "-Dinitrd=false",
    "-Dfirstboot=false",
    "-Dkernel-install=false",
    "-Dldconfig=false",
    "-Dlibcryptsetup=disabled",
    "-Dlibcurl=disabled",
    "-Dlibfido2=disabled",
    "-Dlibidn=disabled",
    "-Dlibidn2=disabled",
    "-Dlibiptc=disabled",
    "-Dlocaled=false",
    "-Dlogind=false",
    "-Dlz4=disabled",
    "-Dmachined=false",
    "-Dmicrohttpd=disabled",
    "-Dnetworkd=false",
    "-Dnscd=false",
    "-Dnss-myhostname=false",
    "-Dnss-resolve=disabled",
    "-Dnss-systemd=false",
    "-Doomd=false",
    "-Dopenssl=disabled",
    "-Dp11kit=disabled",
    "-Dpam=disabled",
    "-Dpcre2=disabled",
    "-Dpolkit=disabled",
    "-Dportabled=false",
    "-Dpstore=false",
    "-Dpwquality=disabled",
    "-Drandomseed=false",
    "-Dresolve=false",
    "-Drfkill=false",
    "-Dseccomp=disabled",
    "-Dselinux=disabled",
    "-Dsmack=false",
    "-Dsysext=false",
    "-Dsysusers=false",
    "-Dtimedated=false",
    "-Dtimesyncd=false",
    "-Dtmpfiles=false",
    "-Dtpm=false",
    "-Dqrencode=disabled",
    "-Dquotacheck=false",
    "-Duserdb=false",
    "-Dukify=disabled",
    "-Dutmp=false",
    "-Dvconsole=false",
    "-Dwheel-group=false",
    "-Dxdg-autostart=false",
    "-Dxkbcommon=disabled",
    "-Dxz=disabled",
    "-Dzlib=disabled",
    "-Dzstd=disabled",
    "-Dhwdb=true",
    "-Dman=enabled",
    "-Dstandalone-binaries=true",
    "-Dstatic-libudev=true",
    "-Dtests=false",
    "-Dlink-boot-shared=false",
    "-Dlink-journalctl-shared=false",
    "-Dlink-networkd-shared=false",
    "-Dlink-systemctl-shared=false",
    "-Dlink-timesyncd-shared=false",
    "-Dlink-udev-shared=false",
    "-Dsplit-bin=false",
    "-Dsysvinit-path=",
    "-Drpmmacrosdir=no",
    "-Dpamconfdir=no",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "perl",
    "gperf",
    "bash",
    "docbook-xsl-nons",
    "python-jinja2",
    "xsltproc",
]
makedepends = [
    "acl-devel",
    "libblkid-devel",
    "libmount-devel",
    "libcap-devel",
    "libkmod-devel",
    "linux-headers",
]
checkdepends = ["xz", "perl"]
depends = ["so:libkmod.so.2!libkmod"]
triggers = ["/usr/lib/udev/rules.d", "/usr/lib/udev/hwdb.d", "/etc/udev/hwdb.d"]
pkgdesc = "Standalone build of systemd-udev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/systemd/systemd"
source = (
    f"https://github.com/systemd/systemd/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "c085f162dec001407dd32f00abbf20b7e6ed7043dcfaf8ed954787d86707f409"
patch_style = "patch"
# the tests that can run are mostly useless
options = ["!splitudev", "!check"]

_have_sd_boot = False

# supported efi architectures
match self.profile().arch:
    case "x86_64" | "aarch64" | "riscv64":
        _have_sd_boot = True

if _have_sd_boot:
    configure_args += [
        "-Dbootloader=enabled",
        "-Defi=true",
        # secure boot
        "-Dsbat-distro=chimera",
        "-Dsbat-distro-summary=Chimera Linux",
        "-Dsbat-distro-pkgname=systemd-boot",
        "-Dsbat-distro-url=https://chimera-linux.org",
        f"-Dsbat-distro-version={self.full_pkgver}",
    ]
    hostmakedepends += ["python-pyelftools"]


def init_configure(self):
    # bypass some ugly configure checks
    self.configure_args.append(f"-Dtime-epoch={self.source_date_epoch}")


def post_patch(self):
    # the patch won't rename
    self.mv("man/systemd-hwdb.xml", "man/udev-hwdb.xml")


def post_install(self):
    # oh boy, big cleanup time

    # drop some more systemd bits
    for f in [
        "etc/systemd",
        "usr/lib/libsystemd.*",
        "usr/lib/pkgconfig/libsystemd.pc",
        "usr/share/dbus-1",
        "usr/share/pkgconfig/systemd.pc",
        "usr/share/polkit-1",
    ]:
        self.uninstall(f, glob=True)

    for f in (self.destdir / "usr/lib/systemd").iterdir():
        # keep efi stubs
        if f.name == "boot":
            continue
        self.rm(f, recursive=True, glob=True)

    # predictable interface names
    self.install_file(
        self.files_path / "80-net-name-slot.rules",
        "usr/lib/udev/rules.d",
        mode=0o644,
    )

    # initramfs-tools
    self.install_initramfs(self.files_path / "udev.hook")
    self.install_initramfs(self.files_path / "udev.init-top", "init-top")
    self.install_initramfs(self.files_path / "udev.init-bottom", "init-bottom")
    # services
    self.install_dir("usr/libexec")
    self.install_link("usr/libexec/udevd", "../bin/udevadm")
    self.install_file(
        self.files_path / "udevd.wrapper", "usr/libexec", mode=0o755
    )
    self.install_file(self.files_path / "dinit-devd", "usr/libexec", mode=0o755)
    self.install_tmpfiles(self.files_path / "tmpfiles.conf", name="udev")
    self.install_service(self.files_path / "udevd", enable=True)
    # systemd-boot
    if _have_sd_boot:
        self.install_file("build/systemd-bless-boot", "usr/libexec", mode=0o755)
        self.install_file(
            self.files_path / "99-gen-systemd-boot.sh",
            "usr/lib/kernel.d",
            mode=0o755,
        )
        self.install_bin(
            self.files_path / "gen-systemd-boot.sh", name="gen-systemd-boot"
        )
        self.install_file(self.files_path / "systemd-boot", "etc/default")


@subpackage("udev-devel")
def _(self):
    return self.default_devel()


@subpackage("udev-libs")
def _(self):
    return self.default_libs()


@subpackage("systemd-boot", _have_sd_boot)
def _(self):
    self.pkgdesc = "UEFI boot manager"
    self.depends += [self.with_pkgver("systemd-boot-efi")]

    return [
        "etc/default/systemd-boot",
        "usr/bin/bootctl",
        "usr/bin/gen-systemd-boot",
        "usr/lib/kernel.d/99-gen-systemd-boot.sh",
        "usr/libexec/systemd-bless-boot",
        "usr/share/bash-completion/completions/bootctl",
        "usr/share/zsh/site-functions/_bootctl",
        "usr/share/man/man1/bootctl.1",
        "usr/share/man/man5/loader.conf.5",
        "usr/share/man/man7/sd-boot.7",
        "usr/share/man/man7/systemd-boot.7",
    ]


@subpackage("systemd-boot-efi", _have_sd_boot)
def _(self):
    self.pkgdesc = "UEFI boot manager"
    self.subdesc = "EFI binaries"

    return [
        "usr/lib/systemd/boot/efi",
        "usr/share/man/man7/linux*.efi.stub.7",
        "usr/share/man/man7/systemd-stub.7",
        "usr/share/man/man7/sd-stub.7",
    ]


@subpackage("base-udev")
def _(self):
    self.pkgdesc = "Base package for udev configs"
    self.depends = [self.parent]
    self.install_if = [self.parent]
    self.options = ["empty"]

    return []
