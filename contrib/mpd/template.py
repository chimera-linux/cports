pkgname = "mpd"
pkgver = "0.23.15"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Ddocumentation=enabled",
    "-Dhtml_manual=true",
    "-Dmanpages=true",
    "-Dsyslog=enabled",
    "-Dinotify=true",
    "-Dio_uring=enabled",
    "-Ddaemon=true",
    "-Dsystemd=disabled",
    "-Depoll=true",
    "-Deventfd=true",
    "-Dsignalfd=true",
    "-Dtcp=true",
    "-Dipv6=enabled",
    "-Dlocal_socket=true",
    # Audio formats
    "-Ddsd=true",
    # Database plugins
    "-Ddatabase=true",
    "-Dupnp=disabled",
    "-Dlibmpdclient=disabled",
    # Neighbor plugins
    "-Dneighbor=true",
    # Storage plugins
    "-Dudisks=enabled",
    "-Dwebdav=enabled",
    # Playlist plugins
    "-Dcue=true",
    # Input plugins
    "-Dcdio_paranoia=enabled",
    "-Dcurl=enabled",
    "-Dmms=enabled",
    "-Dnfs=enabled",
    # Archive plugins
    "-Dbzip2=enabled",
    "-Diso9660=enabled",
    "-Dzzip=disabled",
    # Tag plugins
    "-Did3tag=enabled",
    "-Dchromaprint=enabled",
    # Decoder plugins
    "-Dadplug=disabled",
    "-Daudiofile=enabled",
    "-Dfaad=disabled",
    "-Dffmpeg=enabled",
    "-Dflac=enabled",
    "-Dfluidsynth=enabled",
    "-Dgme=disabled",
    "-Dmad=disabled",
    # MikMod causes a crash
    "-Dmikmod=disabled",
    "-Dmodplug=enabled",
    "-Dopenmpt=disabled",
    "-Dmpcdec=disabled",
    "-Dmpg123=enabled",
    "-Dopus=enabled",
    "-Dsidplay=disabled",
    "-Dsndfile=enabled",
    "-Dtremor=disabled",
    "-Dvorbis=enabled",
    "-Dwavpack=enabled",
    "-Dwildmidi=disabled",
    # Encoder plugins
    "-Dvorbisenc=enabled",
    "-Dlame=enabled",
    "-Dtwolame=enabled",
    "-Dshine=disabled",
    "-Dwave_encoder=true",
    # Filter plugins
    "-Dlibsamplerate=enabled",
    "-Dsoxr=enabled",
    # Output plugins
    "-Dalsa=enabled",
    "-Dao=disabled",
    "-Dfifo=true",
    "-Dhttpd=true",
    "-Djack=enabled",
    "-Dopenal=enabled",
    "-Doss=disabled",
    "-Dpipe=true",
    "-Dpipewire=enabled",
    "-Dpulse=enabled",
    "-Drecorder=true",
    "-Dshout=disabled",
    "-Dsnapcast=true",
    "-Dsndio=disabled",
    "-Dsolaris_output=disabled",
    # Misc libraries
    "-Ddbus=enabled",
    "-Dexpat=enabled",
    "-Dicu=enabled",
    "-Diconv=enabled",
    "-Dpcre=enabled",
    "-Dsqlite=enabled",
    "-Dyajl=enabled",
    "-Dzlib=enabled",
    "-Dzeroconf=avahi",
]
# MPD source tree includes a clashing `build` dir
make_dir = "built"
hostmakedepends = ["pkgconf", "meson", "python-sphinx"]
makedepends = [
    "alsa-lib-devel",
    "audiofile-devel",
    "avahi-devel",
    "boost-devel",
    "bzip2-devel",
    "chromaprint-devel",
    "ffmpeg-devel",
    "flac-devel",
    "fluidsynth-devel",
    "fmt-devel",
    "lame-devel",
    "libcdio-devel",
    "libcdio-paranoia-devel",
    "libcurl-devel",
    "libexpat-devel",
    "libgme-devel",
    "libid3tag-devel",
    "libmms-devel",
    "libmodplug-devel",
    "libnfs-devel",
    "libpulse-devel",
    "libsamplerate-devel",
    "libsndfile-devel",
    "liburing-devel",
    "libvorbis-devel",
    "udisks-devel",
    "mpg123-devel",
    "openal-soft-devel",
    "opus-devel",
    "pcre2-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "soxr-devel",
    "sqlite-devel",
    "twolame-devel",
    "wavpack-devel",
    "yajl-devel",
    "zlib-devel",
]
pkgdesc = "Music player daemon"
maintainer = "nullobsi <nullobsi@unix.dog>"
license = "GPL-2.0-or-later AND BSD-2-Clause"
url = "https://www.musicpd.org"
source = f"{url}/download/{pkgname}/{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "550132239ad1acf82ccf8905b56cc13dc2c81a4489b96fba7731b3049907661a"


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "mpd")
    self.install_file(self.files_path / "mpd.conf", "etc")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file("doc/mpdconf.example", "usr/share/doc/mpd")
